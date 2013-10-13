from setuptools import setup, find_packages
setup(
    name = "JenkJobs",
    version = "0.0.1",
    install_requires = "jenkins-job-builder",
    entry_points = {
      'jenkins_jobs.publishers': [
        'doxygen=jenkjobs:doxygen',
      ]
    },
    packages = find_packages(),
    author='RSDT@UCL',
    license='Apache License, Version 2.0',
    description="RSDT@UCL's extension to jenkins-job-builder"
)
