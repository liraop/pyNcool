from abc import ABC, abstractmethod
import Utils

class GPUDataFetcher(ABC):
    """
    A class/interface/metaclass to gather data from GPU.

    This design choice was made to promote the use both nvidia-smi and nvidia-settings commands
    as well any other agent to gather data from the actual hardware GPU.
    """

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
        Get identification from GPU in `slot`

        Returns:
            {slot,name} dict

        """
        pass

    @abstractmethod
    def get_gpu_temperature(self, slot):
        """
        Get core temperature from GPU in `slot`

        Returns:
            Temperature in Celcius
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

    def get_gpu_temperature(self, slot):

        command = "nvidia-smi -i %d --query-gpu=temperature.gpu --format=csv,noheader" % slot
        temperature = Utils.command_parser(command).strip()

        return temperature
