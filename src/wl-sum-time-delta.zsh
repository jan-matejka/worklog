#!/bin/sh

exec awk '{ split($1, a, ":"); h+=a[1]; m+=a[2]; } END { h+=int(m/60); m = m%60; print h ":" m;}'
