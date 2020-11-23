@retirement_age_calculator
Feature:  Full Retirement Age Calculator
  I want to calculate the age (with additional months) for obtaining full SSA benefits,
  and the year and month for obtaining full SSA benefits

  @age
  Scenario Outline: Calculate Retirement Age
    Given the retirement age is initialed
    When "<birthyear>" is entered
    Then the result is "<age>", "<month>"

    Examples:
      | birthyear | age | month |
      | 1928      | 65  | 0     |
      | 1940      | 65  | 6     |
      | 1958      | 66  | 8     |


  @remove
  Scenario Outline: Calculate Retirement Date
    Given the retirement age is initialed
    When "<birthyear>", "<birthmonth>", "<ageyear>", "<agemonth>" is entered
    Then the result is "<year>", "<month>"

    Examples:
      | birthyear | birthmonth | ageyear | agemonth | year | month |
      | 1942      | 7          | 65      | 10       | 2008 | 5     |
      | 1935      | 3          | 65      | 0        | 2000 | 3     |
      | 1967      | 9          | 67      | 0        | 2034 | 9     |