from setuptools import setup, find_packages

setup(
  name="MusicalMusic",
  version="0.1.2",
  description="Retrieve Sheet music from Musescore!",
  long_description=open("README.md").read(),
  long_description_content_type='text/markdown',
  url="https://github.com/frankye8998/MusicalMusic/",
  author="Frank Ye",
  author_email="frankfrankfrankyeyeye@gmail.com",
  license="GPL 3.0",
  classifiers=[
    "Programming Language :: Python :: 3"
  ],
  packages=find_packages(),
  install_requires=["requests","bs4"]
)

