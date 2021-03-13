#!/bin/python3

from os import path, listdir, _exit
from subprocess import run
from sys import argv, exit

# Extensions that are used to recognize input format. Must not include
# output format extension
Input_Format_Extensions = ['.mp4']
Output_Format_Extension = '.mkv'

def log(string):
    print("[[" + path.basename(__file__) + "]] " + string)

def convert(src, dest):
	"Convert src file into dest file via ffmpeg"
	command = f"ffmpeg -hide_banner -i '{src}' -c:v libx265 -preset ultrafast '{dest}'"
	log('$ ' + command)
	return run(command, shell=True).returncode == 0

def process_file(input):
	"If input file does not have matching output file, create it via convert function."
	output = path.splitext(input)[0] + Output_Format_Extension
	if path.isfile(output):
	    log(f'skipping {input}')
	    return

	if not convert(input, output):
		log(f'Failed processing {input}')
		exit(1)

def process_directory(directory = '.'):
	"Process each file with input format extension in given directory"
	for filename in listdir(directory):
		if any(filename.endswith(ext) for ext in Input_Format_Extensions):
			process_file(filename)

def main():
	# Unify arguments behaviour with two potential calling methods:
	# 	./convert.py via #!
	# 	python convert.py
	this_file = path.abspath(__file__)
	args = [p for p in argv[1:] if path.abspath(p) != this_file]

	if len(args) == 0:
		process_directory()
		return

	for entry in args:
		if path.isdir(entry):
			process_directory(entry)
		else:
			process_file(entry)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as ki:
		try: exit(1)
		except: _exit(1)
