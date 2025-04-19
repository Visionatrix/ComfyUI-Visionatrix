import numpy as np
from PIL import Image
from torch import Tensor, from_numpy


def image_to_pillow(image: Tensor) -> Image.Image:
    return Image.fromarray(np.clip(255.0 * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def images_to_pillow(images: Tensor | list[Tensor]) -> list[Image.Image]:
    pillow_images = []
    for _bn, image in enumerate(images):
        pillow_images.append(image_to_pillow(image))
    return pillow_images


def pillow_to_image(image: Image.Image) -> Tensor:
    return from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
