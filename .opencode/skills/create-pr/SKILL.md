---
name: create-pr
description: "Push local main to remote and create an administrative PR for changes already merged"
---

# Create PR

Load [[software-craft/git-conventions#key-takeaways]] before starting. 

1. Push local main to remote: `git push origin main`.
2. Create a pull request with the squashed commit format from [[software-craft/git-conventions#content]], including @id traceability for all acceptance criteria.
3. IF the PR is approved → write results to output artifacts, advance to next state.
4. IF changes are requested → address feedback on a fix branch per [[software-craft/git-conventions#concepts]], then re-push and update the PR.
5. IF the PR is cancelled → write results to output artifacts, route to post-mortem.
6. Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed.