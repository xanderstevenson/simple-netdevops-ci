import pytest
import glob
import os
import subprocess

# Test for syntax errors in Ansible hosts files
def test_hosts_syntax():
    hosts_files = glob.glob("../**/hosts", recursive=True)
    for hosts_file in hosts_files:
        # Skip directories
        if os.path.isdir(hosts_file):
            continue

        # Check for syntax errors using the ansible-inventory command
        result = subprocess.run(["ansible-inventory", "--list", "-i", hosts_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            pytest.fail(f"Syntax error in {hosts_file}:\n{result.stderr}")
