#%%


import torch

# Default
# %%

torch.cuda.is_available()

# %%

dtype = torch.float
device = torch.device("cuda")

tensor = torch.randn((5, 5), device=device, dtype=dtype)


tensor


# %%

import torch
import torchvision
import torchvision.transforms as transforms


x: int = "34"
