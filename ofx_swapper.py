#!/usr/bin/env python3

import argparse
import sys
import xml.etree.ElementTree as ET


class OFXSwapper:
    def __init__(self, inputFile):
        self._inputFile = inputFile
        self._tree = ET.parse(self._inputFile)
        self._swap_names_and_memos()

    def _swap_names_and_memos(self):
        root = self._tree.getroot()
        for transaction in root.iter("STMTTRN"):
            name = transaction.find("NAME")
            memo = transaction.find("MEMO")
            if name is None:
                print("Name missing")
                continue
            if memo is None:
                continue
            # print(f'Found "{name.text}" and "{memo.text}"')
            old_memo_text = memo.text
            memo.text = name.text
            name.text = old_memo_text

    def write_file(self, file_name):
        self._tree.write(file_name, encoding="unicode")


def parse_command_line():
    parser = argparse.ArgumentParser(
        description="Swap name and memo fields in an OFX file."
    )
    parser.add_argument(
        "infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument(
        "outfile", nargs="?", type=argparse.FileType("w"), default=sys.stdout
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_command_line()
    swapper = OFXSwapper(args.infile)
    swapper.write_file(args.outfile)
