import os
import re
import sys
import getopt

rootdir = ''
exclude = ['CACHE', 'tests']
count = 0

try:
    options, args = getopt.getopt(sys.argv[1:], 'r:', ['root='])
except getopt.GetoptError:
    print 'moduly.py -r <root_directory>'
    sys.exit(1)

for opt, arg in options:
    if opt in ('-r', '--root'):
        rootdir = arg

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
