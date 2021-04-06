from mm import mm


def test_1():
    uut = mm(100)
    assert uut.new(2) == 0
    assert uut.new(2) == 2
    uut.free(0)
    assert uut.new(2) == 4
