#!/usr/bin/env bash

HELPERS=$(dirname "$0")
NAME=$1
DATA=$2

sh "$HELPERS"/_remove-and-create.sh "$NAME"
sh "$HELPERS"/_copy-gutenberg-book-to.sh "$NAME"
sh "$HELPERS"/_run-hadoop-with-python.sh "$NAME" "$DATA"
sh "$HELPERS"/_read-output.sh "$NAME"