# Local OCR

Convert an image containing text into a Markdown document using [Docling](https://github.com/docling-project/docling).

## Requirements

- Python 3.10 or newer
- Docling

Install Docling in your Python environment:

```powershell
python -m pip install docling
```

## Usage

1. Create an `input` folder in the project directory and place a `.jpg`, `.jpeg`, or `.png` image in it.
2. Run the converter:

   ```powershell
   python main.py
   ```

The script processes the first supported image it finds in `input` (excluding `sample.png`) and writes the extracted Markdown to `output/document.md`. The `output` folder is created automatically.

## GPU smoke test

`gpu_test.py` reports whether PyTorch can access CUDA and, when available, runs a small matrix multiplication on the GPU. It requires PyTorch:

```powershell
python -m pip install torch
python gpu_test.py
```

`docling_test.py` is an additional dependency check for Docling, EasyOCR, and PyTorch.
