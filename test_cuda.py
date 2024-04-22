import torch
import torch.cuda

x = torch.tensor([1, 2, 3])

if torch.cuda.is_available():
    x = x.to('cuda')

print('is x on gpu: ',x.device)

print("torch.version.cuda", torch.version.cuda)
print('torch version: ', torch.__version__)


print("")