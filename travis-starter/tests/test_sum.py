import sample_lib


def test_sanity():
    if (True != True):
        raise AssertionError('Sanity test failed')

def test_sum():
    if (sample_lib.sumNums(1,2) != 3):
        raise AssertionError('sum(x,y): Expected: {3}')

def test_sum_np():
    if (sample_lib.sumNp(1,2) == 3):
        raise AssertionError('sumNP(x,y) should not equal {3}')