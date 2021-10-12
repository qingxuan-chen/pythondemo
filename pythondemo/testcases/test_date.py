import pytest
import yaml


class TestDate:

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open('./date.yaml')))
    def test_date(self, a, b):
        print(a+b)
