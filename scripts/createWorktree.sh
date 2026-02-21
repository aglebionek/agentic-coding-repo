${0%/*}/checkIfAlreadyInWorktree.sh

# From the main repo root (/home/aglebionek/work/instago/app)
BRANCH_NAME=$1
git worktree add "../worktrees/${BRANCH_NAME}" -b "${BRANCH_NAME}" develop
cd "../worktrees/${BRANCH_NAME}"

cp /home/aglebionek/work/instago/app/server/.env server/.env
cp /home/aglebionek/work/instago/app/client/.env client/.env
ln -s /home/aglebionek/work/instago/app/server/db server
ln -s /home/aglebionek/work/instago/app/client/node_modules client/node_modules
ln -s /home/aglebionek/work/instago/app/server/node_modules server/node_modules
ln -s /home/aglebionek/work/instago/app/.aglebionek .aglebionek

cat > .worktree-session <<EOF
path-to-worktree: ../worktrees/${BRANCH_NAME}
branch-name: ${BRANCH_NAME}
model-name: $2
task: $3
started: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
EOF