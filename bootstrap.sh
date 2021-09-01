#!/bin/zsh

# move over .zshrc
cp .zshrc ${HOME}

# install pure theme for zsh
mkdir -p "$HOME/.zsh"
git clone https://github.com/sindresorhus/pure.git "${HOME}/.zsh/pure"
