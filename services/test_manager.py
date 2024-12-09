import subprocess


class TestManager:
    @staticmethod
    def run_newman():
        """Run Newman regression tests."""
        try:
            subprocess.run(["newman", "run", "collection.json"], check=True)
            print("Newman tests succeeded.")
            return True
        except subprocess.CalledProcessError:
            print("Newman tests failed.")
            return False
