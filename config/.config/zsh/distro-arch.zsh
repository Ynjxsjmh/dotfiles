
# Arch Linux specific functionality

if ! is-distro-arch; then
  return
fi

alias S='sudo pacman -S'
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

# To remove a package and its dependencies which are not required by
# any other installed package:
# `pacman -Rs package_name`

# The above(-Rs) may sometimes refuse to run when removing a
# group which contains otherwise needed packages. In this case try:
alias Ru='pacman -Rsu'
# Pacman saves important configuration files when removing certain
# applications and names them with the extension: `.pacsave`.
# To prevent the creation of these backup files use the `-n` option:
alias Rn='pacman -Rsn'

alias yS='yay -S'
