import os
import re

rootdir = '/home/tanawat/true-teaching/src/true-teaching'
exclude = ['CACHE', 'tests']
count = 0

for root, subFolders, files in os.walk(rootdir):
    for exclusion in exclude:
        if exclusion in subFolders:
            subFolders.remove(exclusion)
    files = [f for f in files if f.endswith('.js')]
    for f in files:
        fullPath = os.path.join(root, f)
        jsFile = open(fullPath, 'r')
        content = jsFile.read()
        match = re.search(r"angular.module\('(.*?)',.*?\)", content)
        if match:
            count += 1
            print str(count) + ': ' + match.group(1)
            print match.group(0)
