import pytest
@pytest.yield_fixture()
def setup():
    print("once before ever method")
    yield
    print("once after every method")
def testMethod1(setup):
    print("hello")
def testMethod2(setup):
    print("hI")
