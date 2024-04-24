
### setup.py for TradeLeverCalc

```python
from setuptools import setup, find_packages

setup(
    name='tradelevercalc',
    version='0.1.0',
    author='Nicholas Noochla-or',
    author_email='nnlaor@gmail.com',
    description='A trading calculation library for position sizing and risk management',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/FlintSable/TradeLeverCalc',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
