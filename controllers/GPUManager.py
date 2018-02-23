"""
A manager lying between data, GPUs and commands.

"""

from models.gpu import GPU
from utils.parsers import command_parser

GPU_SET = []

def add_gpu(gpu):
    """
    Add `gpu` in GPU_SET

    Args:
        gpu (GPU): GPU object

    """
    GPU_SET.append(gpu)

def initialize(gdf):
    """
    Initialize all GPUs on system using `gdf`
    > it is wise give it a thought or two later

    Args:
        gdf (GPUDataFetcher): Instance of data fetcher

    """
    for i in range(gdf.get_gpu_count()):
        gpu_slot, gpu_model = gdf.get_gpu_info(i)
        add_gpu(GPU(gpu_slot, gpu_model))

    full_update(gdf)

def full_update(gdf):
    """
    Updates all GPUs temperature and fanspeed using `gdf`
    > Probably a temporary method.

    Args:
        gdf (GPUDataFetcher): Instance of the fetcher to gather data

    """
    for gpu in GPU_SET:
        enable_fancontrol(gpu, True)
        gpu.temperature = gdf.get_gpu_temperature(gpu.slot)
        gpu.fanspeed = gdf.get_gpu_fanspeed(gpu.slot)
        enable_fancontrol(gpu, False)

def enable_fancontrol(gpu, enable):
    """
    Set `gpu` fan control as `status`.

    Args:
        gpu (GPU): Instance of GPU
        enable (boolean): True for enable, False for disable
    """

    if enable:
        state = 1
    else:
        state = 0

    command = "nvidia-settings -a [gpu:%s]/GPUFanControlState=%i" % (gpu.slot, state)
    command_parser(command)


#temporary for testing purproses
def status():
    for gpu in GPU_SET:
        print(gpu)
