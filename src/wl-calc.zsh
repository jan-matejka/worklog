#! /usr/bin/env zsh

SELF="${0##*/}"

exec awk '
  /^-/ {
    split($2,a,":");
    split($4,b,":");

    min1 = (a[1] * 60) + a[2];
    min2 = (b[1] * 60) + b[2];
    diff = (min2 - min1);
    sum += diff;
  }

  BEGIN { sum=0; }
  END {
    fmt = int(sum/60);
    minute = (sum % 60);
    if (minute != 0) {
      fmt = fmt ":" minute;
    }
    print fmt;
  }
' $1
