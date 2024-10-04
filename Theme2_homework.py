word = input("Напишите слово : ")

l = len(word)
m = l//2

if l % 2 == 0:
    letter = word[m-1:m+1]
else:
    letter = word[m]

print(letter)