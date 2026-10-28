# Run file:      pytest pytestDir/test_PyTestValidation.py -v -s
# Run one test:  pytest pytestDir/test_PyTestValidation.py::test_initialCheck -v -s

#Fixtures
import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "fail"


@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondWork instance")
    yield #pause
    print("tear down validation")


@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):
    print("This is first test")
    assert preWork == "fail"


@pytest.mark.skip
def test_SecondCheck(preSetupWork, secondWork):
    print("This is Second test")
