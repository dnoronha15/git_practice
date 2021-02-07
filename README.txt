Hello Git and GitHub


If you want to commit on top of the current HEAD with the exact state at a different commit, undoing all the intermediate commits, then you can use reset to create the correct state of the index to make the commit.

# Reset the index and working tree to the desired tree
# Ensure you have no uncommitted changes that you want to keep
git reset --hard 56e05fced

# Move the branch pointer back to the previous HEAD
git reset --soft HEAD@{1}

git commit -m "Revert to 56e05fced"





ADDING THIS IN TO TEST PUSH TO REMOTE