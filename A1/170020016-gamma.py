import argparse

ap = argparse.ArgumentParser()


ap.add_argument("-n", required=True,
           help="first operand")
args = vars(ap.parse_args())


