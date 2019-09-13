import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--msg', type=str)
args = vars(parser.parse_args())

msg = args['msg']

f = open('../output.txt', 'w')
f.writelines(msg)
f.close()

f1 = open('../output.txt', 'r')
print(f1.read())
f1.close()