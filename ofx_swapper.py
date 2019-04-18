import xml.etree.ElementTree as ET

tree = ET.parse('/Users/paul/Downloads/msmoneyExport.OFX')
root = tree.getroot()
for memo in root.iter('MEMO'):
    print(memo.text)
