from PIL import Image, ImageEnhance, ImageFilter
import os 

path = './imgs'
pathOut = './enhancedimages' 

for filename in os.listdir(path) : 
    img = Image.open(f"{path}/{filename}")

    #sharpness
    img.filter(ImageFilter.SHARPEN)

    #for saturation color 
    color = ImageEnhance.Contrast(img)
    img = color.enhance(1.2)

    # brightness 
    brightness = ImageEnhance.Brightness(img)
    img = brightness.enhance(1.1)

    #sharpness
    sharpness = ImageEnhance.Sharpness(img)
    img = sharpness.enhance(1.1)

    clean_name = os.path.splitext(filename)[0]

    img.save(f"{pathOut}/{clean_name}_enhanced.jpg", quality=95)




