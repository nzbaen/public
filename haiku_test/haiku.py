# Haiku test
# This test reads the file 'haiku.txt' and examines all the haiku in the file,
# printing out the haiku, and checking that each line contains the correct number of syllables.
# Note: you can modify the 'haiku.txt' file adding your test cases
import re

haiku_file = 'haiku.txt'

class haikuCheck:
    def __init__(self): 
        pass 

    def clean_haiku(self, haiku):
        lines = haiku.split("/")
        lines = [line.lower()
                .replace("[^a-z]", "")
                .strip() for line in lines]
        return lines

    def syllable_count(self, word):
        words = word.split(" ")
        count = 0
        for word in words:
            matches = re.findall("[aeiouy]+", word)
            count += len(matches)
        return count

    def validate_haiku(self, haiku):
        lines = self.clean_haiku(haiku)
        if len(lines) != 3:
            return false
        counts = [self.syllable_count(line) for line in lines]
        print_string = ','.join([str(i) for i in counts])
        if counts != [5, 7, 5]:
            add = ("No")
            print(print_string + "," + add)
            return False
        else:
            add = ("Yes")
            print(print_string + "," + add)
            return True

# Driver Code 
if __name__ == '__main__': 

    h = haikuCheck()

    with open(haiku_file) as fp:
        for line in fp:
            print(line.rstrip('\n'))
            h.validate_haiku(line)

