import requests

# Replace with your actual token and project ID
GITLAB_TOKEN = 'your_actual_token'
PROJECT_ID = 'your_actual_project_id'
GITLAB_URL = 'https://gitlab.com/api/v4'

headers = {
    'Private-Token': GITLAB_TOKEN
}

def get_pipelines(project_id):
    """Fetch all pipelines for the given project."""
    url = f"{GITLAB_URL}/projects/{project_id}/pipelines"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def delete_pipeline(project_id, pipeline_id):
    """Delete a specific pipeline by ID."""
    url = f"{GITLAB_URL}/projects/{project_id}/pipelines/{pipeline_id}"
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code == 204

def delete_all_pipelines(project_id):
    """Delete all pipelines for the given project."""
    while True:
        pipelines = get_pipelines(project_id)
        if not pipelines:
            print("No more pipelines to delete.")
            break
        
        for pipeline in pipelines:
            pipeline_id = pipeline['id']
            success = delete_pipeline(project_id, pipeline_id)
            if success:
                print(f"Successfully deleted pipeline {pipeline_id}")
            else:
                print(f"Failed to delete pipeline {pipeline_id}")

if __name__ == "__main__":
    delete_all_pipelines(PROJECT_ID)
