# 🚀 GitLab Pipeline Cleaner

A simple script to delete all pipelines from a specified GitLab project.

## 🌟 Features

- Fetch all pipelines from a GitLab project
- Delete all fetched pipelines

## 📋 Requirements

- Python 3.x
- `requests` library

## ⚙️ Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/woobe-studio/GitLab-Pipeline-Cleaner.git
    cd GitLab-Pipeline-Cleaner
    ```

2. **Install the required Python packages:**

    ```sh
    pip install requests
    ```

## 🚀 Usage

1. **Replace the placeholders in the script with your actual GitLab token and project ID:**

    ```python
    GITLAB_TOKEN = 'your_actual_token'
    PROJECT_ID = 'your_actual_project_id'
    ```

2. **Run the script:**

    ```sh
    python gitlab_pipeline_cleaner.py
    ```

## 📝 Script

```python
import requests

# Replace with your actual token and project ID
GITLAB_TOKEN = 'your_actual_token'
PROJECT_ID = 'your_actual_project_id'
GITLAB_URL = 'https://gitlab.com/api/v4'

headers = {
    'Private-Token': GITLAB_TOKEN
}

def get_pipelines(project_id):
    url = f"{GITLAB_URL}/projects/{project_id}/pipelines"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def delete_pipeline(project_id, pipeline_id):
    url = f"{GITLAB_URL}/projects/{project_id}/pipelines/{pipeline_id}"
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    return response.status_code == 204

def delete_all_pipelines(project_id):
    pipelines = get_pipelines(project_id)
    while pipelines:
        for pipeline in pipelines:
            pipeline_id = pipeline['id']
            success = delete_pipeline(project_id, pipeline_id)
            if success:
                print(f"Deleted pipeline {pipeline_id}")
            else:
                print(f"Failed to delete pipeline {pipeline_id}")
        pipelines = get_pipelines(project_id)

if __name__ == "__main__":
    delete_all_pipelines(PROJECT_ID)
````
## ⚠️ Warning
This script will delete all pipelines in the specified project. Use with caution.

## 🛠️ Troubleshooting

### Authentication Errors
- Ensure your GitLab token is correct and has the necessary permissions.

### Network Issues
- Make sure you have a stable internet connection.

Enjoy 🚀 cleaning up your GitLab pipelines! If you have any questions or run into issues, feel free to open an issue on GitHub or reach out for help. Happy coding!
