# Lazy Containers

Container data-types that automatically use the most efficent data-type.
For the lazy / ignorant developer.

## Setup

```shell
$ pip install lazy-containers
...
```

## Usage

```python
from lazy_containers.lazy_list import LazyList as list

l = list(seq, optimize_memory=True)
```
