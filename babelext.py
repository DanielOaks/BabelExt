#!/opt/local/bin/python2.7

import __future__

import os
import sys

print("\nBabelExt")

# Argument Parsing

try:
	import argparse
except ImportError:
	print('You need argparse to run BabelExt. Python2.7 and above provide this.')

parser = argparse.ArgumentParser(description='Linking BabelExt extentions.')

parser.add_argument('-d', help='debug mode', action='store_true')
# example line to print debug info, given this argument:
#if vars(args)['d']: print('    Cleaning build/')

parser.add_argument('-b', help='build directory', dest='build_dir')

parser.add_argument('--clean', help='clean the build directory', action='store_true')
parser.add_argument('--link', help='link together the BabelExt extention', action='store_true')

args = parser.parse_args()

# because all the args are optional, we need to manually print the help
#  if the user doesn't select any thing to do
if not (vars(args)['clean'] or vars(args)['link']):
	parser.print_help()
	exit()


if vars(args)['build_dir']:
	build_dir = vars(args)['build_dir']
	if vars(args)['d']: print('    Build directory changed to ' + build_dir + '\n')
else:
	build_dir = 'build'


# extension cleaning
if vars(args)['clean']:
	if vars(args)['d']: print('    Cleaning ' + build_dir)

	# http://code.activestate.com/recipes/552732-remove-directories-recursively/
	import shutil
	def remove_dir(path):
		if os.path.isdir(path):
			shutil.rmtree(path)

	remove_dir(build_dir)


# extension linking
if vars(args)['link']:
	if vars(args)['d']: print('    Linking to ' + build_dir)
