# Task
# Given N names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each NAME queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for NAME is not found, print Not found instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# Input Format

# The first line contains an integer, N, denoting the number of entries in the phone book.
# Each of the N subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend's name, and the second value is an 8-digit phone number.

# After the N lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a NAME to look up, and you must continue reading lines until there is no more input.

# Note: Names consist of lowercase English alphabetic letters and are first names only.

phonebook = {k:v for k,v in (input().split() for _ in range(int(input())))}
while True:
    try:
        name = input()
        if name in phonebook:
            print(f'{name}={phonebook.get(name)}')
        else:
            print('Not found')
    except:
        break

