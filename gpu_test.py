import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("CUDA version:", torch.version.cuda)

    # Test GPU calculation
    x = torch.rand(3000, 3000).cuda()
    y = torch.rand(3000, 3000).cuda()
    z = x @ y

    print("GPU calculation successful!")
    print("Result device:", z.device)
else:
    print("GPU not available")