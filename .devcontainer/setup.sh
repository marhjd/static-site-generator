#!/bin/sh

curl -sS https://webi.sh/golang | sh; \
source ~/.config/envman/PATH.env

curl -sS https://webi.sh/bat | sh; \
source ~/.config/envman/PATH.env

curl -sS https://webi.sh/git | sh; \
source ~/.config/envman/PATH.env

go install github.com/bootdotdev/bootdev@latest
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.zshrc
source ~/.bashrc
source ~/.zshrc
bootdev login
