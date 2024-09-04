Here's a step-by-step guide to creating a simple Python library for calculating the factorial of a number, including setting up the project structure, writing the code, and adding unit tests.

### **Step 1: Set Up the Project Structure**

Create the following directory structure for your library:

```
factorial_lib/
│
├── factorial_lib/
│   ├── __init__.py
│   └── factorial.py
│
├── tests/
│   ├── test_factorial.py
│
├── setup.py
└── README.md
```

### **Step 2: Write the Factorial Code**

Create the `factorial.py` file inside the `factorial_lib/` directory with the following code:

```python
# factorial_lib/factorial.py

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer

    Returns:
    int: Factorial of n

    Raises:
    ValueError: If n is a negative integer
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
```

### **Step 3: Create Unit Tests**

Create the `test_factorial.py` file inside the `tests/` directory to test the factorial function:

```python
# tests/test_factorial.py

import unittest
from factorial_lib.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
```

### **Step 4: Create `setup.py`**

The `setup.py` file is used to package and distribute your library. Here’s an example:

```python
# setup.py

from setuptools import setup, find_packages

setup(
    name='factorial_lib',
    version='0.1.0',
    packages=find_packages(),
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple library to calculate the factorial of a number',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/factorial_lib',  # Update with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
```

### **Step 5: Add a README File**

Create a `README.md` file to describe your project:

```markdown
# Factorial Library

A simple Python library to calculate the factorial of a non-negative integer.

## Installation

```bash
pip install factorial_lib
```

## Usage

```python
from factorial_lib.factorial import factorial

print(factorial(5))  # Output: 120
```

## License

This project is licensed under the MIT License.
```

### **Step 6: Run Unit Tests**

Run the tests to ensure everything works correctly:

```bash
python -m unittest discover -s tests
```

### **Step 7: Build and Distribute the Library**

If everything works correctly, you can package your library and distribute it:

```bash
# Install required tools
pip install setuptools wheel twine

# Build the distribution files
python setup.py sdist bdist_wheel

# Upload to PyPI (optional)
twine upload dist/*
```

### **Usage Example**

Once your library is installed, you can use it in a Python script:

```python
from factorial_lib.factorial import factorial

print(factorial(5))  # Output: 120
```

This guide should help you create a simple Python library for calculating the factorial of a number, complete with unit tests and setup for distribution.