import sys
import argparse

def ExecuteCommand():
    """The main routine."""
    parser = argparse.ArgumentParser(description='Command Line Interface for Plainview')
    parser.add_argument("command", help="display a square of a given number",
                    type=str)

    args = parser.parse_args()
