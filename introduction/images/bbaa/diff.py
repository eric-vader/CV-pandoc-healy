import cv2
from skimage.metrics import structural_similarity
import numpy as np

attacked = cv2.imread(r'tile2_nnlayers.png', 0)
original = cv2.imread(r'noattack_nnlayers.png', 0)

# sub = cv2.subtract(attacked, original)
# Compute SSIM between the two images
# diff contains the actual image differences between the two images
(score, diff) = structural_similarity(attacked, original, full=True)
diff = 255 - (diff * 255).astype("uint8")
print("Image Similarity: {:.4f}%".format(score * 100))

# Search for all pixels that are different 
# Type is <class 'numpy.ndarray'>, you can optionally convert to a list
coords = np.argwhere(diff > 0)
# coords = coords.tolist() 
print(coords)

cv2.imwrite('diff.png', diff)