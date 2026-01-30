"""Run Azure OCR on images in data/raw and save JSON to data/ocr.

Planned flow:
1) Load AZURE_DOC_INTEL_ENDPOINT / AZURE_DOC_INTEL_KEY from env.
2) Iterate images in data/raw.
3) Call Document Intelligence Read/Analyze.
4) Save word/line text + bbox to data/ocr/<image>.json.
"""

def main() -> None:
    print("TODO: implement Azure OCR pipeline")


if __name__ == "__main__":
    main()
