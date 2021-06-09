from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from payment_calc import PaymentCalc


class Main:
    # Run program
    @staticmethod
    def run(file):
        calc = PaymentCalc(file)
        calc.compute_pay_rates()


if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--file', dest="file", required=True, help="work info file")
    options = parser.parse_args()

    pg = Main()
    pg.run(options.file)