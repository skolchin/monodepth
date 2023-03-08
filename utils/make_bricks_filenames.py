from pathlib import Path
from itertools import tee, islice

def pairwise(iterable):
    a, b = tee(iterable)
    yield from zip(islice(a, 0, None, 2), islice(b, 1, None, 2))

files = sorted(Path('../bricks').glob('**/*.png'))

mapping = {'L': {}, 'R': {}}

for fn in files:
    for key in mapping.keys():
        if key + '.' in str(fn):
            mapping[key][fn.name[:-5]] = str(fn)

with open('./filenames/bricks_files.txt', 'wt') as fp:
    for key, fn in mapping['L'].items():
        fp.write(f'{fn} {mapping["R"][key]}\n')
