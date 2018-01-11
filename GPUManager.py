from models.gpu import GPU

"""
A manager lying between data, GPUs and commands.

"""

GPU_SET = []

def add_gpu(GPU):
    """
    Add a `GPU` to `slot` in the GPU_SET

    Args:
        slot (int): GPU's slot on system.
        gpu (GPU): GPU object.

    """
    GPU_SET.append(GPU)
