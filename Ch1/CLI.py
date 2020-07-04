import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")  # 增加 echo 位置参数名解释它的作用
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()

# if args.echo:
#     print(args.echo)

if args.square:
    print(args.square ** 2)
