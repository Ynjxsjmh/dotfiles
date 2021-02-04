
# Debian stuff

if ! is-distro-debian; then
  return
fi

alias acs='apt-cache search'
alias acsh='apt-cache show'
alias acp='apt-cache policy'

alias adg="sudo apt-get dist-upgrade"
alias agi="sudo apt-get install --assume-yes"
alias agr="sudo apt-get remove"
alias agu="sudo apt-get upgrade"
alias agu="sudo apt-get update"

alias ati="sudo aptitude install"
alias dbp='dpkg-buildpackage'

# Sort installed Debian-packages by size.
if external-command-exists dpkg-query ; then
  # List installed Debian-packages sorted by size
  alias debs-by-size="dpkg-query -Wf 'x \${Installed-Size} \${Package} \${Status}\n' | sed -ne '/^x  /d' -e '/^x \(.*\) install ok installed$/s//\1/p' | sort -nr"
fi
