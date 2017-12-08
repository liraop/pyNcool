import Utils

def get_gpu_count():
    """
    Get local machine total attached gpu devices

    Returns:
        Total attached GPU count

    """

    return int(Utils.command_parser("nvidia-smi --query-gpu=count --format=csv,noheader"))


def get_gpu_info(slot):
    """
    Get data from GPU in `slot`

    Returns:
        {slot,name} dict

    """
    gpu_data = {"slot":slot}

    command = "nvidia-smi -i %d --query-gpu=name --format=csv,noheader" % slot
    gpu_data["name"] = Utils.command_parser(command).strip()

    return gpu_data
