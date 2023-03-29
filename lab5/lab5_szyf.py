from PIL import Image
import random
white=(255,255,255)
black=(0,0,0)
obrazek1=Image.new('RGB', (100, 200), color = 'white')
obrazek2=Image.new('RGB', (100, 200), color = 'white')

obrazek = Image.open('ludzik.png')
for i in range(100):
    for j in range(100):
        pixel=obrazek.getpixel((i,j))
        los=random.randint(0, 1)
        if pixel==white:
            if los==1:
                obrazek1.putpixel((i,2*j),black)
                obrazek1.putpixel((i,2*j+1),white)
                obrazek2.putpixel((i,2*j),black)
                obrazek2.putpixel((i,2*j+1),white)
            else:
                obrazek1.putpixel((i,2*j),white)
                obrazek1.putpixel((i,2*j+1),black)
                obrazek2.putpixel((i,2*j),white)
                obrazek2.putpixel((i,2*j+1),black)
        else:
            if los==1:
                obrazek1.putpixel((i,2*j),black)
                obrazek1.putpixel((i,2*j+1),white)
                obrazek2.putpixel((i,2*j),white)
                obrazek2.putpixel((i,2*j+1),black)
            else:
                obrazek1.putpixel((i,2*j),white)
                obrazek1.putpixel((i,2*j+1),black)
                obrazek2.putpixel((i,2*j),black)
                obrazek2.putpixel((i,2*j+1),white)
obrazek1.save('image1.png')
obrazek2.save('image2.png')


