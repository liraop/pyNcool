#!/usr/bin/env python3

from controllers import GPUDataGatherer
from controllers import GPUManager as MANAGER

def main():
    """
    Main function x)
    """
    GATHERER = GPUDataGatherer.SMIFetcher()
    MANAGER.initialize(GATHERER)
    MANAGER.status()


if __name__ == '__main__':
    main()
