from datetime import timedelta

""""
    Constants used through the project
"""""

ZERO_WORK = timedelta(hours=0)
TWELVE_PM = timedelta(hours=12)

WEEK = ['MO', 'TU', 'WE', 'TH', 'FR']
WEEKEND = ['SA', 'SU']
PAYMENT_RATES = {
    "week": {
        (0, 9): 25,
        (9, 18): 15,
        (18, 0): 20
    },
    "weekend": {
        (0, 9): 30,
        (9, 18): 20,
        (18, 0): 25
    }
}
