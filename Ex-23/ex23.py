# Exercise 23: String, Bytes and Character Encoding

import sys
script, input_encoding, error = sys.argv

# Defining a main function to read every line of the language_file(the inputted file.)
def main(language_file, encoding, errors):
    line = language_file.readline()

# To check that the line is present in the file. If so, then print_line function will be called and also it will return language file to the main function again.
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# Definition of print_line function

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)  # encoding the language.
    cooked_string = raw_bytes.decode(encoding, errors=errors) # Decoding the language.

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding= "utf-8") 

main(languages, input_encoding, error)