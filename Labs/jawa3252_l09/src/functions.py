"""
-------------------------------------------------------
Functions, Lab 8
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-10"
-------------------------------------------------------
"""


# 1
def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """

    if "OH" in chemical[-2:]:
        hydroxide = True

    else:
        hydroxide = False

    return hydroxide


# 3
def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """

    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]

    return pc, pi, pq


# 7
def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """

    count = 0

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in range(0, len(s)):
        for x in range(0, len(vowels)):
            if vowels[x] == s[i]:
                count += 1

    return count


# 10
def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """

    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    for i in range(0, len(txt)):
        if txt[i].isdigit():
            dgts += 1

        elif txt[i].isspace():
            whtspc += 1

        elif txt[i].isupper():
            uppr += 1

        elif txt[i].islower():
            lowr += 1

    return uppr, lowr, dgts, whtspc


# 14
def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """

    d = 0

    if len(s1) != len(s2):
        d = -1

    else:
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                d += 1

    return d
