from hatchling.builders.hooks.plugin.interface import BuildHookInterface

import subprocess
from pathlib import Path
from datetime import datetime

class DocGenBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):

        md_path = Path(self.root + "/Documentation/md2anki.1.md")
        man_path = Path(self.root + "/Documentation/md2anki.1")
        today = datetime.today().strftime('%Y-%m-%d')

        subprocess.run(
            [
                "pandoc",
                "--from=markdown",
                "--standalone",
                "--variable",
                f"footer={str(self.metadata.version)}",
                "--variable",
                f"date={str(today)}",
                "--to=man",
                str(md_path),
                "-o",
                str(man_path),
            ],
            check=True,
        )
