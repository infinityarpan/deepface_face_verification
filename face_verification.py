import argparse
from deepface import DeepFace
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Defining the argument parser
parser = argparse.ArgumentParser(description="Path to the photos for comparing")
parser.add_argument("image_1", type=str, help="Path to the photo.")
parser.add_argument("image_2", type=str, help="Path to the photo.")
parser.add_argument("model", nargs='+', type=str, help="Specify the model to be used e.g ArcFace, DeepID, VGG-Face, etc.")
args = parser.parse_args()
# Taking the arguments
image_1 = args.image_1
image_2 = args.image_2
models = args.model
# Read the images with matplotlib. We could also use opencv.
img1 = mpimg.imread(image_1)
img2 = mpimg.imread(image_2)
# Drawing a white figure with vitually 2 rows and 2 columns and displaying a name over the figure
fig = plt.figure(figsize=[10,100])
fig.suptitle('Face Verification', fontsize=12, fontweight='bold')
rows = len(models) + 1
columns = 2
# Plotting the image
fig.add_subplot(rows, columns, 1)
plt.imshow(img1)
plt.axis('off')
plt.title('Image 1')
# Plotting the image
fig.add_subplot(rows, columns, 2)
plt.imshow(img2)
plt.axis('off')
plt.title('Image 2')
# Checking for a match
disp_row = 1
for model in models:
    disp_row = disp_row + 2
    result = DeepFace.verify(img1_path = image_1, img2_path = image_2, model_name = model)
    print(result)
    message = ''
    if result['verified']:
        message = 'Face matched! They both are the same person.'
    else :
        message = 'Oh no! Face didn\'t match'
# Plotting the result
    details = fig.add_subplot(rows, columns, disp_row)
    details.text(0.1, 0.9, message)
    details.text(0.1, 0.8, 'Model used: ' + result.get('model'))
    details.text(0.1, 0.7, 'similarity metric used: ' + result.get('similarity_metric'))
    details.text(0.1, 0.6, 'Cosine distance: %s'%result.get('distance'))
    details.text(0.1, 0.5, 'Threshold used: %s'%result.get('threshold'))
# plt.axis('off') is used to hide the axis scale
    plt.axis('off')
plt.show()