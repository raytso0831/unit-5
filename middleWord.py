#Ray Tso
#4/23/18
#middleWord.py

words=input('type in some words:').split(' ')
middle=len(words)

if middle%2==0:
    print(words[middle//2])

