import pytest
import sys
def testcase_0():
    with pytest.raises(Exception):
        assert (1/0)
@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires Python 3.6")
def testcase_1():
    with pytest.raises(Exception) as e:
        assert (1,2,3)==(1,2,4)
    print(e)

def fun1():
    raise ValueError("IndexError func1 Error")
@pytest.mark.skip(reason="skip reason")
def testcase_2():
    with pytest.raises(Exception) as e:
        fun1()
    print(str(e))
    assert (str(e.value)) == "Exception fun1 raised"