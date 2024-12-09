import argparse
from services.config_loader import ConfigLoader
from services.git_manager import GitManager
from services.build_manager import BuildManager
from services.test_manager import TestManager
from services.mr_manager import MRManager


def main():
    parser = argparse.ArgumentParser(description="Automation Tool")
    parser.add_argument("--config", required=True, help="Path to the configuration file")
    args = parser.parse_args()

    # Load configuration
    config = ConfigLoader.load(args.config)

    # Initialize managers
    git_manager = GitManager(config["gitlab_url"], config["base_dir"])
    build_manager = BuildManager()
    test_manager = TestManager()
    mr_manager = MRManager(config["gitlab_url"], config["gitlab_token"])

    # Workflow
    git_manager.clone()
    git_manager.switch_branch(config["base_branch"])
    git_manager.pull_branch(config["base_branch"])

    if not build_manager.build(config["base_dir"]):
        return

    build_manager.run_dev_mode(config["base_dir"])
    test_manager.run_newman()

    git_manager.create_branch(config["feature_branch"])
    git_manager.commit_and_push(f"Implement feature: {config['ticket_id']}", config["feature_branch"])

    mr_manager.create_merge_request(
        config["group_id"], config["feature_branch"], config["base_branch"], config["mr_title"], config["mr_description"]
    )

    if not build_manager.build(config["base_dir"]):
        return
    build_manager.run_dev_mode(config["base_dir"])
    test_manager.run_newman()


if __name__ == "__main__":
    main()
