import pyperclip
from time import sleep

last = None

def main():
    while True:
        now = pyperclip.paste()
        if now != last:
            parts = now.split('\n')
            try:
                parts.remove('')
            except:
                pass
            print(' / '.join(parts))
            last = now
        sleep(0.5)

try:
    main()
except KeyboardInterrupt:
    pass