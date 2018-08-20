import sample_lib


def test_sanity():
    if (True != True):
        raise AssertionError('Sanity test failed')

def test_sum():
    if (sample_lib.sum(1,2) != 3):
        raise AssertionError('sum(x,y): Expected: {3}')
