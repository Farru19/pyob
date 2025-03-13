# Python Code Obfuscator

## Description
This is a simple Python script that obfuscates Python code by renaming variables, encoding string literals using Base64, and removing comments and unnecessary whitespace. This makes the code harder to read while maintaining its functionality.

## Features
- Renames variables to random names
- Encodes string literals using Base64
- Removes comments and extra whitespace
- Keeps the code functional while making it harder to read

## Installation
No external dependencies are required except for Python 3.x. Simply clone this repository and run the script.

```bash
git clone https://github.com/yourusername/python-code-obfuscator.git
cd python-code-obfuscator
```

## Usage
To obfuscate a Python script, modify the `sample_code` variable inside `obfuscator.py` with the code you want to obfuscate and run:

```bash
python obfuscator.py
```

### Example
#### Input Code:
```python
# This is a test script
def greet(name):
    message = "Hello, " + name
    print(message)

greet("Farhan")
```
#### Obfuscated Output:
```python
import base64

Hsdjskfj = base64.b64decode("SGVsbG8sIA==").decode() + Afjdkasl
print(Hsdjskfj)
```

## Versioning
### v1.0.0
- Initial release
- Basic variable renaming, string obfuscation, and comment removal

## License
This project is licensed under the MIT License.
