Feature: Sorting
    sorting abc
    Scenario: Sort_abs with original sort
        Given There is an array which is [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
        When I sort this array originally
        Then Array is [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]

    Scenario: Sort_abs with lambda sort
        Given There is an array which is [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
        When I sort this array with lambda
        Then Array is [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]