from setuptools import setup, find_packages

setup(
  name="MusicalMusic",
  version="0.0.2",
  description="Retrieve Sheet music from Musescore!",
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

