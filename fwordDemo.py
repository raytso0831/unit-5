#Ray Tso
#4/23/18
#fwordDemo.py

words=input('type in some words:').split(' ')

for item in words:
    if 'f' in item or 'F' in item:
        print(item)

