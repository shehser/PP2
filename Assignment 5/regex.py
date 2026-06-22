import re

# 1
def match_a_zero_or_more_b(text):
    pattern = r'^ab*$'
    return bool(re.match(pattern, text))


# 2
def match_a_two_to_three_b(text):
    pattern = r'^ab{2,3}$'
    return bool(re.match(pattern, text))


# 3
def find_lowercase_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)


# 4
def find_upper_then_lower(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)


# 5
def match_a_anything_b(text):
    pattern = r'^a.*b$'
    return bool(re.match(pattern, text))


# 6
def replace_chars_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)


# 7
def snake_to_camel(text):
    pattern = r'_(.)'
    return re.sub(pattern, lambda match: match.group(1).upper(), text)


# 8
def split_at_uppercase(text):
    pattern = r'(?=[A-Z])'
    return re.split(pattern, text)


# 9
def insert_spaces_capitals(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, ' ', text)


# 10
def camel_to_snake(text):
    str1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', str1).lower()


if __name__ == "__main__":
    print(match_a_zero_or_more_b('ab'))
    print(match_a_two_to_three_b('abb'))
    print(find_lowercase_underscore('hello_world test_case'))
    print(find_upper_then_lower('Python RegEx'))
    print(match_a_anything_b('axxxb'))
    print(replace_chars_with_colon('Hello, world. Python'))
    print(snake_to_camel('this_is_snake_case'))
    print(split_at_uppercase('SplitAtUppercaseLetters'))
    print(insert_spaces_capitals('InsertSpacesBetweenWords'))
    print(camel_to_snake('camelCaseToSnakeCase'))
