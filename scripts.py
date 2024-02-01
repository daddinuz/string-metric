import sys
import subprocess


def test():
    match sys.argv[1:]:
        case []:
            subprocess.run(
                ["python", "-u", "-m", "unittest", "discover", "-s", "tests"]
            )
        case _:
            print("USAGE: test")
            sys.exit(1)


def fmt():
    match sys.argv[1:]:
        case []:
            subprocess.run(
                ["python", "-m", "black", "string_metric", "tests", "scripts.py"]
            )
        case _:
            print("USAGE: fmt")
            sys.exit(1)
