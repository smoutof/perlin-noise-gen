import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np
from tqdm import tqdm

try:
    print("Best results come from a 1 : 1 aspect ratio.")
    x = int(input("Width in pixels: "))
    y = int(input("Height in pixels: "))
    input(f"Total pixels: {x * y}, enter to continue.")
except:
    print("Invalid integer!")
    input()
    exit()

noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)

xpix, ypix = x, y
pic = np.zeros((xpix, ypix))

for i in tqdm(range(xpix), desc="Generating Perlin Noise"):
    for j in range(ypix):
        noise_val = noise1([i / xpix, j / ypix])
        noise_val += 0.5 * noise2([i / xpix, j / ypix])
        noise_val += 0.25 * noise3([i / xpix, j / ypix])
        noise_val += 0.125 * noise4([i / xpix, j / ypix])

        pic[i, j] = noise_val

plt.imshow(pic, cmap='gray')
plt.show()
