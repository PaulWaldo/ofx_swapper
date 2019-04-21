import unittest
import os
from ofx_swapper import OFXSwapper
import xml.etree.ElementTree as ET


class TestOFXSwapper(unittest.TestCase):

    def test_swap_name_and_memo(self):
        sut = OFXSwapper('test_data/test.ofx')
        root = sut._tree.getroot()

        # Check the first transaction to see if it got swapped
        statements = root.iter('STMTTRN')
        self.assertIsNotNone(statements)
        first_statement = next(statements)
        name = first_statement.find('NAME').text
        self.assertEqual(name, 'Merchant1')
        memo = first_statement.find('MEMO').text
        self.assertEqual(memo, 'DEBIT CARD PURCHASE XXXXX1234')

    def test_write_file_writes_a_file(self):
        sut = OFXSwapper('test_data/test.ofx')
        test_file = 'test.ofx'
        sut.write_file(test_file)
        self.assertTrue(os.access(test_file, os.F_OK))
        os.unlink(test_file)

if __name__ == '__main__':
    unittest.main()
