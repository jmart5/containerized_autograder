#!/bin/bash

# Docker command to run the grader
docker run -v "$(pwd)":/grading_dir -w /grading_dir -v "$(pwd)"/tests/testcases:/grading_dir/tests/testcases grader-oct21 /bin/bash -c "autograder run && cd / && python3 ./csv_generator.py"

