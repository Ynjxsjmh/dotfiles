#!/bin/zsh

if [[ "${_SOURCED_PROFILE}" != 'yes' ]]; then
  emulate sh -c "${HOME}/.profile"
fi

export _SOURCED_ZSH_ZPROFILE='yes'


# Load common functions by absolute path to avoid searching every entry in $fpath.
autoload "${ZDOTDIR}/functions/external-command-exists"
