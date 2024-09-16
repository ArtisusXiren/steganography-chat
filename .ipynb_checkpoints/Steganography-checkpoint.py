#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pillow


# In[1]:


from PIL import Image
def encode(message,img):
    img=Image.open(img)
    width,height=img.size
    encoded_image=img.copy()
    message += '\x00'
    message_bits=''.join([format(ord(char),'08b') for char in message])
    index=0
    for x in range (height):
        for y in range (width):
            pixels=list(img.getpixel((y,x)))
            for i in range(3):
                if index<len(message_bits):
                    pixels[i]=pixels[i]& ~1| int(message_bits[index])
                    index+=1
            encoded_image.putpixel((y,x),tuple(pixels))
            if index>=len(message_bits):
                break
        if index>=len(message_bits):
            break
    encoded_image.save(output_path)
    return encoded_image


# In[2]:


def decode(image):
    img=Image.open(image)
    width,height=img.size
    message_bits=[]
    for x in range(height):
        for y in range(width):
            pixels=list(img.getpixel((y,x)))
            for i in range(3):
                message_bits.append(pixels[i] & 1)
    message_bits=''.join(map(str,message_bits))            
    message_bytes=[message_bits[i:i+8] for i in range(0,len(message_bits),8)]
    message=''.join([chr(int(m,2)) for m in message_bytes])
    message = message.split('\x00', 1)[0]
    return message
output_path=(r"C:\Users\ArtisusXiren\Pictures\encoded_img.png")
text=decode(output_path)
print(text)


# In[ ]:




