from lazy_containers.lazy_list import LazyList as list


def test_extend():
    l = list([1,2,3])
    l.extend([4,5])
    assert l.set == {1,2,3,4,5}


# TODO: need more test coverage
