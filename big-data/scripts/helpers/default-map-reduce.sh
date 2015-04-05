HELPERS=scripts/helpers
NAME=$1
DATA=$2

sh $HELPERS/remove-and-create.sh $NAME
sh $HELPERS/copy-gutenberg-book-to.sh $NAME
sh $HELPERS/run-hadoop-with-python.sh $NAME $DATA
sh $HELPERS/read-output.sh $NAME