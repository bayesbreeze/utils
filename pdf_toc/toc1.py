import fitz

# Create a new PDF
doc = fitz.open("ff.pdf")

# ([\d\.]+.*?)[•\.\s]+(\d+)[.\n\s]*
# ['$1', $2],\n
ch1 = [
    ['1. Introduction to the Fourier Transform', 1],
    ['1.1 Introduction', 1],
    ['1.2 Basic Functions', 2],
    ['1.3 Sines, Cosines and Composite waves', 3],
    ['1.4 Orthogonality', 4],
    ['1.5 Waves in time and space', 7],
    ['1.6 Complex numbers. A Mathematical Tool', 7],
    ['1.7 The Fourier transform', 11],
    ['1.8 Fourier transforms in the physical world: The Lens as an FT computer', 16],
    ['1.9 Blurring and convolution', 19],
    ['1.9.1 Blurring', 19],
    ['1.9.2 Convolution', 20],
    ['1.10 The "Point" or "Impulse" response function', 22],
    ['1.11 Band-limited functions', 23],
    ['1.12 Summary', 23],
    ['1.13 Bibliography', 24],
]

ch2 = [
    ['2. The 1-D Fourier Transform', 25],
    ['2.1 Introduction', 25],
    ['2.2 Re-visiting the Fourier transform', 29],
    ['2.3 The Sampling Theorem', 35],
    ['2.4 Aliasing', 36],
    ['2.5 Convolution', 38],
    ['2.6 Digital Filtering', 41],
    ['2.7 The Power Spectrum', 43],
    ['2.8 Deconvolution', 47],
    ['2.9 System Identification', 49],
    ['2.10 Summary', 51],
    ['2.11 Bibliography', 52],
]
ch3 = [
    ['3. The 2-D Fourier Transform', 53],
    ['3.1 Introduction', 53],
    ['3.2 Linear space-invariant systems in two dimensions', 54],
    ['3.3 Ideal systems', 56],
    ['3.4 A simple X-ray imaging system', 59],
    ['3.5 Modulation Transfer Function (MTF)', 65],
    ['3.6 Image processing', 70],
    ['3.7 Tomography', 73],
    ['3.8 Computed Tomography', 78],
    ['3.9 Summary', 87],
    ['3.10 Bibliography', 88],
]

# ([\d\.]+.*?)[•\.\s]+(\d+)[.\n\s]*
# ['$1', $2],\n
ch4 = [
 ['4. The Fourier Transform in Magnetic Resonance Imaging', 89],
 ['4.1 Introduction', 89],
 ['4.2 The 2-D Fourier transform', 91],
 ['4.3 Magnetic Resonance Imaging', 91],
['4.3.1 Nuclear Magnetic Resonance', 91],
 ['4.3.2 Excitation, Evolution, and Detection', 95],
 ['4.3.3 The Received Signal: FIDs and Echos', 97],
 ['4.4 MRI', 98],
 ['4.4.1 Localization: Magnetic Field Gradients', 98],
 ['4.4.2 The MRI Signal Equation', 100],
 ['4.4.3 2-D Spin-Warp Imaging', 103],
 ['4.4.4 Fourier Sampling: Resolution, Field-of-View, and Aliasing', 106],
 ['4.4.5 2-D Multi-slice and 3-D Spin Warp Imaging', 109],
 ['4.4.6 Alternate k-space Sampling Strategies', 113],
 ['4.5 Magnetic Resonance Spectroscopic Imaging', 118],
 ['4.6 Motion in MRI', 123],
 ['4.7 Conclusion', 127],
 ['4.8 Bibliography', 128],
]

ch5 = [
    ["5. The Wavelet Transform", 129],
    ["5.1 Introduction", 129],
    ["5.2 Time-Frequencyanalysis", 131],
        ['5.2.1 Generalities', 131],
        ['5.2.2. How does time-frequency analysis work?', 133],
        ['5.2.3 Windowed Fourier transform', 135],
        ['5.2.4 Wavelet transform', 140],
        ["5.3 Multiresolution Analysis", 143],
        ['5.3.1 Scaling Functions', 144],
        ['5.3.2 Definition', 148],
        ['5.3.3 Scaling Relation', 151],
        ['5.3.4 Relationship of mu1tiresolution analysis to wavelets', 154],
        ['5.3.5 Multiresolution signal decomposition', 158],
        ['5.3.6 Digital filter interpretation', 160],
        ['5.3.7 Fast Wavelet Transform Algorithm', 164],
        ['5.3.8 Multidimensional Wavelet Transforms', 164],
        ['5.3.9 Fourier vs. Wavelet Digital Signal Processing', 169],
    ["5.4 Applications", 171],
         ['5.4.1 Image Compression', 171],
        ['5.4.2 Irregular heart beat detection from EKG signals', 172],
    ["5.5 Summary", 173],
]

ch6 = [
    ["6. The Discrete Fourier Transform and Fast Fourier Transform", 174],
    ['6.1 Introduction', 174],
    ['6.2 From Continuous to Discrete', 174],
     ['6.2.1 The comb function', 175],
 ['6.2.2 Sampling', 177],
 ['6.2.3 Interpreting DFT data in a cyclic buffer', 179],
 ['6.3 The Discrete Fourier Transform', 180],
 ['6.4 The Fast Fourier Transform', 182],
  ['6.4.1 The DFT as a matrix equation', 184],
 ['6.4.2 Simplifying the transition matrix', 184],
 ['6.4.3 Signal-flow-graph notation', 186],
 ['6.4.4 The DFT expressed as a signal flow graph', 186],
 ['6.4.5 Speed advantages o f the F F T', 187],
  ['6.5 Caveats to using the DFT/FFT', 189],
 ['6.6 Conclusion', 193],
 ['6.7 Bibliography', 193],
]

genLevel = lambda title: title.split(' ')[0][:-1].count('.') + 1

offset = 17
toc = ch1 + ch2 + ch3 + ch4 + ch5 + ch6
toc_with_offset = [[1, "Contents", 5]] +  [[genLevel(title), title, page + offset] for title, page in toc]

print(toc_with_offset)

doc.set_toc(toc_with_offset)

# Save the document
doc.save("ff_saved.pdf")
doc.close()
