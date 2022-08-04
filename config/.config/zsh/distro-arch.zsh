
# Arch Linux specific functionality

if ! is-distro-arch; then
  return
fi

alias S='sudo pacman -S'
alias Syu='sudo pacman -Sy archlinux-keyring && pacman -Syu'
alias Syyu='sudo pacman -Sy archlinux-keyring && pacman -Syyu'

# Querying package databases
#   -Ss string1 string2: Search for packages in the database,
#                        searching both in packages' names and descriptions
#   -Qs string1 string2: Search for already installed packages
#   -Qi package_name:    Search for locally installed packages.
alias Ss='pacman -Ss'
alias Qs='pacman -Qs'
alias Qi='pacman -Qi'

# Removing packages
#   -Rs:  To remove a package and its dependencies which are not
#         required by any other installed package.
#   -Rsu: The above(-Rs) may sometimes refuse to run when removing a
#         group which contains otherwise needed packages.
#   -n:   To prevent the creation of these backup files.
#         Pacman saves important configuration files when removing
#         certain applications and names them with the extension: `.pacsave`.
alias Ru='sudo pacman -Rsu'
alias Rn='sudo pacman -Rsn'

# Yay is a Pacman wrapper with AUR support. It passes options to
# Makepkg and Pacman after resolving packages to install/upgrade.
#   -S, -Si, -Sl, -Ss, -Su, -Sc, -Qu
#          These operations are extended to support both AUR and repo packages.
#   -R     Yay will also remove cached data about devel packages.
alias yS='yay -S'
alias yRu='yay -Rsu'
alias yRn='yay -Rsn'
