"""Install lazy_containers package."""
from setuptools import setup

setup(
    name='lazy_containers',
    version='0.0.1',
    author='Aaron Mangum',
    url='https://github.com/potatochip/lazy-containers',
    packages=['lazy_containers'],
    python_requires='>=3.3',
    setup_requires=["pytest-runner", "flake8", "flake8-docstrings"],
    tests_require=["pytest", "pytest-cov", ]
)
