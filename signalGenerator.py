from scipy import signal
import pylab as p
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from PIL import Image
import numpy as np
import random as rand
import cv2
import scipy.misc



t = np.arange(0., 4.*np.pi, 0.01)
f = np.zeros(t.size)

delta = 0.

for j in range(100):
    rand.seed()
    noise = rand.choice(np.arange(0.01, 0.02, 0.01))
    delta = rand.choice(np.arange(0.01, np.pi, 0.01))
    freq = rand.choice(np.arange(0.01, 5., 0.01))
    disturbance = np.zeros(t.size)

    for i in range(t.size):
        disturbance = rand.choice(np.arange(-1. * noise, noise, 0.01))
        f[i] = np.sin(freq * t[i] + delta) + disturbance

    #for i in range(t.size):
    #    disturbance = rand.choice(np.arange(-1. * noise, noise, 0.01))
    #    f[i] = signal.square(freq * t[i] + delta) + disturbance

    fig = plt.figure(figsize=(10, 10), dpi=40)
    plt.axis('off')
    plt.plot(f, 'k', linewidth=5)
    fig.savefig("signals/sin/" + str(j) + ".png")
    im = cv2.imread("signals/sin/" + str(j) + ".png", 0)
    #im = (im/256).astype('uint8')
    scipy.misc.toimage(im, cmin=0.0, cmax=...).save("signals/sin/" + str(j) + ".png")
