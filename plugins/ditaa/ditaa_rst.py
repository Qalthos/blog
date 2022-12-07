#!/usr/bin/env python
"""Custom reST_ directive for ditaa_ integration.

.. _reST: http://docutils.sourceforge.net/rst.html
.. _ditaa: http://ditaa.sourceforge.net/
"""

from pathlib import Path
from subprocess import Popen, PIPE
import tempfile
from zlib import adler32

from docutils.nodes import image, literal_block
from docutils.parsers.rst import Directive, directives


class DiTAA(Directive):
    required_arguments = 0
    optional_arguments = 0
    has_content = True
    _ditaa_flags = [
        "no-antialias",
        "no-separation",
        "round-corners",
        "no-shadows",
    ]

    option_spec = {
        "name": directives.unchanged,
        "class": directives.class_option,
        "alt": directives.unchanged,
        "scale": directives.percentage,
    }
    for f in _ditaa_flags:
        option_spec[f] = directives.flag

    def run(self):
        settings = self.state.document.settings
        path = Path("content/images/")
        path.mkdir(exist_ok=True)

        nodes = []

        # Y U NO STDINNNNN...
        body = "\n".join(self.content)
        tf = tempfile.NamedTemporaryFile()
        tf.write(body.encode("utf8"))
        tf.flush()

        # make a name
        name = self.options.pop("name", None)
        if not name:
            name = "%08x" % (adler32(body) & 0xFFFFFFFF)
        if not name.endswith(".png"):
            name += ".png"

        alt = self.options.get("alt", "ditaa diagram")
        classes = self.options.pop("class", ["ditaa"])

        filename = path / name
        if not filename.exists():
            cmdline = [
                "ditaa",
                tf.name,
                filename,
                "--overwrite",
                "--encoding",
                "utf8",
            ]

            if "scale" in self.options:
                cmdline.extend(["--scale", "%f" % (float(self.options["scale"]) / 100)])
            for f in self._ditaa_flags:
                if f in self.options:
                    cmdline.append("--" + f)

            try:
                p = Popen(cmdline, stdout=PIPE, stderr=PIPE)
                out, err = p.communicate()
            except Exception as exc:
                error = self.state_machine.reporter.error(
                    "Failed to run ditaa: %s" % (exc,),
                    literal_block(self.block_text, self.block_text),
                    line=self.lineno,
                )
                nodes.append(error)
            else:
                if p.returncode != 0:
                    error = self.state_machine.reporter.error(
                        'Error in "%s" directive: %s' % (self.name, err),
                        literal_block(self.block_text, self.block_text),
                        line=self.lineno,
                    )
                    nodes.append(error)
                    return nodes

        urlpath = "/images"
        url = urlpath + "/" + name
        imgnode = image(uri=url, classes=classes, alt=alt)
        nodes.append(imgnode)
        return nodes


def register():
    """Plugin registration."""
    directives.register_directive("ditaa", DiTAA)
