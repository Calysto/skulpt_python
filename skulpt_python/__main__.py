from IPython.kernel.zmq.kernelapp import IPKernelApp 
from .kernel import SkulptPythonKernel
IPKernelApp.launch_instance(kernel_class=SkulptPythonKernel) 
