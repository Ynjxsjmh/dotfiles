#!/bin/sh
# ~/.profile is read by the display manager on login.

export _SOURCED_PROFILE='yes'

export OS_TYPE
OS_TYPE="$(uname -s)"

export DISTRO_TYPE='unknown'
if [[ -r /etc/debian_version ]]; then
  DISTRO_TYPE='debian'
elif [[ -r /etc/arch-release ]]; then
  DISTRO_TYPE='arch'
fi
