import argparse
import math

ap = argparse.ArgumentParser()


ap.add_argument("-m", required=True,
           help="first operand")
ap.add_argument("-n", required=True,
           help="second operand")
args = vars(ap.parse_args())

n = int(args["n"])
m = int(args["m"])

rem = int(n%m)
quo = int(n/m)

out = "".join(["1" for _ in range(quo)])+"0"
b = int(math.log(m,2))+1
cut_off = math.pow(2,b)-m
    
if rem < cut_off:
    rem_bin = str(bin(rem).replace("0b", ""))
    rem_bin= "".join(["0" for _ in range(1,b-len(rem_bin))])+rem_bin
else:
    rem += int(cut_off)
    rem_bin = str(bin(rem).replace("0b", ""))
    rem_bin= "".join(["0" for _ in range(1,b+1-len(rem_bin))])+rem_bin
if m==1:
    rem_bin =""

print(out+rem_bin)


