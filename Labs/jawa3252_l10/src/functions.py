"""
-------------------------------------------------------
Functions, Lab 10
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""


def customer_first(fh):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    # Read all lines and split into records
    lines = fh.readlines()
    records = [line.strip().split(",") for line in lines]
    result = min(records, key=lambda x: x[4])

    return result


def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    fh.seek(0)
    lines = fh.readlines()
    numbers = [int(line.strip()) for line in lines]
    largest = max(numbers)
    largest_str = str(largest)
    fh.write(f"\n{largest_str}")
    return largest


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """

    lines = fh.readlines()
    words = [line.strip() for line in lines]
    count = 0
    for i in range(0, len(words), 1):
        if(word == words[i]):
            count += 1

    return count


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with the longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    longest_word = ""
    max_length = 0

    for line in fh:
        words = line.strip().split()
        for word in words:

            if len(word) > max_length:
                longest_word = word
                max_length = len(word)
            elif len(word) == max_length:
                longest_word = word

    return longest_word


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    content = fh_1.read()
    fh_2.write(content)

    return None
