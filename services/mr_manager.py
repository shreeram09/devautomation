import requests


class MRManager:
    def __init__(self, gitlab_url, token):
        self.gitlab_url = gitlab_url
        self.token = token

    def create_merge_request(self, project_id, source_branch, target_branch, title, description):
        """Create a merge request."""
        headers = {"PRIVATE-TOKEN": self.token}
        data = {
            "id": project_id,
            "source_branch": source_branch,
            "target_branch": target_branch,
            "title": title,
            "description": description,
        }
        response = requests.post(f"{self.gitlab_url}/api/v4/projects/{project_id}/merge_requests", headers=headers, data=data)
        if response.status_code == 201:
            print("Merge request created successfully.")
        else:
            print(f"Failed to create merge request: {response.text}")
