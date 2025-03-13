import re
import random
import base64
import string

# Generate a random variable name
def random_var_name():
    return ''.join(random.choices(string.ascii_letters, k=8))

# Obfuscate string literals by encoding them in Base64
def obfuscate_string_literals(code):
    def encode_match(match):
        original = match.group(0)
        encoded = base64.b64encode(original.encode()).decode()
        return f'base64.b64decode("{encoded}").decode()'
    return re.sub(r'"(.*?)"|'(.*?)'', encode_match, code)

# Rename variables in the code
def obfuscate_variable_names(code):
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)
    keywords = set("import def return if else for while break continue class pass".split())
    unique_tokens = set(tokens) - keywords
    obfuscation_map = {token: random_var_name() for token in unique_tokens}
    for orig, obf in obfuscation_map.items():
        code = re.sub(rf'\b{orig}\b', obf, code)
    return code

# Remove comments and extra whitespace
def remove_comments_and_whitespace(code):
    code = re.sub(r'#.*', '', code)  # Remove comments
    code = re.sub(r'\s+', ' ', code)  # Remove extra whitespace
    return code.strip()

# Main function to obfuscate Python code
def obfuscate_code(code):
    code = remove_comments_and_whitespace(code)
    code = obfuscate_string_literals(code)
    code = obfuscate_variable_names(code)
    return code

# Example usage
if __name__ == "__main__":
    sample_code = """
    # This is a test script
    def greet(name):
        message = "Hello, " + name
        print(message)
    greet("Farhan")
    """
    obfuscated = obfuscate_code(sample_code)
    print("Obfuscated Code:\n", obfuscated)
