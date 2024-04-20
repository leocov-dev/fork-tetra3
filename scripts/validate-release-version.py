"""
Assert that the git tag version matches the pyproject.toml version.
"""
import os
import sys
import toml
from pathlib import Path
from docs import conf

__repo = Path(__file__).parent.parent

if __name__ == "__main__":

    tag_version = os.environ.get("TAG", "")

    docs_version = conf.release

    with open(__repo / "pyproject.toml", "r") as ppt:
        project_version = toml.load(ppt)["project"]["version"]

    if not (project_version == tag_version):
        print("versions did not match:")
        print(f"project: {project_version}")
        print(f"docs:    {docs_version}")
        print(f"tag:     {tag_version}")
        sys.exit(1)

    print(f"version strings <{project_version}> OK")
