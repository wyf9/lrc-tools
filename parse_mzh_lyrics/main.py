import pyperclip

orig = pyperclip.paste()

trans = orig.split('\n')

n = 0
while True:
    n += 1
    try:
        if n % 2 == 1:
            print(trans[n-1], end=' / ')
        else:
            print(trans[n-1])
    except:
        break