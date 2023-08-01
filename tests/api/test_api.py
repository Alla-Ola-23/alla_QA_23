import pytest


@pytest.mark.change
#перевірка можлівості відалення
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == 'Alla'


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Kyrylova'

  





