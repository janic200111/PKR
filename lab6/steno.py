from PIL import Image

img = Image.open("obrazek.jpg")

width, height = img.size

tekst ="Ala ma kota i psa"
bintekst=""
pom=[]
for i in tekst:
    p=ord(i)
    p=bin(p)[2:]
    while len(p)!=8:
        p='0'+p
    bintekst+=p

j=0
pixel_list = list(img.getdata())
for i in range (len(pixel_list)):
    if j>=len(bintekst):
        break
    pom = (pixel_list[i][0] >> 1) << 1 | int(bintekst[j])
    pixel_list[i]=(pom,pixel_list[i][1],pixel_list[i][2])
    j+=1

img.putdata(pixel_list)
img.save("encoded_image.png")

pixel_list = list(img.getdata())
dl=0
decode=""
buf=""
for pixel in pixel_list:
    lsb_value = bin(pixel[0])[-1]
    buf+=lsb_value
    dl+=1
    if dl==8:
        dec = int(buf,2)
        decode+=chr(dec)
        buf=""
        dl=0
print(decode)


