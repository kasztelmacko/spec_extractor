#!/usr/bin/env bash
set -e

if [ -z "$GITHUB_TOKEN" ]; then
  echo "No GITHUB_TOKEN set, skipping GitHub auth"
  exit 0
fi

git config --global user.name "${GITHUB_USER:-github}"
git config --global user.email "${GITHUB_EMAIL:-github@users.noreply.github.com}"

git config --global credential.helper store

cat > ~/.git-credentials <<EOF
https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com
EOF

chmod 600 ~/.git-credentials

echo "✓ GitHub auth configured"
