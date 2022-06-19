file = open('input.txt', "r")
lines = file.readlines()
file.close()

compteur = 0

for line in lines: 
    numbers,letter,password = line.split(' ')
    first,second = numbers.split('-')
    letter = letter.replace(':','')
    if int(first) + 1 < len(password) and int(second) + 1 < len(password):
        bool1 = (password[int(first)+1] == letter)
        bool2 = (password[int(second)+1] == letter)
        if (bool1 and not bool2) or (not bool2 and bool1):
            compteur += 1

print(compteur)