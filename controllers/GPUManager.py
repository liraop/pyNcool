from models.gpu import GPU

"""
A manager lying between data, GPUs and commands.

"""

GPU_SET = []

def add_gpu(gpu):
    """
    Add `gpu` in GPU_SET

    Args:
        gpu (GPU): GPU object

    """
    GPU_SET.append(gpu)

def update(gpu_data_fetcher):
    """
    Updates all GPUs temperature and fanspeed using `GPUDataFetcher`
    Preliminary method. > I better give it a thought later <

    """
    for gpu in GPU_SET:
        gpu.temperature = gpu_data_fetcher.get_gpu_temperature(gpu.slot)
        gpu.fanspeed = gpu_data_fetcher.get_gpu_fanspeed(gpu.slot)

#temporary for testing purproses
def status():
    for gpu in GPU_SET:
        print(gpu)
