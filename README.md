<style>
  body {
    background-color: #00264d;
    border: 5px solid FLoralWhite;
    padding: 2px;
    font-family: "Verdana";
  }

  p {
    color: FLoralWhite;
    font-size: 16px;
  }

  h1 {
    color: FLoralWhite;
    font-size: 24px;
  }

  h2 {
    color: FLoralWhite;
    font-size: 20px;
  }

  ul {
    list-style-type: square;
    color: FLoralWhite;
  }

  li {
    margin-bottom: 8px;
  }

  a {
    text-decoration: none;
    color: FLoralWhite;
  }

  code {
    background-color: white;
    padding: 4px;
    font-family: "Helvetica", monospace;
    color: Gray;
  }
</style>


<h1>Containerized Autograding Tool</h1>
<p align="center">
  <b>An easy-to-use autograding tool inside a container</b>
</p>

# Table of Contents

- [Description](#Description)
- [Features](#features)
- [Installation](#installation)
- [Use](#use)
- [Tutorial](#tutorial)
- [Common Errors](#common-errors)
- [Reference Information](#reference-information)

## Description
This is an autograding tool that runs inside a Docker container. This tool can be used to grade programming assignments automatically. All that is needed to use the tool is the Docker image and the specific directory strucutre discussed below. The student submisison files and testing files can be added to their respective directories. Then the tool can be executed. 

## Features

* Easy to setup and run
* Compatible with Mac, Linux, and Windows
* Capable of grading programming assignments in C, C++, Java, and Python
* Student Self-Checking is possible 

## Installation

* First, download the Docker container image [here](https://hub.docker.com/repository/docker/jmart5/containerized_autograding/general). 
* Next, download the folder structure zip file from the repository [here](https://github.com/jmart5/containerized_autograder/tree/main). There is a Mac/Linux version and a Windows version.


## Use

1. Place student assignment submissions inside the main grading directory. 
  1.1 Ensure that all assignement followed the file naming convention: `lastname_firstname_hw##.fileExtension`

2. Place test cases, output cases, and input cases into their respective directories inside the `tests` directory.

3. Verify that Docker is running on your local machine.

4. Navigate to the main grading directory using your systems command line. Once there, execute the following command:

  4.1 Mac & Linux
  `./startup/run_grader.sh`

  4.2 Windows
  `.\startup\run-autograder.bat`

  The autograding container will be initiated. If any errors are encountered check [here](#common-errors) for more information.

5.The results directory will be automatically created inside the main grading directory upon completion. Inside this directory, the `results_summary.csv` file contains a summary of the grades for each submission. Individual submission results are also available.

## Tutorial


## Common Errors

* Make sure Docker is running. `docker: Cannot connect to the Docker daemon at ...`
* Forgetting to add student submissions to the grading directory. <br>```AutograderError: No student submissions found in '/grading_dir'.```<br>
This error can be correct by adding the student submission files to the grading directory (grading_dir).
* Not adding test cases. `No suitable testcases found.` This will not return an error, but this message will appear in the grading comments. Make sure test case files have been added to the test case directory.
* Make sure to clear old results from directory before rerunning.
* Warning - When opening the `results_summary.csv` file in Excel, the values of the comments sections will not be visible. This is an issue with the automatic importing of CSV files into Excel. The comment values are present in the CSV file.

## Reference Information

* An open-source autograding tool is used inside the container. The autograding tool, AutoGrader, was developed by ovsyanka83. For more information on AutoGrader, click [here](https://github.com/zmievsa/autograder).
* The CSV results output file was generated using a python script developed by jmart5. For more information, click [here](https://github.com/jmart5/results_generator).
