from PIL import Image

ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#FUNCS
def resize(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)


def gray(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    

def pixtoasc(image):
    pixels = image.getdata()
    characters = "".join([ascii_chars[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=100):
    try:
        #Change img to what you want here#
        target = 'nba.png'
        image = PIL.Image.open(target)
    except:
        print(target, 'is not a valid path. Try again')
        return
  
       
    new_img_data = pixtoasc(gray(resize(image)))
    
    
    pixel_count = len(new_img_data)  
    ascii_image = "\n".join([new_img_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    
    print(ascii_image)
    
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

main()
