from __future__ import print_function

import os

root = 'r:/test/'
out_path = 'r:/output.txt'


def prasa(r, fp):
    r = os.path.abspath(r)
    items = os.listdir(r)
    files = [i for i in items if os.path.isfile(os.path.join(r, i))]

    if len(files) == 1:
        print(r, files)
        fp.write(r + '\n')

    for item in items:
        root1 = os.path.join(r, item)

        if os.path.isdir(root1):
            prasa(root1, fp)

with open(out_path, 'w') as fp:
    prasa(root, fp)