#!/usr/bin/env python3

import logging, time, subprocess, shlex


def getGPUTemperature():
	textCommand = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits"
	command = shlex.split(textCommand)
	temperature = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)

	return temperature.stdout.read().strip()


def main():
	logging.basicConfig(level="INFO")

	logging.info("GPU temperature: %s°C", getGPUTemperature())


main()
