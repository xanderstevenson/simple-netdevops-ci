from setuptools import setup, find_packages

setup(
    name='your-package-name',
    version='0.1',
    description='A description of your package',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),  # Automatically find all Python packages in the project
    install_requires=[
        # List the dependencies required by your package here
        'pytest',
        'setuptools',
        'ansible',
        'ansible-lint',
        'pyyaml',
        'requests'
    ],
)
