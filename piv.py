# import the standard numerical and plotting packages
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread

# load the images
a = imread("B005_1.tif")
b = imread("B005_2.tif")

fig, axs = plt.subplots(1, 2, figsize=(9, 4))
axs[0].imshow(a, cmap=plt.cm.gray)
axs[1].imshow(b, cmap=plt.cm.gray)
plt.show()

# top left windows from each image
win_size = 32

a_win = a[:win_size, :win_size].copy()
b_win = b[:win_size, :win_size].copy()

fig, axs = plt.subplots(1, 2, figsize=(9, 4))
axs[0].imshow(a_win, cmap=plt.cm.gray)
axs[1].imshow(b_win, cmap=plt.cm.gray)
plt.show()

# shifting interrogation windows
fig = plt.imshow(b_win-a_win, cmap=plt.cm.gray)
plt.title("Without shift")
plt.show()

plt.imshow(b_win - np.roll(a_win, (1, 0), axis=(0, 1)), cmap=plt.cm.gray)
plt.title("Difference when A hasbeen shifted by 1 pixel")
plt.show()

# find the best shift algorithmically: shift and calculate the sum of squared differences. The minimum is the best
def match_template(img, template, maxroll=8):
	best_dist = np.inf
	best_shift = (-1, -1)
	for y in range(maxroll):
		for x in range(maxroll):
			# calculate Euclidean distance
			dist = np.sqrt(np.sum((img - np.roll(template, (x, y), axis=(0, 1))) ** 2))
			if dist < best_dist:
				best_dist = dist
				best_shift = (y, x)
	return (best_dist, best_shift)

# test that it works by manually rolling (shifting circurlary) the same image
output = match_template(np.roll(a_win, (2, 0), axis=(0, 1)), a_win)
print(output)
