import pylrc
from pylrc.classes import Lyrics, LyricLine
import os


def load_lrc(fname: str) -> Lyrics:
    with open(fname, 'r', encoding='utf-8') as f:
        lrcstr = ''.join(f.readlines())
        return pylrc.parse(lrcstr)


def get_lst() -> list[str]:
    lst = []
    filelst = os.listdir('.')
    for fname in filelst:
        if fname.endswith('_orig.lrc'):
            if fname[:-9] + '_tran.lrc' in filelst:
                lst.append(fname[:-9])
    return lst

def ms_to_tag(line: LyricLine) -> str:
    return f'{line.minutes:02d}:{line.seconds:02d}.{line.milliseconds:03d}'

def find_match(lyrics: Lyrics, time: str | LyricLine) -> LyricLine | None:
    if isinstance(time, LyricLine):
        time = ms_to_tag(time)
    for i in range(len(lyrics)):
        if ms_to_tag(lyrics[i]) == time and lyrics[i].text != '':
            return lyrics[i]
    return None

def transfer(fname: str) -> None:
    orig = load_lrc(f'{fname}_orig.lrc')
    tran = load_lrc(f'{fname}_tran.lrc')
    mixed = load_lrc(f'{fname}_orig.lrc')

    mixed.clear()

    i = 0
    while i < len(orig):
        try:
            mixed.append(orig[i])
            match = find_match(tran, orig[i])
            if match:
                mixed.append(match)
        except IndexError:
            pass
        i += 1
    result = mixed.toLRC()
    with open(f'{fname}_mixed.lrc', 'w', encoding='utf-8') as f:
        f.write(result)


if __name__ == '__main__':
    lst = get_lst()
    print(f'List: {lst}')
    for i in lst:
        print(f'Transferring {i}...')
        transfer(i)
    print('Finished!')
