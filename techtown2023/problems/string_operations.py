
# Your task is to implement these functions using builtins and slicing notation
# Do not use any imports

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_string_operations.py -x -v


def get_string_length(string):
    return len(string)

# HINT: isinstance(x, bytes)
def convert_to_string(something):
    return str(something) if type(something) is not bytes else something.decode("ascii")

def make_uppercase(string):
    return string.upper()

def make_lowercase(string):
    return string.lower()

def take_first_3_characters(string):
    return string[:3]

def take_every_other_character(string):
    return string[::2]

def take_last_8_characters(string):
    return string[-8:]

# HINT: str.split
def count_words(string):
    return len(string.split())

# HINT: str.join
def remove_first_word(string):
    return " ".join(string.split()[1:])

def censor_curse_words(string, list_of_bad_words):
    "this function replaces bad words with '***'"
    list_of_bad_words = [bad.lower() for bad in list_of_bad_words]
    censored = []
    for word in string.split():
        if word.lower() in list_of_bad_words:
            censored.append("***")
        else:
            censored.append(word)
    return " ".join(censored)

# HINT: ord, hex
def convert_to_hexadecimal(string):
    return string.encode("utf-8").hex(sep=" ")

# HINT:
def convert_list_of_unicode_codepoints_to_string(list_of_codepoints):
    return "".join(chr(code) for code in list_of_codepoints)

def convert_list_of_ints_to_bytes(list_of_uint8):
    return bytes(list_of_uint8)

# HINT: str.endswith
def check_if_filename_has_filetype(filename: str, accepted_file_extensions: list) -> bool:
    return any(filename.lower().endswith("." + ext.lower()) for ext in accepted_file_extensions)
