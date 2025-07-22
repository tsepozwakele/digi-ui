import unittest
from tests.SortTest import SortTest

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SortTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
