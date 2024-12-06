from PIL import Image, ImageDraw

# Create a blank image with white background
width, height = 400, 500
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw the Iron Man helmet shape
helmet_color = (204, 0, 0)  # Iron Man's red color
draw.polygon([(150, 100), (250, 100), (300, 200), (300, 350), 
              (100, 350), (100, 200)], fill=helmet_color, outline='black')

# Draw the eyes
eye_color = (255, 255, 255)  # White color for the eyes
draw.polygon([(160, 160), (180, 160), (180, 200), (160, 200)], fill=eye_color, outline='black')
draw.polygon([(220, 160), (240, 160), (240, 200), (220, 200)], fill=eye_color, outline='black')

# Draw the mouth
mouth_color = (255, 255, 255)  # White color for the mouth
draw.polygon([(160, 270), (240, 270), (240, 290), (160, 290)], fill=mouth_color, outline='black')

# Draw the lines on the helmet
draw.line([(160, 100), (160, 200)], fill='black', width=3)
draw.line([(240, 100), (240, 200)], fill='black', width=3)
draw.line([(100, 200), (300, 200)], fill='black', width=3)

# Save the image
image.save('iron_man_helmet.png')
image.show()
