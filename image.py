import numpy as np
import torch
from PIL import Image, ImageEnhance, ImageFilter

from .utils import image_to_pillow, pillow_to_image


class VixImageFilters:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "brightness": (
                    "FLOAT",
                    {"default": 0.0, "min": -1.0, "max": 1.0, "step": 0.01},
                ),
                "contrast": (
                    "FLOAT",
                    {"default": 1.0, "min": -1.0, "max": 2.0, "step": 0.01},
                ),
                "saturation": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 5.0, "step": 0.01},
                ),
                "sharpness": (
                    "FLOAT",
                    {"default": 1.0, "min": -5.0, "max": 5.0, "step": 0.01},
                ),
                "blur": ("INT", {"default": 0, "min": 0, "max": 16, "step": 1}),
                "gaussian_blur": (
                    "FLOAT",
                    {"default": 0.0, "min": 0.0, "max": 1024.0, "step": 0.1},
                ),
                "edge_enhance": (
                    "FLOAT",
                    {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01},
                ),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Image"

    @classmethod
    def process_image(
        cls,
        img: torch.Tensor,
        brightness: float,
        contrast: float,
        saturation: float,
        sharpness: float,
        blur: int,
        gaussian_blur: float,
        edge_enhance: float,
        processing_list: bool = False,
    ) -> torch.Tensor:
        img = np.clip(img + brightness, 0.0, 1.0) if brightness != 0.0 else img
        img = np.clip(img * contrast, 0.0, 1.0) if contrast != 1.0 else img

        pil_image = None

        if saturation != 1.0:
            pil_image = ImageEnhance.Color(image_to_pillow(img)).enhance(saturation)

        if sharpness != 1.0:
            pil_image = ImageEnhance.Sharpness(pil_image or image_to_pillow(img)).enhance(sharpness)

        if blur > 0:
            pil_image = pil_image or image_to_pillow(img)
            for _ in range(blur):
                pil_image = pil_image.filter(ImageFilter.BLUR)

        if gaussian_blur > 0.0:
            pil_image = pil_image or image_to_pillow(img)
            pil_image = pil_image.filter(ImageFilter.GaussianBlur(radius=gaussian_blur))

        if edge_enhance > 0.0:
            pil_image = pil_image or image_to_pillow(img)
            edge_enhanced = pil_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
            mask = Image.new("L", pil_image.size, color=round(edge_enhance * 255))
            pil_image = Image.composite(edge_enhanced, pil_image, mask)

        return pillow_to_image(pil_image) if pil_image else (img.unsqueeze(0) if processing_list else img)

    def do_it(
        self,
        image: torch.Tensor | list[torch.Tensor],
        brightness: float,
        contrast: float,
        saturation: float,
        sharpness: float,
        blur: int,
        gaussian_blur: float,
        edge_enhance: float,
    ):
        if len(image) > 1:
            result = [
                self.process_image(
                    img,
                    brightness,
                    contrast,
                    saturation,
                    sharpness,
                    blur,
                    gaussian_blur,
                    edge_enhance,
                    processing_list=True,
                )
                for img in image
            ]
            return (torch.cat(result, dim=0),)
        return (
            self.process_image(
                image,
                brightness,
                contrast,
                saturation,
                sharpness,
                blur,
                gaussian_blur,
                edge_enhance,
            ),
        )
