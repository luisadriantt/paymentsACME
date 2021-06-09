from datetime import timedelta
from utils.time_parser import to_24_hours, format_hour, hour_to_number, hours_to_tuple, number_to_hour
from utils.constants import ZERO_WORK, TWELVE_PM, WEEK, PAYMENT_RATES
from utils.file_parser import read_parse_file


class PaymentCalc:

    def __init__(self, input_data):
        self.input_data = input_data

    # Given a list of strings with employees work info, returns the pay rate for each employee
    def compute_pay_rates(self):
        work_list = read_parse_file(self.input_data)
        if len(work_list) == 0:
            print("File is empty")
        else:
            for line in work_list:
                employee = line.split("=")[0]
                amount = self.to_pay_per_week(line)
                print(f'The amount to pay {employee} is: {amount} USD')

    # Returns the amount to pay an employee for a week of work as well as the name
    def to_pay_per_week(self, line_of_work):
        amount = 0

        worked_schedule = line_of_work.split("=")[1].split(",")
        for day in worked_schedule:
            amount += self.to_pay_per_day(day)
        return amount

    # Calculates the amount to pay per day
    def to_pay_per_day(self, day):
        amount = 0
        worked_from = timedelta(hours=int(day.split("-")[0][2:4]))
        worked_to = timedelta(hours=int(day.split("-")[1][:2]))
        worked_day = day[:2]
        subtract_hours_worked = worked_to - worked_from
        total_hours_worked = format_hour(subtract_hours_worked)
        day_type = "week" if worked_day in WEEK else "weekend"

        hours_ranges = [*PAYMENT_RATES.get(day_type).keys()]

        for i in range(len(hours_ranges)):
            rate_from = number_to_hour(hours_ranges[i][0])
            rate_to = number_to_hour(hours_ranges[i][1])
            worked_hours = total_hours_worked

            if rate_from <= worked_from <= to_24_hours(rate_to):
                n_rate_to = rate_to if worked_to <= TWELVE_PM else to_24_hours(rate_to)
                if to_24_hours(worked_to) > n_rate_to:
                    subtract_hours = n_rate_to - worked_from
                    worked_hours = format_hour(subtract_hours)

                range_rate_hours = hours_to_tuple(rate_from, rate_to)
                amount += self.to_pay_per_hour(worked_day, worked_hours, range_rate_hours)

                # If worked hours out of range
                if total_hours_worked > worked_hours:
                    left_to_pay = total_hours_worked - worked_hours
                    new_index = i + 1
                    while left_to_pay > ZERO_WORK:
                        next_rate = new_index if new_index < len(hours_ranges) else 0
                        rate_from = number_to_hour(hours_ranges[next_rate][0])
                        rate_to = number_to_hour(hours_ranges[next_rate][1])
                        left_in_range = to_24_hours(rate_to) - rate_from
                        range_rate_hours = hours_to_tuple(rate_from, rate_to)

                        if left_in_range > left_to_pay:
                            amount += self.to_pay_per_hour(worked_day, left_to_pay, range_rate_hours)
                            left_to_pay -= left_to_pay
                        else:
                            amount += self.to_pay_per_hour(worked_day, left_in_range, range_rate_hours)
                            left_to_pay -= left_in_range
                            new_index += 1
        return amount

    # Returns the amount to pay for the given hour and day
    @staticmethod
    def to_pay_per_hour(day, worked_hours, hours_range):
        if day in WEEK:
            pay_rate = PAYMENT_RATES.get("week").get(hours_range)
            return hour_to_number(worked_hours) * pay_rate
        else:
            pay_rate = PAYMENT_RATES.get("weekend").get(hours_range)
            return hour_to_number(worked_hours) * pay_rate
