#!/bin/bash
# Watch all the .scss files under the directories which are on the same level of this script.
node-sass --no-source-map --style compressed -o . .
