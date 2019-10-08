import pytest
@pytest.yield_fixture()
def setup():
    print("open URL to login")
    yield
    print("closing browser after login")
def test_loginByemail(setup):
    print("hello")
def test_loginByfacebook(setup):
    print("hI")
