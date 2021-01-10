from rand import inteiro_aleatorio
from unittest.mock import Mock, patch


def test_inteiro_aleatorio():
    with patch("rand.randint", return_value=6, autospec=True) as m:
        args = (1, 10)
        ret = inteiro_aleatorio(*args)
        assert m.assert_called_once_with(*args) is None
        assert ret == 6
