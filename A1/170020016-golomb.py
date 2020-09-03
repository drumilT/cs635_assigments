import argparse

ap = argparse.ArgumentParser()


ap.add_argument("-m", required=True,
           help="first operand")
ap.add_argument("-n", required=True,
           help="second operand")
args = vars(ap.parse_args())


