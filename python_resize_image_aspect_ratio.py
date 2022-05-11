from PIL import Image

src_img = 'test_images/unbiased-coder-logo.png'
dst_img = 'test_images/unbiased-coder-logo-half.png'

print (f'Using source image: {src_img}')

with Image.open(src_img) as im:
    print (f'Found image width: {im.width} and height: {im.height}')

    new_width = im.width // 2
    new_height = im.height // 2

    print (f'Using new image width: {new_width} and height: {new_height}')

    im_resized = im.resize((new_width, new_height))
    im_resized.save(dst_img, 'png')

print (f'Saved half resized image: {dst_img}')
