head -n1000 data/gutenberg-book.txt | python scripts/lineswordcount/mapper.py | sort | python scripts/lineswordcount/reduce.py