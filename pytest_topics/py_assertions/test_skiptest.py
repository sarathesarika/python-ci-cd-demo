import pytest
import sys
import reason

const =9/5
def cent_to_fah(cent=0):
    fah=(cent*const)+32
    return fah
@pytest.mark.skip(reason="as usual ")
def test_case01():
    assert type(const)==float

@pytest.mark.skipif(sys.version_info < (3,6),reason="requires Python 3.6 or higher")
def test_case02():
    assert cent_to_fah()==32