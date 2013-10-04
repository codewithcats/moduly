import os

rootdir = '/home/tanawat/true-teaching/src/true-teaching'
exclude = ['CACHE', 'tests']
count = 0

for root, subFolders, files in os.walk(rootdir):
    for exclusion in exclude:
        if exclusion in subFolders:
            subFolders.remove(exclusion)
    files = [f for f in files if f.endswith('.js')]
    for f in files:
        count += 1
        print str(count) + ': ' + f
