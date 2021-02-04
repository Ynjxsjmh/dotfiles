
# Arch Linux specific functionality

if ! is-distro-arch; then
  return
fi

alias S='sudo pacman -S'
alias Ss='pacman -Ss'
alias Syu='sudo pacman -Syu'
alias Syyu='sudo pacman -Syyu'

# Querying package databases
#   -Ss string1 string2: Search for packages in the database,
#                        searching both in packages' names and descriptions
#   -Qs string1 string2: Search for already installed packages
#   -Qi package_name:    Search for locally installed packages.
alias Ss='pacman -Ss'
alias Qs='pacman -Qs'
alias Qi='pacman -Qi'

alias Rn='pacman -Rsn'
alias Ru='pacman -Rsu'

alias yS='yay -S'
