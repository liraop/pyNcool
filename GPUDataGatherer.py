from abc import ABC, abstractmethod
import Utils

class GPUDataFetcher(ABC):

    @abstractmethod
    def get_gpu_count(self):
        """
        Get local machine total attached gpu devices

        Returns:
            Total attached GPU count

        """
        pass

    @abstractmethod
    def get_gpu_info(self, slot):
        """
        Get data from GPU in `slot`

        Returns:
            {slot,name} dict

        """
        pass

class SMIFetcher(GPUDataFetcher):
    """
    Fetching data using NVIDIA SMI commands
    """

    def get_gpu_count(self):

        return int(Utils.command_parser("nvidia-smi --query-gpu=count --format=csv,noheader"))


    def get_gpu_info(self, slot):

        gpu_data = {"slot":slot}

        command = "nvidia-smi -i %d --query-gpu=name --format=csv,noheader" % slot
        gpu_data["name"] = Utils.command_parser(command).strip()

        return gpu_data
