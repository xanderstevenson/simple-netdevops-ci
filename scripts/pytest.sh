#    This script does the followings:
#
#   1. If virtual directory ${WORKSPACE}/venv exists, remove all of it.
#
#   2. Create virtual environment ${WORKSPACE}/venv, then activate it.
#
#   3. Run editable install for the project.
#
#   4. Finally run pytest.
#
#   5. Send pytest results to Webex notification script

#!/bin/bash

if [ -z $1 ]; then
    echo "Usage: ${0##*/} <dir>"
    exit 1
fi
 
if [ ! -d $1 ]; then
    echo "$1 does not exist."
    exit 1
fi
 
virtual_dir=$1/venv
 
echo "Virtual directory $virtual_dir."
 
if [ -d $virtual_dir ]; then
    rm -rf $virtual_dir
    echo "$virtual_dir removed."
fi
 
# Create a virtual environment
/Users/alexstev/.pyenv/shims/virtualenv $virtual_dir

# Activate the virtual environment
source $virtual_dir/bin/activate

# Install your project and pytest
$virtual_dir/bin/pip install -e .
$virtual_dir/bin/pip install pytest

# Run pytest on hosts_test.py and playbooks_test.py
pytest_output=$($virtual_dir/bin/pytest $1/tests/test_hosts.py $1/tests/test_playbooks.py)

# Capture the exit code of pytest
pytest_exit_code=$?

# Deactivate the virtual environment
deactivate

# Get the Jenkins build number
build_number=$BUILD_NUMBER

# Check the exit code of pytest and send results to webex_notification_script.py
if [ $pytest_exit_code -ne 0 ]; then
    # Pytest failed
    message="Pytest FAILED in Jenkins"

    # Add the details section with triple backticks
    message+="

    Details: 

    build #$build_number

    $pytest_output"

    # Call webex_notification_script.py with the message
    /Users/alexstev/.pyenv/shims/python3 $WORKSPACE/scripts/webex_notification_script.py "$message"
fi

# Exit with the same exit code as pytest
exit $pytest_exit_code
