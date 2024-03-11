import unittest
from task import conv_num, my_datetime, conv_endian


class ConvNumTest(unittest.TestCase):
    def test1(self):
        """Tests if empty string returns None"""
        num_str = ""
        self.assertEqual(conv_num(num_str), None)

    def test2(self):
        """Tests lowercase hex number"""
        num_str = "0x15ac3f"
        self.assertEqual(conv_num(num_str), int(num_str, 16))

    def test3(self):
        """Tests uppercase hex number"""
        num_str = "0x15AC3F"
        self.assertEqual(conv_num(num_str), int(num_str, 16))

    def test4(self):
        """Tests hex number with both lowercase and uppercase"""
        num_str = "0x15Ac3F"
        self.assertEqual(conv_num(num_str), int(num_str, 16))

    def test5(self):
        """Tests hex number with uppercase prefix"""
        num_str = "0X15Ac3F"
        self.assertEqual(conv_num(num_str), int(num_str, 16))

    def test6(self):
        """Tests if hex number with no prefix returns None"""
        num_str = "15Ac3F"
        self.assertEqual(conv_num(num_str), None)

    def test7(self):
        """Tests negative hex number"""
        num_str = "-0x15Ac3F"
        self.assertEqual(conv_num(num_str), int(num_str, 16))

    def test8(self):
        """Tests if hex number with decimal returns None"""
        num_str = "0x15A.c3F"
        self.assertEqual(conv_num(num_str), None)

    def test9(self):
        """Tests hex number with uppercase prefix"""
        num_str = "0X15Ac3F"
        self.assertEqual(conv_num(num_str), int(num_str, 16))

    def test10(self):
        """Tests floating-point number"""
        num_str = "14.25"
        self.assertEqual(conv_num(num_str), float(num_str))

    def test11(self):
        """Tests floating-point number with decimal at start"""
        num_str = ".1425"
        self.assertEqual(conv_num(num_str), float(num_str))

    def test12(self):
        """Tests floating-point number with decimal at end"""
        num_str = "1425."
        self.assertEqual(conv_num(num_str), float(num_str))

    def test13(self):
        """Tests negative floating-point number"""
        num_str = "-14.25"
        self.assertEqual(conv_num(num_str), float(num_str))

    def test14(self):
        """Tests negative floating-point number with decimal at start"""
        num_str = "-.1425"
        self.assertEqual(conv_num(num_str), float(num_str))

    def test15(self):
        """Tests negative floating-point number with decimal at end"""
        num_str = "-1425."
        self.assertEqual(conv_num(num_str), float(num_str))

    def test16(self):
        """Tests if number with multiple decimal points returns None"""
        num_str = "1.42.5"
        self.assertEqual(conv_num(num_str), None)

    def test17(self):
        """Tests 0.0"""
        num_str = "0.0"
        self.assertEqual(conv_num(num_str), float(num_str))

    def test18(self):
        """Tests integer number"""
        num_str = "5478"
        self.assertEqual(conv_num(num_str), int(num_str))

    def test19(self):
        """Tests negative integer number"""
        num_str = "-5478"
        self.assertEqual(conv_num(num_str), int(num_str))

    def test20(self):
        """Tests 0"""
        num_str = "0"
        self.assertEqual(conv_num(num_str), int(num_str))

    def test21(self):
        """Tests if an integer non-string returns None"""
        num_str = 5478
        self.assertEqual(conv_num(num_str), None)

    def test22(self):
        """Tests if a floating-point non-string returns None"""
        num_str = 14.25
        self.assertEqual(conv_num(num_str), None)

    def test23(self):
        """Tests if a hex number non-string returns None"""
        num_str = 0x15Ac3F
        self.assertEqual(conv_num(num_str), None)

    def test24(self):
        """Tests if a letter string returns None"""
        num_str = "cats"
        self.assertEqual(conv_num(num_str), None)

    def test25(self):
        """Tests if None returns None"""
        num_str = None
        self.assertEqual(conv_num(num_str), None)

    def test26(self):
        """Tests if a single hex prefix returns None"""
        num_str = "0x"
        self.assertEqual(conv_num(num_str), None)

    def test27(self):
        """Tests if a single decimal point returns None"""
        num_str = "."
        self.assertEqual(conv_num(num_str), None)

    def test28(self):
        """Tests if a single negative sign returns None"""
        num_str = "-"
        self.assertEqual(conv_num(num_str), None)

    def test29(self):
        """Tests if a single space returns None"""
        num_str = " "
        self.assertEqual(conv_num(num_str), None)

    def test30(self):
        """Tests if a space inside a number returns None"""
        num_str = "41 23"
        self.assertEqual(conv_num(num_str), None)


class MyDatetimeTest(unittest.TestCase):
    def test1(self):
        """Tests original date"""
        num_sec = 0
        self.assertEqual(my_datetime(num_sec), "01-01-1970")

    def test2(self):
        """Tests 1 second"""
        num_sec = 1
        self.assertEqual(my_datetime(num_sec), "01-01-1970")

    def test3(self):
        """Tests 1 day"""
        num_sec = 86400
        self.assertEqual(my_datetime(num_sec), "01-02-1970")

    def test4(self):
        """Tests 1 year"""
        num_sec = 31536000
        self.assertEqual(my_datetime(num_sec), "01-01-1971")

    def test5(self):
        """Tests 5 years (includes one leap year)"""
        num_sec = 157766400
        self.assertEqual(my_datetime(num_sec), "01-01-1975")

    def test6(self):
        """Tests 123456789 seconds"""
        num_sec = 123456789
        self.assertEqual(my_datetime(num_sec), "11-29-1973")

    def test7(self):
        """Tests hundreds of years"""
        num_sec = 201653971200
        self.assertEqual(my_datetime(num_sec), "02-29-8360")


class ConvEndianTest(unittest.TestCase):
    def test0(self):
        """Test with zero"""
        self.assertEqual(conv_endian(0, 'big'), '00')
        self.assertEqual(conv_endian(0, 'little'), '00')
    def test1(self):
        """test from assignment desc"""
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test2(self):
        """test from assignment desc"""
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test3(self):
        """test from assignment desc"""
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test4(self):
        """test from assignment desc"""
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')
        self.assertEqual(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test5(self):
        """test from assignment desc"""
        self.assertIsNone(conv_endian(num=-954786, endian='small'))

    def test6(self):
        """Large Positive Number"""
        self.assertEqual(conv_endian(4294967295, 'big'), 'FF FF FF FF')
        self.assertEqual(conv_endian(4294967295, 'little'), 'FF FF FF FF')

    def test7(self):
        """little endian reversal test"""
        self.assertEqual(conv_endian(66047, 'little'), 'FF 01 01')

if __name__ == '__main__':
    unittest.main()
