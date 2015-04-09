from setuptools import setup, find_packages
setup(
    name="JenkJobs",
    version="0.0.2",
    install_requires="jenkins-job-builder",
    entry_points={
      'jenkins_jobs.publishers': [
        'rsdt_doxygen=jenkjobs:rsdt_doxygen',
      ],
      'jenkins_jobs.properties': [
        'trac=jenkjobs:trac',
      ]
    },
    packages=find_packages(),
    author='RSDT@UCL',
    license='Apache License, Version 2.0',
    description="RSDT@UCL's extension to jenkins-job-builder"
)
