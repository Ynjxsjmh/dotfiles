#!/bin/zsh

# The display manager sources ~/.profile so we should never hit this.
# Keep it just in case.
if [[ "${_SOURCED_PROFILE}" != 'yes' ]]; then
  emulate sh -c ". ${HOME}/.profile"
fi

function is-os-linux() { [[ "${OS_TYPE}" == "Linux" ]]; }
function is-os-darwin() { [[ "${OS_TYPE}" == "Darwin" ]]; }
function is-os-macos() { [[ "${OS_TYPE}" == "Darwin" ]]; }
function is-os-freebsd() { [[ "${OS_TYPE}" == "FreeBSD" ]]; }

function is-distro-arch() { [[ "${DISTRO_TYPE}" == 'arch' ]]; }
function is-distro-debian() { [[ "${DISTRO_TYPE}" == 'debian' ]]; }
