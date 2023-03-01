from unittest.mock import patch

from .factory import factory


@patch('src.mocks.factory.MyClass.notify')
def test_mock_my_class(mock_notify):
    my_class = factory()
    params = {'a':1, 'b':2}
    my_class.notify(params)
    assert mock_notify.assert_called_with(params) is None
