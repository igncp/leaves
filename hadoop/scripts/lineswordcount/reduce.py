import sys

words_in_line = 0
current_words_in_line = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    words_in_line, count = line.split('\t', 1)
    try:
        count = int(count)
        words_in_line = int(words_in_line)
    except ValueError:
        continue

    if current_words_in_line == words_in_line:
        current_count += count
    else:
        if current_words_in_line:
            print '%s\t%s' % (current_words_in_line, current_count)
        current_count = count
        current_words_in_line = words_in_line

if current_words_in_line == words_in_line:
    print '%s\t%s' % (current_words_in_line, current_count)