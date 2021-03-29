import tensorflow as tf

IMG_HEIGHT = 256
IMG_WIDTH = 256
N_CHANNELS = 3

# randomly crop the image
def random_crop(image):
    return tf.image.random_crop(image, size=[IMG_HEIGHT, IMG_WIDTH, N_CHANNELS])

def normalize(image):
    image = tf.cast(image, tf.float32)
    image /= 127.5
    return image - 1

def random_jitter(image, resize_zoom: float = 1.1):
    """
    resize_zoom => Increase the image size (that will go into the network)
    by resize_zoom (eg. 255 * 1.1) before randomly cropping it by the image size (eg. 255x255).
    """

    # Resize image if we're choosing to resize
    image = tf.image.resize(image, [int(IMG_HEIGHT*resize_zoom), int(
        IMG_WIDTH*resize_zoom)], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

    # Crop the image with the given height and width
    image = random_crop(image)
    image = tf.image.random_flip_left_right(image)
    return image

def preprocess_image(image, label, phase: "train/test"):
    if phase == "train":
        image = random_jitter(image)
    return normalize(image)
