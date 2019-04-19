import unittest
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


if __name__ == '__main__':
    unittest.main()
