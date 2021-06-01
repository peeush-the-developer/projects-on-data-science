# Usage
# python main.py -i Data/Input/Sample_01.jpg
# python main.py -i Data/Input/Sample_01.jpg -o Data/Output/Out_Sample_01.jpg

# Import libraries
import cv2
import argparse
import imutils

# Add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
                required=True, help="Input image path")
ap.add_argument("-o", "--output", type=str, required=False,
                help="Path to output folder")
args = vars(ap.parse_args())


def apply_sobel(image):
    '''
    Apply Sobel kernel on the image

    Arguments:
        image: An numpy.ndarray image

    Returns:
        result: A sobeled (or edge) image
    '''
    # Detect horizontal edges
    sobel_x = cv2.Sobel(image, ddepth=cv2.CV_8U, dx=0, dy=1, ksize=3)
    # Detect vertical edges
    sobel_y = cv2.Sobel(image, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=3)

    # Apply bitwise or to have both types of edges in the image
    return cv2.bitwise_or(sobel_x, sobel_y)


def sketch_pencil(image, verbose=False):
    '''
    Create a pencil sketch from the image

    Arguments:
        image: An numpy.ndarray image (BGR channel)

    Returns:
        result: Pencil sketch from the input image
    '''
    # Get original shape and resize to height=400
    orig = image.copy()
    _, orig_h, orig_w = orig.shape
    image = imutils.resize(image, height=400)

    # Convert the input image to gray scale image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove any noise using a 3x3 gaussian filter
    image = cv2.GaussianBlur(image, ksize=(3, 3), sigmaX=0)
    # image = cv2.bilateralFilter(image, d=11, sigmaColor=21, sigmaSpace=7)

    if verbose:
        cv2.imshow("Blurred", image)
        cv2.waitKey(0)

    # Create a negative image
    image_neg = 255 - image

    if verbose:
        cv2.imshow("Blurred (inv)", image_neg)
        cv2.waitKey(0)

    # Detect the edges from both image & its negative using Sobel
    edges_image = apply_sobel(image)
    edges_image_inv = apply_sobel(image_neg)

    if verbose:
        cv2.imshow("Edges (sobel)", edges_image)
        cv2.waitKey(0)
        cv2.imshow("Edges (inv) (sobel)", edges_image_inv)
        cv2.waitKey(0)

    # Merge these two edge images with equal weights
    edges = cv2.addWeighted(edges_image, 1, edges_image_inv, 1, gamma=0)

    # Invert the blended image to get black sketch on white background
    edges_inv = 255 - edges

    if verbose:
        cv2.imshow("Edges", edges)
        cv2.imshow("Edges (inv)", edges_inv)
        cv2.waitKey(0)

    # Return the edges_inv
    return imutils.resize(edges_inv.copy(), height=orig_h)


# Load the image
image = cv2.imread(args["input"])
# Display original
cv2.imshow("Original", image)
# Apply operations to fetch Pencil sketch
sketch = sketch_pencil(image, verbose=False)
# Display the result
cv2.imshow("Sketch", sketch)

# Wait for key press.
cv2.waitKey(0)
# Close all opencv windows
cv2.destroyAllWindows()

# Save the output sketch file if required.
if args.get("output", None) is not None:
    cv2.imwrite(args["output"], sketch)
