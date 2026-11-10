from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, ImageFormatOption

# Project folders
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def process_image():

    # Find converted PNG/JPG images
    images = [
        file for file in INPUT_DIR.iterdir()
        if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS
        and file.name != "sample.png"
    ]

    if not images:
        print("No supported image found!")
        return

    image_path = images[0]

    print(f"Processing: {image_path.name}")

    # Initialize Docling
    converter = DocumentConverter(
        allowed_formats=[InputFormat.IMAGE],
        format_options={
            InputFormat.IMAGE: ImageFormatOption()
        }
    )

    print("Starting image conversion...")

    # Convert image
    result = converter.convert(image_path)

    # Export Markdown
    markdown_text = result.document.export_to_markdown()

    # Save Markdown
    output_file = OUTPUT_DIR / "document.md"

    output_file.write_text(
        markdown_text,
        encoding="utf-8"
    )

    print("\nSUCCESS!")
    print("Markdown conversion completed.")
    print(f"Saved at: {output_file}")

    print("\nExtracted content preview:")
    print(markdown_text[:1500])


if __name__ == "__main__":
    process_image()