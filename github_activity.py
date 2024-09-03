import sys
import urllib.request
import json

def fetch_github_activity(username):
    # Construct the URL for the GitHub API
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        # Fetch data from the GitHub API
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
            events = json.loads(data)
            
            # Display recent activities
            for event in events:
                if event["type"] == "PushEvent":
                    repo_name = event["repo"]["name"]
                    commit_count = len(event["payload"]["commits"])
                    print(f"Pushed {commit_count} commits to {repo_name}")
                elif event["type"] == "IssuesEvent":
                    action = event["payload"]["action"]
                    repo_name = event["repo"]["name"]
                    print(f"{action.capitalize()} an issue in {repo_name}")
                elif event["type"] == "WatchEvent":
                    repo_name = event["repo"]["name"]
                    print(f"Starred {repo_name}")
                # Add more event types if needed
            
    except urllib.error.HTTPError as e:
        print(f"Error fetching data from GitHub API: {e}")
    except urllib.error.URLError as e:
        print(f"Network error: {e}")
    except json.JSONDecodeError:
        print("Error decoding the JSON response.")

def main():
    if len(sys.argv) < 2:
        print("Usage: github-activity <username>")
        return
    
    username = sys.argv[1]
    fetch_github_activity(username)

if __name__ == "__main__":
    main()
