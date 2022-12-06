filecontent = open("input.txt", "r")

inputstring = ''
for line in filecontent:
    inputstring += line
offset = 14
communicationString = inputstring[0:offset]

def stringHasDuplicateCharacters(stringToCheck):

    checkedCharacters = []

    for i in stringToCheck:
        if i not in checkedCharacters:
            checkedCharacters.append(i)
    if len(checkedCharacters) == len(stringToCheck):
        print(checkedCharacters)
        return False
    return True

counter = offset

for c in inputstring:
    print(communicationString[-offset:])
    if not stringHasDuplicateCharacters(communicationString[-offset:]):
        break
    communicationString += c
    counter += 1

print(len(communicationString))
print(counter - offset)

