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
            if name == None:
                print('Name missing')
                continue
            if memo == None:
                continue
            print(f'Found "{name.text}" and "{memo.text}"')
            old_memo_text = memo.text
            memo.text = name.text
            name.text = old_memo_text

    def write_file(self, file_name):
        pass

# tree.write('modified.OFX')
