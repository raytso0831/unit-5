#Ray Tso
#4/26/18
#vowelword.py

words=input('Enter some words:').split(' ')

for w in words:
    if w[0] in 'AEIOUaeiou':
        print(w)