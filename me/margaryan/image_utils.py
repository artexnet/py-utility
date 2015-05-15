__author__ = 'arthur'

from PIL import Image


IMAGE_EXTENSIONS = ['.JPG', '.JPEG', '.PNG', '.GIF', '.BMP']


# checks if provided file has an image extension
def is_image(filename):
    if str(filename).__len__() < 5 or '.' not in filename:
        return False
    ext = get_extension(filename).upper()
    for e in IMAGE_EXTENSIONS:
        if e == ext:
            return True
    return False


# returns extension of provided filename
def get_extension(img_file):
    return img_file[img_file.rfind('.'):]


# returns the name of provided filename without extension
def get_file_name(img_file):
    return img_file[:img_file.rfind('.')]


# auto-rotates provided file based on EXIF orientation information
def autorotate(img_file):
    image = Image.open(img_file)
    exif = image._getexif()
    if not exif:
        return False

    orientation_key = 274  # cf ExifTags
    if orientation_key in exif:
        orientation = exif[orientation_key]

        rotate_values = {
            3: 180,
            6: 270,
            8: 90
        }

        if orientation in rotate_values:
            # rotating and saving the picture
            image = image.rotate(rotate_values[orientation])
            image.save(img_file, quality=100)
            return True
    return False


# returns the string title of provided image orientation ['portrait', 'landscape']
def get_orientation(img_file):
    image = Image.open(img_file)
    return 'landscape' if image.size[0] > image.size[1] else 'portrait'


# resizes provided image file
def resize(img_file, width, height, result_file=None):
    if is_image(img_file):
        size = width, height
        try:
            im = Image.open(img_file)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(result_file) if result_file else im.save(img_file)
            return True
        except IOError:
            print "unable to resize image '%s'" % img_file
    return False


# crops provided image file to specified size
def crop(img_file, width, height, result_file=None, x_point=0, y_point=0):
    if is_image(img_file):
        try:
            im = Image.open(img_file)
            # exiting if provided dimensions are greater then original image size
            if im.size[0] < width or im.size[1] < height:
                return False

            # defining cropping area
            w = im.size[0]
            h = im.size[1]
            x = (w - width) / 2 if x_point == 0 else x_point
            y = (h - height) / 2 if y_point == 0 else y_point

            # cropping image
            box = (x, y, width + x, height + y)
            im = im.crop(box)

            # saving cropped image
            im.save(result_file) if result_file else im.save(img_file)
            return True
        except IOError:
            print "unable to crop image '%s'" % img_file
    return False


# best adopts the provided image to specified dimension
def adopt_to_dimension(img_file, width, height, result_file=None):
    if is_image(img_file):
        try:
            im = Image.open(img_file)
            # exiting if provided dimensions are greater then original image size
            if im.size[0] < width or im.size[1] < height:
                return False

            # calculating source image ratios
            width_ratio = im.size[0] / float(width)
            height_ratio = im.size[1] / float(height)

            # resizing the image if the width/height ratio is equal
            if width_ratio == height_ratio:
                return resize(img_file, width, height, result_file)

            # calculating target image dimensions
            if width_ratio > height_ratio:
                point = (im.size[0] - im.size[1] * float(width) / float(height)) / float(2)
                target_width = im.size[0] - point * float(2)
                box = (int(point), 0, int(target_width) + int(point), im.size[1])
            else:
                point = (im.size[1] - im.size[0] * float(height) / float(width)) / float(2)
                target_height = im.size[1] - point * float(2)
                box = (0, int(point), im.size[0], int(target_height) + int(point))

            # scaling and cropping/resizing the image
            im = im.crop(box)
            im.resize((width, height), Image.ANTIALIAS)

            # saving generated image
            im.save(result_file) if result_file else im.save(img_file)
            return True
        except IOError:
            print "unable to scale and resize image '%s'" % img_file
    return False