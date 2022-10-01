#! /usr/bin/env zsh

SELF="${0##*/}"
. wl_prelude

declare -a pargs
declare -A paargs
zparseopts -K -D -a pargs -Apaargs x
(( ${pargs[(I)-x]} )) && {
  set -x
  export WL_XTRACE=true
}

xdgenv-exec WL worklog -- wl_dispatch $SELF "$@"
