import argparse

ap = argparse.ArgumentParser()


ap.add_argument("-n", required=True,
           help="first operand")
args = vars(ap.parse_args())

n = int(args["n"])

binary_form = str(bin(n).replace("0b", ""))
offset = binary_form[1:]
length = "".join(["1" for _ in range(1,len(binary_form))]) + "0"
print(length+", "+offset)





