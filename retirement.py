def _validate_age_month(month):
  month = int(month)

  if month < 0 or month > 11:
    raise ValueError(f'Age month "{month}" must be between 0 and 11')

  return month


def _validate_age_year(year):
  year = int(year)

  if year < 65 or year > 67:
    raise ValueError(f'Age year "{year}" must be between 65 and 67')

  return year


def _validate_birth_month(month):
  month = int(month)

  if month < 1 or month > 12:
    raise ValueError(f'Birth month "{month}" must be between 1 and 12')

  return month


def _validate_birth_year(year):
  year = int(year)

  if year < 1900:
    raise ValueError(f'Birth year "{year}" must be no earlier than 1900')
  elif year >= 3000:
    raise ValueError(f'Birth year "{year}" must be earlier than 3000')

  return year

class RetireAge:

    def __init__(self, age=0, month=0):
        self._age = age
        self._month = month

    @property
    def age(self):
        return self._age

    @property
    def month(self):
        return self._month

    def calculate_retirement_age(self, birth_year):
        birth_year = _validate_birth_year(birth_year)

        if birth_year <= 1937:
            self._age = 65
            self._month = 0
        elif birth_year == 1938:
            self._age = 65
            self._month = 2
        elif birth_year == 1939:
            self._age = 65
            self._month = 4
        elif birth_year == 1940:
            self._age = 65
            self._month = 6
        elif birth_year == 1941:
            self._age = 65
            self._month = 8
        elif birth_year == 1942:
            self._age = 65
            self._month = 10
        elif 1943 <= birth_year <= 1954:
            self._age = 66
            self._month = 0
        elif birth_year == 1955:
            self._age = 66
            self._month = 2
        elif birth_year == 1956:
            self._age = 66
            self._month = 4
        elif birth_year == 1957:
            self._age = 66
            self._month = 6
        elif birth_year == 1958:
            self._age = 66
            self._month = 8
        elif birth_year == 1959:
            self._age = 66
            self._month = 10
        else:
            self._age = 67
            self._month = 0

class RetireDate:

    def __init__(self, year=0, month=0):
        self._year = year
        self._month = month

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    def calculate_retirement_date(self, birth_year, birth_month, age_years, age_months):
        birth_year = _validate_birth_year(birth_year)
        birth_month = _validate_birth_month(birth_month)
        age_years = _validate_age_year(age_years)
        age_months = _validate_age_month(age_months)

        year = birth_year + age_years
        month = birth_month + age_months

        if month > 12:
            year += 1
            month -= 12

        self._year = year
        self._month = month
