#!/usr/bin/env python3

import GPU, logging, time, subprocess, utils

def main():
	print(utils.commandParser("nvidia-smi -L"))

main()
