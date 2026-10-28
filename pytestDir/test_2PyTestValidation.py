# Run file:      pytest pytestDir/test_2PyTestValidation.py -v -s
# Run one test:  pytest pytestDir/test_2PyTestValidation.py::test_thirdCheck -v -s

#Fixtures
import pytest


def test_thirdCheck(preSetupWork):
    print("This is Third test")
