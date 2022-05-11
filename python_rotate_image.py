from PIL import Image

src_img = 'test_images/unbiased-coder-logo.png'
dst_img = 'test_images/unbiased-coder-logo-rotated.png'

print (f'Using source image: {src_img}')

with Image.open(src_img) as im:
    print (f'Rotating image by 45 degrees')

    im_rotated = im.rotate(angle=45)
    im_rotated.save(dst_img, 'png')

print (f'Saved rotated image: {dst_img}')
