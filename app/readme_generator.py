import requests
from groq import Groq
from app.config import GROQ_API_KEY, GITHUB_TOKEN

client = Groq(api_key=GROQ_API_KEY)

GITHUB_API = "https://api.github.com"


def fetch_repo_data(repo: str) -> str:
    """
    Fetch real repository metadata from GitHub API.
    """
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }

    repo_url = f"{GITHUB_API}/repos/{repo}"
    response = requests.get(repo_url, headers=headers)

    if response.status_code != 200:
        return f"Repository {repo} not found or inaccessible."

    data = response.json()

    return f"""
Repository Name: {data.get('name')}
Description: {data.get('description')}
Stars: {data.get('stargazers_count')}
Forks: {data.get('forks_count')}
Open Issues: {data.get('open_issues_count')}
Primary Language: {data.get('language')}
"""


def generate_readme(repo: str) -> str:
    """
    Generate a COMPLETE professional README based on real repo data.
    """

    repo_info = fetch_repo_data(repo)

    prompt = f"""
You are a professional technical documentation writer.

Generate a COMPLETE GitHub README.md file in FULL MARKDOWN FORMAT.

Do NOT summarize.
Do NOT explain.
Do NOT add commentary.
Return ONLY the full README markdown.

Use this repository information:

{repo_info}

Include:

# Title
## Overview
## Features
## Installation
## Usage
## Project Structure
## Environment Variables
## Contributing
## License

Make it professional and realistic.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content

