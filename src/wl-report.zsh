#! /usr/bin/env sh

awk '/^- / { for(i=5;i<=NF;i++) printf $i" "; print "" }' $1 | sort | uniq
