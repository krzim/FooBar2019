"""
Braille Translation
===================

Because Commander Lambda is an equal-opportunity despot, she has several visually-impaired minions. But she never
bothered to follow intergalactic standards for workplace accommodations, so those minions have a hard time navigating
her space station. You figure printing out Braille signs will help them, and - since you'll be promoting efficiency at
the same time - increase your chances of a promotion.

Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3
grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station
to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and ""read"" the text
with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word ""code"", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, ""code"" becomes the output string
""100100101010100110100010"".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the
bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle
capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for
spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("code")
Output:
    100100101010100110100010

Input:
solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    00000101111011001010001000000011111010100101010010010010100000000011000011101010101001011110111000000011010010101010
    11010000000101101010011011001111000111000000001010101110011000101110100000000111101100101000100000001110001000001010
    11101111000000100110101010110110

-- Java cases --
Input:
Solution.solution("code")
Output:
    100100101010100110100010

Input:
Solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
Solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    00000101111011001010001000000011111010100101010010010010100000000011000011101010101001011110111000000011010010101010
    11010000000101101010011011001111000111000000001010101110011000101110100000000111101100101000100000001110001000001010
    11101111000000100110101010110110
"""


ascii2braille = {" ": "000000", "a": "100000", "b": "110000", "c": "100100", "d": "100110", "e": "100010",
                 "f": "110100", "g": "110110", "h": "110010", "i": "010100", "j": "010110", "k": "101000",
                 "l": "111000", "m": "101100", "n": "101110", "o": "101010", "p": "111100", "q": "111110",
                 "r": "111010", "s": "011100", "t": "011110", "u": "101001", "v": "111001", "w": "010111",
                 "x": "101101", "y": "101111", "z": "101011", "capital": "000001"}


def solution(plaintext):
    return ''.join((ascii2braille[c] if c.islower() or c == ' ' else ascii2braille["capital"] + ascii2braille[c.lower()]
                    for c in plaintext))


if __name__ == "__main__":
    assert solution("code") == "100100101010100110100010"
    assert solution("Braille") == "000001110000111010100000010100111000111000100010"
    assert solution("The quick brown fox jumps over the lazy dog") == "0000010111101100101000100000001111101010010101" \
                                                                      "0010010010100000000011000011101010101001011110" \
                                                                      "1110000000110100101010101101000000010110101001" \
                                                                      "1011001111000111000000001010101110011000101110" \
                                                                      "1000000001111011001010001000000011100010000010" \
                                                                      "1011101111000000100110101010110110"