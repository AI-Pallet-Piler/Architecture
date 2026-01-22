import os
import subprocess

REPOS = {
    "Frontend":"https://github.com/AI-Pallet-Piler/Frond-end-.git",
    "Backend":"https://github.com/AI-Pallet-Piler/Backend.git",
    "API-gateway":"https://github.com/AI-Pallet-Piler/API-gateway.git"
}

# function to copy the repos in the parent directory
def Setup():
    # Get the current working directory and its parent and print them
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    print(f"Current Directory: {current_dir}")
    print(f"Working Directory: {parent_dir}")
    print(f"Working in parent directory: {parent_dir}")

    #pull the repos in the parent directory
    for repo_name, repo_url in REPOS.items():
        repo_path = os.path.join(parent_dir, repo_name)
        if os.path.exists(repo_path):
            print(f"{repo_name} already exists at {repo_path}, skipping clone.")
        else:
            print(f"Cloning {repo_name} from {repo_url} into {repo_path}")
            subprocess.run(["git", "clone", repo_url, repo_path])

Setup()