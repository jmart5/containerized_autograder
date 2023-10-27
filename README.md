<h1>Containerized Autograding Tool</h1>
<p align="center">
  <b>A easy-to-use autograding tool</b>
</p>

# Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Use](#use)
- [Common Errors](#common-errors)
- [Background](#background)


## Features

* Easy to run
* To-do

## Installation

* Download the Docker container image [here](https://hub.docker.com/repository/docker/jmart5/containerized_autograding/general). 
* Download the folder structure zip file from the repository [here](https://github.com/jmart5/containerized_autograder/tree/main).




## Use

## Common Errors

* Forgetting to add student submissions to the grading directory. <br>```AutograderError: No student submissions found in '/grading_dir'.```<br>
This error can be correct by adding the student submission files to the grading directory (grading_dir).
* Not adding test cases. `No suitable testcases found.` This will not return an error, but this message will appear in the grading comments. Make sure test case files have been added to the test case directory.

## Background

* An open-source autograding tool is used inside the container. The autograding tool, AutoGrader, was developed by ovsyanka83. For more information on AutoGrader, click [here](https://ovsyanka83.github.io/autograder/#/?id=usage).
