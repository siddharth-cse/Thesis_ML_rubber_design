import sys
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p', type=int, nargs=8,help='parameters for rubber geometry')
parser.add_argument('-r', type=int, nargs=1,help='parameters for insert geometry')

args = parser.parse_args()
print(args.p,args.r)

