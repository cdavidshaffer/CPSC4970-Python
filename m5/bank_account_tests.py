import unittest
from io import StringIO

from m5.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):
    def test_write_to(self):
        s = StringIO()
        ba = BankAccount(100, "Fred")
        ba.deposit(500)
        ba.write_to(s)
        self.assertEqual("BankAccount|100|Fred|500\n", s.getvalue())


if __name__ == '__main__':
    unittest.main()
