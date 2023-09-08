# simple-netdevops-ci

## This code is meant to accompany the DevOps Shop video titled 'Simple NetDevOps CI with GitHub, Jenkins, pytest, and Webex'.

This is a simple and free CI pipeline that receives a webhook from GitHub whenever anything changes in the GitHub repo. The webhook triggers a build action in Jenkins that runs a shell that clones the GitHub repo and creates a virtual environment to run pytests. Currently, the repo I am cloning from is based on Ansible, so my tests are for Ansible playbooks and inventory files, but those can be adapted to test whatever you want. If a pytests fail, a messag with details is sent to a Webex space and the uild fails as well.

The code works with:
<ul>
<li>Jenkins 2.401.3 </li>
<li>pytest 7.4.0</li>
<li>Python 3.9.5</li>
<li>Webex 43.7.0.26612</li>
</ul>
<p align="center"><img src="https://github.com/xanderstevenson/simple-netdevops-ci/assets/27918923/c006358a-eba3-4a48-b1e0-8dc488223f2e" width="500" /></p>

The logic is as follows:

<p align="center"><img src="https://github.com/xanderstevenson/simple-netdevops-ci/assets/27918923/431a5e69-a103-42f8-a745-b75fbb7283d6" width="500" /></p>

Jenkins will require the GitHub plugin, at a minimum.

This project build upon the [Intro to Ansible for Automation](https://youtu.be/2rDAziMChXs) video in the DevOps Shop series. The code related to that video is found at [intro-ansible-automation](https://github.com/xanderstevenson/intro-ansible-automation)

## Installation

1. Create a GitHub Webhook directed at Jenkins
2. Install the GitHub plugin in Jenkins main settings
3. Configure a Freestyle Project in Jenkins
4. In the Jenkins project settings, set Git at the Source Code Management and add your source repo.  For Build Trigger, select "GitHub hook trigger". In the Build Steps, choose "Execute Shell" and ass this code:
#!/bin/bash
${JENKINS_HOME}/scripts/pytest.sh ${WORKSPACE}
5. Copy the files in this repo into your Jenkins home directory, where your workspace is located, adjusting file paths and such.
6. If you want to include the Webex alerting, you should include the Webex token and Room ID. Those can be found by following the instructions [here](https://blogs.cisco.com/developer/automatewebexspace01)
7. I have provided a requirements.txt I created from a pip freeze in my local directory. This could be useful for local testing but should not be necessary for a Jenkins build, which will create a virtual environment and install dependencies in it, based on the pytest.sh and the setup.py files.

## Usage

As it stands, the pytests check for syntax errors in Ansible playbooks and inventory host files, but new tests could be added for many other things. Quite simply, anytime you update the GitHub repo, it will send a webhook to Jenkins, where it will run the shell script build trigger that clones the GitHub repo and creates a virtual environment to run pytests. If a pytests fails, a Webex message is sent to a space, detailing what failed and the Jenkins build will fail as well. It would be a good idea to also add a Post Build Action in the Jenkins Project to send an email when a build is successful or fails.



