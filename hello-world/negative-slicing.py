letters = 'abcdefghijklmnopqrstuvwxyz'

backwards = letters[::-1]
print(backwards)

print(letters[25:0:-1])
print(letters[25::-1])
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[25:17:-1])
print(letters[:-9:-1])

# Python slicing idioms
# Getting the last item
print(letters[:-1])
# Getting the first item but also safely checks if the array
# is empty because if there are no items it will return and empty sequence
print(letters[:1])
# Unsafely getting the first item, this will crash if the sequence is empty
print(letters[0])
