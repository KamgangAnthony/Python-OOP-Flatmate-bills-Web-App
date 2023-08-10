import calendar


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    total_num_of_days = 0

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        Flatmate.total_num_of_days += days_in_house

    def pays(self, bill):
        # month, year = bill.period.split()
        #
        # num_days = calendar.monthrange(int(year), list(calendar.month_name).index(month))[1]

        return round((self.days_in_house / self.total_num_of_days) * bill.amount, 2)
