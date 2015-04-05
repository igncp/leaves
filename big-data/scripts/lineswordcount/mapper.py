import sys

for line in sys.stdin:
    words = line.split()
    words_count = len(words)
    print '%s\t%s' % (words_count, 1)
