# coding=utf-8
# 被测试方法
import unittest


class Search:

    def search_fun(self):
        print('search')
        return True


class TestSaerch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('这是setupclass 类级别')
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print('这是teardownclass 类级别')

    def setUp(self) -> None:
        print('这是setup 方法级别')

    def tearDown(self) -> None:
        print('这是teardown 方法级别')

    def test_search1(self):
        print('testsearch1')
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print('testsearch2')
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print('testsearch3')
        # search = Search()
        assert True == self.search.search_fun()


class TestSaerch1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('这是setupclass1 类级别')
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print('这是teardownclass1 类级别')

    def setUp(self) -> None:
        print('这是setup1 方法级别')

    def tearDown(self) -> None:
        print('这是teardown1 方法级别')

    def test_search1(self):
        print('testsearch1')
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print('testsearch2')
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print('testsearch3')
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print('判断相等')
        self.assertEqual(1, 2, '判断1 == 2')

    def test_notequal(self):
        print('判断不相等')
        self.assertNotEqual(1, 2, '判断1 != 2')


if __name__ == '__main__':
    # unittest.main()
    #创建一个测试套件
    # suite = unittest.TestSuite()
    # test_cases = [TestSaerch1("test_equal"), TestSaerch1("test_notequal")]
    # suite.addTests(test_cases)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    #执行某个测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSaerch1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSaerch)
    suite = unittest.TestSuite([suite2, suite1])
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)