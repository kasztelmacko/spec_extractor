#!/usr/bin/env bash
set -e

# Configure GitHub auth if token exists
if [ -n "$GITHUB_TOKEN" ]; then
  git config --global user.name "${GITHUB_USER:-github}"
  git config --global user.email "${GITHUB_EMAIL:-github@users.noreply.github.com}"
  git config --global credential.helper store

  cat > /root/.git-credentials <<EOF
https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com
EOF

  chmod 600 /root/.git-credentials
  echo "✓ GitHub auth configured"
fi

exec "$@"
