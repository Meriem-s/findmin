# Findmin Python Module


## Description

Given an array of elements that provide a less than operator,find the minimum using as few comparisons as possible. The array shall be given such that the first few elements are strictly monotonically decreasing, the remaining elements are strictly monotonically increasing. The less than operator be defined as the operator that works on such vectors where a < b if min(a,b) == a.

## Getting Started

Once the project is cloned from the repository, your project folder should look like this:
```
- findmin
| - findmin
  | - __init__.py
| - tests
  | - __init__.py
| - setup.py
| - CHANGELOG.md
| - LICENCE.md
| - MANIFEST.in
| - README.md
| - dist
  | - findmin-0.0.1.tar.gz

```
### Dependencies

* Python 3

### Installing the package using pip

* Go to `dist` folder 
* Run the following line to install the package:

```
pip install findmin-0.0.1.tar.gz
```


### Usage Example 

Once the package is installed, we can import the package and test it as follows:

```
from findmin import findmin
print(findmin([3,1,0,1,2,3])) 
```

```
OUTPUT
0
```
If the array format is not correct, a `ValueError` error will be raised.

### Executing the Unit Testing

* Inside `test_findmin.py` a series of tests is executed.
Run the following command line to test `findmin` package.

``` 
cd tests
python -m unittest discover
```

## Version History

* 0.0.1:  Initial Release.

    See the CHANGELOG.md file for details

## License

See the LICENSE.md file for details


