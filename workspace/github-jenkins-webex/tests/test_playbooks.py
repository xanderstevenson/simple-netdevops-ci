import os
import subprocess
import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_playbooks():
    # Define the root directory to start from
    # You should replace with your own
    root_directory = "/Users/alexstev/.jenkins/workspace/github-jenkins-webex"
    
    # Get a list of all playbook files in the root directory
    playbook_files = [
        os.path.join(root_directory, file)
        for file in os.listdir(root_directory)
        if file.endswith(".yaml")
    ]
    
    # Get a list of all playbook files in one level of child directories
    child_directories = [
        os.path.join(root_directory, directory)
        for directory in os.listdir(root_directory)
        if os.path.isdir(os.path.join(root_directory, directory))
    ]
    
    for directory in child_directories:
        playbook_files.extend([
            os.path.join(directory, file)
            for file in os.listdir(directory)
            if file.endswith(".yaml")
        ])
    
    for playbook in playbook_files:
        logger.info(f"Running playbook: {playbook}")
        result = subprocess.run(["ansible-playbook", playbook, "-i", "hosts"], capture_output=True, text=True)
        logger.info("test")
        # Check the return code and output for assertions
        assert result.returncode == 0
        assert "PLAY RECAP" in result.stdout
