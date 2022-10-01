#!/bin/sh
#
# Reads daily worklog files from stdin and sums their time spent

find ${1:?} -type f | \
  xargs -n1 wl-calc |
  awk '
  {
    split($1, a, ":");
    h+=a[1];
    m+=a[2];
  }

  END {
    fmt = h + int(m/60);
    m_remainder = (m % 60);

    if (m_remainder != 0) {
      fmt = fmt ":" m_remainder;
    }

    print fmt;
  }
  '
