import xml.etree.ElementTree as ET

tree = ET.parse('/Users/paul/Downloads/msmoneyExport.OFX')
root = tree.getroot()
# print(ET.tostring(root))
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

print('***************************************************************************')
for transaction in root.iter('STMTTRN'):
    name = transaction.find('NAME')
    memo = transaction.find('MEMO')
    if name == None:
        print('Name missing')
        continue
    if memo == None:
        continue
    print(f'Found "{name.text}" and "{memo.text}"')

tree.write('modified.OFX')
