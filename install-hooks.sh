#!/bin/bash
mkdir -p .git/hooks
ln -sf check-links.sh .git/hooks/pre-push
echo "Pre-push hook installed!"