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
