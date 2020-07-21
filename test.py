import unittest

import HtmlTestRunner


class t(unittest.TestCase):
    def test_a(self):
        self.assertTrue(True)
    def test_b(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(report_name='report', add_timestamp=False,
                                                           combine_reports=True))
