#!/bin/sh
# Publish skins/breeze and plugins/tw_folders to their Composer mirrors.
# Usage: ./split.sh [tag]   e.g. ./split.sh v1.0.1 after tagging main
set -e
push() { # prefix repo
  sha=$(git subtree split --prefix="$1")
  git push "https://github.com/$2.git" "$sha:refs/heads/main" --force
  [ -z "$TAG" ] || git push "https://github.com/$2.git" "$sha:refs/tags/$TAG" --force
}
TAG=$1
push skins/breeze qdpops/breeze
push plugins/tw_folders qdpops/tw-folders
