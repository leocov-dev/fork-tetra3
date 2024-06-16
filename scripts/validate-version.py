"""
Assert that the git tag version matches the pyproject.toml version.
"""
import argparse
import os
import sys
import toml
from pathlib import Path

__repo = Path(__file__).parent.parent

# make conf.py importable
sys.path.append(str(__repo / 'docs'))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--check-tag", action="store_true")

    args = parser.parse_args()

    import conf
    versions_to_match = [
        conf.release,  # docs version string
    ]

    with open(__repo / "pyproject.toml", "r") as ppt:
        # project version string
        versions_to_match.append(toml.load(ppt)["project"]["version"])

    if args.check_tag:
        # git tag version in github workflows
        versions_to_match.append(os.environ.get("TAG", ""))

    if not all([v == versions_to_match[0] for v in versions_to_match]):
        print(f"versions did not match: {versions_to_match}")
        sys.exit(1)

    print(f"version strings <{versions_to_match[0]}> OK")
