# 🌌 Spectral Hacker v0.1

**Educational Spectroscopy Tool — Light Spectrum Analyzer for Space Photography**

---

## 🚀 What Is This?

Spectral Hacker is a simple but functional educational tool that analyzes light spectrum data from basic space photography to estimate gas composition.

This project is designed for hobbyists, families, students, or anyone curious about space — using only a regular photo and consumer-level hardware. It demonstrates basic spectral analysis principles using Python image processing.

---

## 🔬 What It Does

- ✅ Accepts space/star/telescope images.
- ✅ Extracts average RGB spectrum from the photo.
- ✅ Converts RGB values into approximate wavelength peaks.
- ✅ Matches detected wavelengths to known gas emission/absorption lines.
- ✅ Outputs rough gas composition estimates.
- ✅ Plots spectrum as a simple visual bar chart.

**Disclaimer:**  
⚠ Not laboratory-accurate spectroscopy.  
⚠ This is a hobbyist, educational proof-of-concept for basic physical modeling.

---

## ⚙ How To Run

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/Couchtr26/SpectralHacker.git
cd SpectralHacker
2️⃣ Install Requirements
Make sure you have Python 3 installed.

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Add Your Test Image
Place your space/star photo inside sample_images/ directory.

Rename your image as:

Copy
Edit
sample_galaxy.jpg
(future versions will support multiple uploads)

4️⃣ Run The Analyzer
bash
Copy
Edit
python main.py
The program will:

Output detected gases in your terminal.

Generate a spectrum graph in /output/spectrum_results.png.

🧰 Requirements
Python 3.x

Pillow

NumPy

Matplotlib

bash
Copy
Edit
pip install Pillow numpy matplotlib
🚧 Future Improvements
✅ Larger gas reference tables

✅ Redshift correction models

✅ Multi-frame averaging

✅ Mobile app version (eventually)

✅ Public web demo

🤝 Why I Built This
Because programming is my Rubik’s cube —
and physics is the source code of reality.

I wanted to build something people could play with, learn from, and say:

“Holy shit — that’s cool.”

Thomas (Grey Knight Software)
Copyright (c) 2025 Couchtr26