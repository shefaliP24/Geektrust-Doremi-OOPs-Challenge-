import unittest
from geektrust import Doremi
from unittest.mock import patch
from io import StringIO

class TestCases(unittest.TestCase):
    
    # def testcase1(self):
    #     with patch('sys.stdout', new = StringIO()) as fake_out:
    #         fp=open(r"sample_input\input1.txt")
    #         Doremi().User_input(fp)
    #         fp.close()
    #         self.assertMultiLineEqual(fake_out.getvalue(),"RENEWAL_REMINDER MUSIC 10-03-2022\nRENEWAL_REMINDER VIDEO 10-05-2022\nRENEWAL_REMINDER PODCAST 10-03-2022\nRENEWAL_AMOUNT 750\n","should print")

    def testcase2(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            fp=open(r"sample_input\input2.txt")
            Doremi().User_input(fp)
            fp.close()
            self.assertMultiLineEqual(fake_out.getvalue(),"INVALID_DATE\n")

    def testcase3(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            fp=open(r"sample_input\input3.txt")
            Doremi().User_input(fp)
            fp.close()
            self.assertMultiLineEqual(fake_out.getvalue(),"SUBSCRIPTIONS_NOT_FOUND\n")

    

    def testcase4(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            fp=open(r"sample_input\input4.txt")
            Doremi().User_input(fp)
            fp.close()
            self.assertMultiLineEqual(fake_out.getvalue(),"ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY\n")

    # def testcase5(self):
    #     with patch('sys.stdout', new = StringIO()) as fake_out:
    #         fp=open(r"sample_input\input5.txt")
    #         Doremi().User_input(fp)
    #         fp.close()
    #         self.assertMultiLineEqual(fake_out.getvalue(),"ADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND\nADD_TOPUP_FAILED SUBSCRIPTIONS_NOT_FOUND\n")
    # def testcase6(self):
    #     with patch('sys.stdout', new = StringIO()) as fake_out:
    #         fp=open(r"sample_input\input6.txt")
    #         Doremi().User_input(fp)
    #         fp.close()
    #         self.assertMultiLineEqual(fake_out.getvalue(),"INVALID_DATE\nADD_SUBSCRIPTION_FAILED INVALID_DATE\nADD_SUBSCRIPTION_FAILED INVALID_DATE\nADD_TOPUP_FAILED INVALID_DATE\nSUBSCRIPTIONS_NOT_FOUND\n")
    def testcase7(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            fp=open(r"sample_input\input7.txt")
            Doremi().User_input(fp)
            fp.close()
            self.assertMultiLineEqual(fake_out.getvalue(),"INVALID_DATE\n")

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestCases())