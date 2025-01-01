# NudeDetect

NudeDetect is a Python-based tool for detecting nudity and adult content in images. This project combines the capabilities of the NudeNet library, EasyOCR for text detection, and the Better Profanity library for identifying offensive language in text.

## Features

- **Nudity Detection:** Detects nudity in images using NudeNet's pre-trained models.
- **Adult Content Detection:** Identifies adult or offensive text content using EasyOCR and Better Profanity.
- **Text Detection:** Reads and processes text from images with EasyOCR.
- **Visualization:** Highlights detected text in images using OpenCV and Matplotlib.

---

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.7 or higher is recommended). Then, clone this repository:

```bash
git clone https://github.com/darkwaves-ofc/nude-detect.git
cd nude-detect
```

### Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Requirements
The following Python libraries are used in this project:
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [NudeNet](https://github.com/notAI-tech/NudeNet)
- [Better Profanity](https://github.com/snguyenthanh/better_profanity)
- NumPy
- OpenCV
- Matplotlib

---

## Usage

### 1. Nudity Detection
To detect nudity in an image, use the script `main.py`:
1. Set the path to the image in `image_path`.
2. Run the script:

```bash
python main.py
```

### 2. Text Detection and Profanity Check
To detect text and check for profanity in an image, use the script `text_image.py`:
1. Update the `image_path` variable with the image's path.
2. Run the script:

```bash
python text_image.py
```

### Output
- The `main.py` script outputs:
  - Whether the image contains nudity (`isNudeContent: True/False`).
  - Whether the image contains adult text content (`isAdultContent: True/False`).
- The `text_image.py` script displays the processed image with detected text highlighted.

---

## Project Structure

```
nude-detect/
├── main.py         # Main script for nudity and adult content detection
├── text_image.py   # Script for text detection and visualization
├── images/         # Folder for sample images
├── requirements.txt # Dependencies
└── README.md       # Documentation
```

---

## Contribution

Feel free to fork this repository, make improvements, and create pull requests. Contributions are welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgments

- [NudeNet](https://github.com/notAI-tech/NudeNet) for its robust nudity detection capabilities.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for text detection.
- [Better Profanity](https://github.com/snguyenthanh/better_profanity) for profanity filtering.

---

## Disclaimer

This project is intended for ethical and responsible use. The developers are not responsible for any misuse of this tool.

