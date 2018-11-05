#!/usr/bin/env bash
sed -i -e 's/<SEP>/,/g' unique_tracks.txt
sed -i -e 's/<SEP>/,/g' triplets_sample_20p.txt

./sqlite_example.sh 2> /dev/null

./tasks.sh