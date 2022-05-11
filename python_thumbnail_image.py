from PIL import Image

src_img = 'test_images/unbiased-coder-logo.png'
dst_img = 'test_images/unbiased-coder-logo-thumbnail.png'

print (f'Using source image: {src_img}')

with Image.open(src_img) as im:
    print (f'Found image width: {im.width} and height: {im.height}')

    new_width = 128
    new_height = 128

    print (f'Generating a 128x128 thumbnail')

    im_thumbnail = im.resize((new_width, new_height))
    im_thumbnail.save(dst_img, 'png')

print (f'Saved thumbnail image: {dst_img}')
