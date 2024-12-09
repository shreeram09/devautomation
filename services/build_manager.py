import subprocess


class BuildManager:
    @staticmethod
    def build(repo_dir):
        """Run Maven build."""
        try:
            subprocess.run(["mvn", "clean", "install"], cwd=repo_dir, check=True)
            print("Build succeeded.")
            return True
        except subprocess.CalledProcessError:
            print("Build failed.")
            return False

    @staticmethod
    def run_dev_mode(repo_dir):
        """Run the application in dev mode."""
        subprocess.Popen(["mvn", "quarkus:dev"], cwd=repo_dir)
        print("Running in dev mode.")
