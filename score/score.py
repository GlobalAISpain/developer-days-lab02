import os
import torch
import torch.nn as nn
from torchvision import transforms
import json
import logging

#GAI Get the latest version of ML model and load it with pytorch
def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model
    

#GAI Make model inference and define the classes. Apply softmax layer
def run(input_data):
    input_data = torch.tensor(json.loads(input_data)["data"])

    # get prediction
    with torch.no_grad():
        

    result = {"label": classes[index], "probability": str(pred_probs[index])}
    return result