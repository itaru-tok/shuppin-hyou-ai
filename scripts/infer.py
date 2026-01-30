"""Run OCR + YOLO + LLM postprocess and emit final JSON.

Planned flow:
1) Load OCR JSON from data/ocr.
2) Run YOLO on image to get car_exploded_diagram bbox.
3) Send OCR text to LLM for key/value extraction and correction.
4) Merge into final JSON under outputs/.
"""

def main() -> None:
    print("TODO: implement end-to-end inference")


if __name__ == "__main__":
    main()
