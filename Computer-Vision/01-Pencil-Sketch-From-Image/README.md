# Project: Pencil sketch for given image

This is a fun project performed using OpenCV library.  
We apply various OpenCV operations to get pencil sketch of the given RGB image.

## Run the project

### To display the pencil sketch of the image

```shell
python main.py -i Data/Input/Sample_01.jpg
```

### To display and store the pencil sketch of the image

```shell
python main.py -i Data/Input/Sample_01.jpg -o Data/Output/Out_Sample_01.jpg
```

## Steps

1. Load image as BGR channel image
2. Convert to gray-scale image
3. Apply Gaussian blur on grayscale image
4. Invert the image
5. Detect edges for blurred grayscale image and inverted image
6. Merge both the images with equal weights
7. Display the result
8. If store required, then write the result into provided filename.

# Results

## Input

![Input image](Data/Input/Sample_01.jpg)

## Output

![Output result](Data/Output/Out_Sample_01.jpg)
