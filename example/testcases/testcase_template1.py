def main():
    integer_list = [10, 25, 7, 42, 15, 31]
    result = student_submission.findMax(integer_list)

    EXPECTED_RESULT = 42
    if result == EXPECTED_RESULT:
        PASS()
    else:
        FAIL()


main()
