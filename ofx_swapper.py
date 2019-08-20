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
        for transaction in root.iter('STMTTRN'):
            name = transaction.find('NAME')
            memo = transaction.find('MEMO')
            if name is None:
                print('Name missing')
                continue
            if memo is None:
                continue
            # print(f'Found "{name.text}" and "{memo.text}"')
            old_memo_text = memo.text
            memo.text = name.text
            name.text = old_memo_text

    def write_file(self, file_name):
        self._tree.write(file_name, encoding='unicode')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Swap name and memo fields in an OFX file.')
    parser.add_argument('input', help='an OFX file to parse')
    parser.add_argument(
        '--overwrite', '-o',
        help='overwrite input file, otherwise write to stdout',
        action='store_true')
    args = parser.parse_args()

    swapper = OFXSwapper(args.input)
    if args.overwrite:
        swapper.write_file(args.input)
    else:
        swapper.write_file(sys.stdout)
