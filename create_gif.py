import imageio.v3 as iio
filenames = ['jack_image1.png', 'jack_image2.png', 'jack_image3.png']
images = []
for filename in filenames :
    images.append(iio.imread(filename)[:, :, :3])
iio.imwrite('team.gif', images, duration = 500, loop = 0)     