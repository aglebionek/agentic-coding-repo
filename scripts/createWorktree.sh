${0%/*}/checkIfAlreadyInWorktree.sh

# From the main repo root 
BRANCH_NAME=$1
git worktree add "../worktrees/${BRANCH_NAME}" -b "${BRANCH_NAME}" develop
cd "../worktrees/${BRANCH_NAME}"

# copy or symlink anything you might need in the worktree, like .env files or node_modules

cat > .worktree-session <<EOF
path-to-worktree: $(pwd)
branch-name: ${BRANCH_NAME}
model-name: $2
task: $3
started: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
EOF
