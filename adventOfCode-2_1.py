file = open('input.txt', "r")
lines = file.readlines()
file.close()

compteur = 0

for line in lines: 
    numbers,letter,password = line.split(' ')
    min,max = numbers.split('-')
    letter = letter.replace(':','')
    if int(min) <= password.count(letter) <= int(max) :
        compteur += 1

print(compteur)