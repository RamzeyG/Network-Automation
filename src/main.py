from ssh_automate import *

parser = argparse.ArgumentParser()
parser.add_argument('-kfile', '--kevinfile')
parser.add_argument('-sf', '--singlefile')
parser.add_argument('-b', '--devicebrand', default='cisco')

args = parser.parse_args()


Main(args)
