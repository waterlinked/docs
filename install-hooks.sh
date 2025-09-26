#!/bin/bash
mkdir -p .git/hooks
ln -sf ../../hooks/pre-push .git/hooks/pre-push
echo "Pre-push hook installed!"