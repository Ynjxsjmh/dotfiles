alias sudo='sudo '

alias pls='sudo sh -c "$(fc -ln -1)"'
# alias tmux="tmux new-session -d -s \>_ 2>/dev/null; tmux new-session -t \>_ \; set-option destroy-unattached"

alias df='df -h'
alias du='du -c -h'

alias mkdir='mkdir -p -v'

alias diff='colordiff'
alias grep='grep --color=auto'
alias ls='ls --color=auto -F'

alias ll='ls -lah'

alias ..='cd ..'
alias ..2="cd ../.."
alias ..3="cd ../../.."
alias ..4="cd ../../../.."
alias ..5="cd ../../../../.."

alias battery='upower -i $(upower -e | grep "BAT") | grep -E "state|to\ full|to\ empty|percentage"'

# unar can detect encoding automatically,
# unzip need extra package to support gbk encoding.
# See https://wiki.archlinux.org/title/Localization/Simplified_Chinese_(简体中文)#zip_压缩包乱码
alias unzip='unar'

unalias gl
alias gl='git log --pretty="%C(cyan)%ad %C(yellow)%h %C(cyan)%d %Creset%s" --date-order --graph --date=iso'
alias gla='git log --pretty="%C(cyan)%ad %C(red)%aN %C(yellow)%h %C(cyan)%d %Creset%s" --date-order --graph --date=iso'

alias tmux='tmux -f $HOME/.config/tmux/.tmux.conf'
