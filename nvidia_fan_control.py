#!/usr/bin/env python3

import GPU
import utils

def main():
    """
    Main function x)
    """

    gpu_counter = utils.get_gpu_count()
    print("%d GPU found on system" % gpu_counter)

main()
