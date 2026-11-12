import torch
import docling
import easyocr
print("Docling installed successfully")
print("EasyOCR installed successfully")
print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))
