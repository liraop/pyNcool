#!/usr/bin/env python3

import GPU, logging, time, subprocess, shlex

def commandParser(osCommand):
	"""
	Simple OS command parser.

	Args:
		osCommand: The command to be parsed.
		e.g.: 'nvidia-smi -L'

	Returns:
		A string array corresponding to the osCommand stdout.
		e.g.: ['GPU', '0:', 'GeForce', 'GTX', '960', '(UUID:', 'GPU-1d11ae72-cd45-276f-0a0d-b2be8b74e4da)']

	"""
	command = shlex.split(osCommand)
	result = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)

	return result.stdout.read().split();

def main():
	print(commandParser("nvidia-smi -L"))

main()
