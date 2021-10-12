# coding=utf-8
import unittest

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('这是setupclass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('这是teardownclass')

    def setUp(self) -> None:
        print('这是setup')

    def tearDown(self) -> None:
        print('这是teardown')

    def test_abc(self):
        print('test abc')

    def test_upper(self):
        print('111')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('222')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print('333')
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()