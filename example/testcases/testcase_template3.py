def main():
    result = student_submission.is_even_or_odd(566)

    EXPECTED_RESULT = "Even"
    if result == EXPECTED_RESULT:
        PASS()
    else:
        FAIL()

    result2 = student_submission.is_even_or_odd(569)

    EXPECTED_RESULT2 = "Odd"
    if result2 == EXPECTED_RESULT2:
        PASS()
    else:
        FAIL()


main()
