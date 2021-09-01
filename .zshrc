### kill history
export HISTFILE=/dev/null

### ls colors
export CLICOLOR=1

### pure theme
fpath+=$HOME/.zsh/pure
autoload -U promptinit; promptinit
prompt pure
