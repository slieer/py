import torch
a = torch.ones(3, 3).to('cuda')
b = torch.ones(3, 3).to('cuda')
print(a + b)

