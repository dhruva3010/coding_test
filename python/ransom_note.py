def can_construct(ransom_note, magazine):
    for char in ransom_note:
        if char in magazine:
            # This line removes one occurrence of the character 'char' from the 'magazine' string.
            # The replace() method is used with a count of 1 to ensure only one instance is replaced.
            # This simulates "using up" a letter from the magazine to construct the ransom note.
            magazine = magazine.replace(char, '', 1)
        else:
            return False
    return True

print(can_construct("a", "b"))
print(can_construct("aa", "ab"))
print(can_construct("aa", "aab"))
