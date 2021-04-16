# Color-palette
Color palette is a program that can be used to detect dominant colors in a painting or a picture and build a color palette from it. Program uses k-means clustering to identify major colors in all the pixels present in the image.

---

## Requirments-
    Python >=3.6 
    PILLOW == 8.1.0
    matploitlib == 3.3.4
    scipy == 1.6.2
    pandas = 1.2.3
	
 ---
 
## Input-
    Program will take two inputs, 
    First is the path of the image and second is the number of colors to detect in the image.

   ![](https://github.com/Micky659/Color-palette/blob/master/Stock/Raja_Ravi_Varma's_Galaxy_of_Musicians.jpg)

#### Example-
 Enter image location: **Stock/Raja_Ravi_Varma's_Galaxy_of_Musicians.jpg**
 
 Enter number of colors in palette: **10**
  
  ---
   
## Output-
    The program will create two images of the same extension as the input image,
    
    The first image is the palette of dominant colors and
   ![](https://github.com/Micky659/Color-palette/blob/master/Output/Palette%20of%20Raja_Ravi_Varma's_Galaxy_of_Musicians.jpg)
   
    the second image is the combined image of the input and palette.
    
   ![](https://github.com/Micky659/Color-palette/blob/master/Output/Raja_Ravi_Varma's_Galaxy_of_Musicians%20with%20palette.jpg)
   
   ***Be my guest to build over my code and use it wisely***
