#!/opt/local/bin/python2

import __future__

import os
import sys

# Argument Parsing

try:
	import argparse
except ImportError:
	print('You need argparse to run BabelExt. Python2.7 and above provide this.')

parser = argparse.ArgumentParser(description='Linking BabelExt extentions.')

parser.add_argument('-d', help='debug mode', action='store_true')
# example line to print debug info, given this argument:
#if vars(args)['d']: print('    Cleaning build/')

parser.add_argument('-b', help='build directory, defaults to: build', dest='build_dir')

parser.add_argument('--clean', '-c', help='clean the build directory', action='store_true')
parser.add_argument('--link', '-l', help='link together the BabelExt extention', action='store_true')

args = parser.parse_args()

# because all the args are optional, we need to manually print the help
#  if the user doesn't select any thing to do
if not (vars(args)['clean'] or vars(args)['link']):
	parser.print_help()
	exit()


if vars(args)['build_dir']:
	build_dir = vars(args)['build_dir']
	if vars(args)['d']: print('  Build directory changed to ' + build_dir)
else:
	build_dir = 'build'

if vars(args)['link']:
	vars(args)['clean'] = True

# http://code.activestate.com/recipes/552732-remove-directories-recursively/
import shutil
def remove_dir(path):
	if os.path.isdir(path):
		shutil.rmtree(path)


# extension cleaning
if vars(args)['clean']:
	if vars(args)['d']: print('  Cleaning ' + build_dir)

	remove_dir(build_dir)


# extension linking
if vars(args)['link']:
	if vars(args)['d']: print('  Linking to ' + build_dir)

	if vars(args)['d']: print('    Copying bases into ' + build_dir)
	shutil.copytree('base', build_dir)
