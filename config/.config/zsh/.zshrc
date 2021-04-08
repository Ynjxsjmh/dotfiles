# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# History
HISTFILE=${ZDOTDIR:-${HOME}}/.histfile
# The maximum number of events stored in the internal history list.
HISTSIZE=10000
# The maximum number of history events to save in the history file.
SAVEHIST=50000
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '${ZDOTDIR}/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall


# Load Antigen
source ~/.antigen/antigen.zsh

# Load Antigen configurations
antigen init ${ZDOTDIR}/.antigenrc

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ${ZDOTDIR}/.p10k.zsh ]] || source ${ZDOTDIR}/.p10k.zsh

source "${ZDOTDIR}/aliases.zsh"
source "${ZDOTDIR}/distro-debian.zsh"
source "${ZDOTDIR}/distro-arch.zsh"


eval "$(zoxide init zsh)"
