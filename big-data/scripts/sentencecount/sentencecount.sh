RELATIVE_DIR=$(dirname "$0")
HELPERS=scripts/helpers
NAME=sentencecount

sh $HELPERS/remove-and-create.sh $NAME
sh $HELPERS/copy-gutenberg-book-to.sh $NAME
python scripts/sentencecount/job.py -c scripts/sentencecount/mrjob.conf hdfs-dir/sentencecount/gutenberg-book.txt -r hadoop > counts