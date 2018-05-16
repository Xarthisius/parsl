import parsl
from parsl import *
parsl.set_stream_logger()

matminer_util = {"sites":
                 [{"site": "pool_matminer_util",
                   "auth": {
                       "channel": None,
                   },
                   "execution": {
                       "executor": "ipp",
                       "provider": "kubernetes",
                       "namespace": "development",
                       "image": "039706667969.dkr.ecr.us-east-1.amazonaws.com/dlhubcontainers_matminer_util",
                       "secret": "ryan-kube-secret",
                       "block": {
                           "initBlocks": 1,
                           "maxBlocks": 1,
                           "minBlocks": 1,
                           "options": {"overrides": "pip3 install -U parsl"},
                       }
                   }
                   }],
                 "controller": {"publicIp": "128.135.250.229"}
                 }


dfk = DataFlowKernel(config=matminer_util)


@App('python', dfk)
def hello():
    return 'Hello World!'


print(hello().result())
