import re
import sys

def split_camel_case(data: str) -> str:
    """Splits a camel case string into space-separated words in lowercase."""
    words = re.findall(r'[A-Z]?[a-z]+|\d+', data)
    return " ".join(word.lower() for word in words)

def combine_camel_case(words, identifier_type):
    """Combines words into camel case based on identifier type."""
    words = words.split()

    if identifier_type == "C":
        return "".join(word.capitalize() for word in words)
    elif identifier_type == "V":
        return words[0].lower() + "".join(word.capitalize() for word in words[1:])
    elif identifier_type == "M":
        return words[0].lower() + "".join(word.capitalize() for word in words[1:]) + "()"

def process_line(line):
    operation, identifier_type, data = line.strip().split(";")
    if operation == 'S':
        if identifier_type == 'M':
            data = data[:-2]
        print(split_camel_case(data))
    
    elif operation == "C":
        print(combine_camel_case(data, identifier_type))

if __name__ == "__main__":
    for line in sys.stdin:
        process_line(line)