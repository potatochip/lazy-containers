from lazy_containers.lazy_list import LazyList as list



def test_meta():
    l = list([1,2,3])
    l.extend([4,5])
    assert l.set == 0