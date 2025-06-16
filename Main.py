import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Simplified gas reference (wavelengths in nm)
gas_reference = {
    'Hydrogen': [656, 486, 434],
    'Helium': [587, 447, 502],
    'Oxygen': [495, 500, 630],
    'Sodium': [589],
    'Nitrogen': [658, 654]
} 

# Approximate RGB to wavelength mapping
# This is rough but good enough for fun and educational purposes
rgb_to_wavelength = {
    'R': (620, 750),
    'G': (495, 570),
    'B': (450, 495)
}

def extract_rgb_spectrum(image_path):
    img = Image.open(image_path)
    img = img.resize((500, 500)) #Resize consistency
    data = np.array(img)

    r_mean = np.mean(data[:, :, 0])
    g_mean = np.mean(data[:, :, 1])
    b_mean = np.mean(data[:, :, 2])

    spectrum = {'R': r_mean, 'G': g_mean, 'B': b_mean}
    return spectrum

def estimate_wavelength_peaks(spectrum):
    wavelengths = []
    for color, intensity in spectrum.items():
        min_w, max_w = rgb_to_wavelength[color]
        peak = min_w + (max_w - min_w) * (intensity / 255)
        wavelengths.append(peak)
    return wavelengths

def match_gases(wavelength_peaks):
    detected = []
    for gas, lines in gas_reference.items():
        for ref_line in lines:
            for peak in wavelength_peaks:
                if abs(ref_line - peak) < 20: # rough tolerance
                    detected.append(gas)
                    break
    return set(detected)

def plot_spectrum(spectrum, output_path):
    colors = ['Red', 'Green', 'Blue']
    values = [spectrum['R'], spectrum['G'], spectrum['B']]

    plt.bar(colors, values, color=['red', 'green', 'blue'])
    plt.title('Extracted RGB Spectrum')
    plt.ylabel('Intensity')
    plt.savefig(output_path)
    plt.close()

def main():
    image_path = 'sample_images/sample_galaxy.jpg' #Test Image
    output_path = 'output/spectrum_results.png'

    spectrum = extract_rgb_spectrum(image_path)
    plot_spectrum(spectrum, output_path)

    wavelength_peaks = estimate_wavelength_peaks(spectrum)
    detected_gases = match_gases(wavelength_peaks)
    
    print("Detected Gases:", detected_gases)

if __name__ == '__main__':
    main()    