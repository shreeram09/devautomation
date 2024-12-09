from git import Repo
from pathlib import Path


class GitManager:
    def __init__(self, repo_url, repo_dir):
        self.repo_url = repo_url
        self.repo_dir = Path(repo_dir)
        self.repo = None

    def clone(self):
        """Clone the repository if not already cloned."""
        if not self.repo_dir.exists():
            self.repo = Repo.clone_from(self.repo_url, self.repo_dir)
            print(f"Cloned repository into {self.repo_dir}")
        else:
            self.repo = Repo(self.repo_dir)
            print(f"Repository already exists at {self.repo_dir}")

    def switch_branch(self, branch_name):
        """Switch to the specified branch."""
        self.repo.git.checkout(branch_name)
        print(f"Switched to branch: {branch_name}")

    def pull_branch(self, branch_name):
        """Pull the latest changes from the specified branch."""
        self.repo.remotes.origin.pull(branch_name)
        print(f"Pulled latest changes for branch: {branch_name}")

    def create_branch(self, branch_name):
        """Create and switch to a new branch."""
        self.repo.git.checkout("-b", branch_name)
        print(f"Created and switched to branch: {branch_name}")

    def commit_and_push(self, message, branch_name):
        """Commit and push changes."""
        self.repo.git.add(A=True)
        self.repo.index.commit(message)
        self.repo.remotes.origin.push(branch_name)
        print(f"Committed and pushed changes to branch: {branch_name}")
