import string

s = '''In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation).
A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures.
Depending on the programming language and precise data type used, a variable declared to be a string may either cause storage in memory to be statically allocated for a predetermined maximum length or employ dynamic allocation to allow it to hold a variable number of elements.
When a string appears literally in source code, it is known as a string literal or an anonymous string.[1]
In formal languages, which are used in mathematical logic and theoretical computer science, a string is a finite sequence of symbols that are chosen from a set called an alphabet.'''
s = s.lower()

alf = list(string.ascii_lowercase)
suma, t = 0, 0
for x in alf:
    suma = s.count(x)
    t = t + s.count(x)
    print(x, "", suma)

print(t)
