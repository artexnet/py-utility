__author__ = 'arthur'

import re
import string


REGEX_EMAIL = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
REGEX_URL = '^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
REGEX_HTML_TAG = r"""</?\w+((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)/?>"""
REGEX_IPv4 = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
REGEX_MAC_ADDRESS = r'^(?i)([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$'
REGEX_POSITIVE_INT = '^\d+$'
REGEX_NEGATIVE_INT = '^-\d+$'
REGEX_INTEGER = '^-{0,1}\d+$'
REGEX_POSITIVE_NUM = '^\d*\.{0,1}\d+$'
REGEX_NEGATIVE_NUM = '^-\d*\.{0,1}\d+$'
REGEX_NUMBER = '^-{0,1}\d*\.{0,1}\d+$'
REGEX_12HOUR_TIME = r'^(1[012]|[1-9]):[0-5][0-9](\s)?(?i)(am|pm)$'
REGEX_24HOUR_TIME = r'^([0-1]{1}[0-9]{1}|20|21|22|23):[0-5]{1}[0-9]{1}$'
REGEX_DATE_PATTERN_V1 = '^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(19|20)\d{2}$'


# checks if the input string is empty
def is_empty(_str):
    return _str is not None and _str.strip()


# checks if the input string is an email
def is_email(_str):
    return _str is not None and bool(re.match(REGEX_EMAIL, _str)) is True


# checks if the input string is a URL
def is_url(_str):
    return _str is not None and bool(re.match(REGEX_URL, _str)) is True


# checks if the input string is an HTML tag
def is_html_tag(_str):
    return _str is not None and bool(re.match(REGEX_HTML_TAG, _str)) is True


# checks if the input string is an IPv4 IP address
def is_ipv4_address(_str):
    return _str is not None and bool(re.match(REGEX_IPv4, _str)) is True


# checks if the input string is a MAC address
def is_mac_address(_str):
    return _str is not None and bool(re.match(REGEX_MAC_ADDRESS, _str)) is True


# checks if the input string is a positive integer
def is_positive_int(_str):
    return _str is not None and bool(re.match(REGEX_POSITIVE_INT, _str)) is True


# checks if the input string is a negative integer
def is_negative_int(_str):
    return _str is not None and bool(re.match(REGEX_NEGATIVE_INT, _str)) is True


# checks if the input string is an integer number
def is_integer(_str):
    return _str is not None and bool(re.match(REGEX_INTEGER, _str)) is True


# checks if the input string is a positive number
def is_positive_num(_str):
    return _str is not None and bool(re.match(REGEX_POSITIVE_NUM, _str)) is True


# checks if the input string is a negative number
def is_negative_num(_str):
    return _str is not None and bool(re.match(REGEX_NEGATIVE_NUM, _str)) is True


# checks if the input string is a number
def is_number(_str):
    return _str is not None and bool(re.match(REGEX_NUMBER, _str)) is True


# checks if the input string comprised of digit
def is_digit(_str):
    return _str is not None and _str.isdigit()


# checks if the input string is a 12-hour formatted time
def is_12h_time(_str):
    return _str is not None and bool(re.match(REGEX_12HOUR_TIME, _str)) is True


# checks if the input string is a 24-hour formatted time
def is_24h_time(_str):
    return _str is not None and bool(re.match(REGEX_24HOUR_TIME, _str)) is True


# checks if the input string is a date
def is_date(_str):
    return _str is not None and bool(re.match(REGEX_DATE_PATTERN_V1, _str)) is True


# checks if the input string is palindrome
def is_palindrome(_str):
    s = ''.join(char for char in _str if char.isalpha()).upper()
    return s == s[::-1]


# returns a string comprised of ascii letters
def get_ascii_letters():
    return string.ascii_letters


# returns a string comprised of digits
def get_digits():
    return string.digits


# returns a string comprised of hex digits
def get_hexdigits():
    return string.hexdigits


# returns a string comprised of whitespaces
def get_whitespaces():
    return string.whitespace


# makes a first letter of input string capital
def capitalize(_str):
    return str(_str).capitalize()


# makes a first letter of input string capital and makes the rest lowercase
def capitalize_as_title(_str):
    return str(_str).title()


# generates a random UUID
def get_random_uuid():
    from uuid import uuid4
    return str(uuid4())