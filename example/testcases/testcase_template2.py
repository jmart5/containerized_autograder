def main():
    result = student_submission.calculate_hypotenuse(3, 4)

    EXPECTED_RESULT = 5
    if result == EXPECTED_RESULT:
        PASS()
    else:
        FAIL()


main()
