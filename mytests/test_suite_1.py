import pytest

pytestmark = [pytest.mark.frontend,pytest.mark.slow]

@pytest.mark.smoke
def test_login_valid_user():
    print(".............Hello How are you")
    print("Login with valid user")

@pytest.mark.regression
@pytest.mark.smoke
def test_login_with_password():
    print("Login with valid password")
    assert 1==3,"failed"