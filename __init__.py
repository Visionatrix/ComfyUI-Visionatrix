import json


class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


any_typ = AnyType("*")


class VixUiAspectRatioSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "aspect_ratio": (
                    [
                        "1:1 (1024x1024)",
                        "2:3 (832x1216)",
                        "3:4 (896x1152)",
                        "5:8 (768x1216)",
                        "9:16 (768x1344)",
                        "9:19 (704x1472)",
                        "9:21 (640x1536)",
                        "3:2 (1216x832)",
                        "4:3 (1152x896)",
                        "8:5 (1216x768)",
                        "16:9 (1344x768)",
                        "19:9 (1472x704)",
                        "21:9 (1536x640)",
                    ],
                ),
                "display_name": ("STRING", {"default": "Aspect Ratio"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "order": ("INT", {"default": 20}),
                "custom_id": ("STRING", {"default": "aspect_ratio"}),
            },
            "optional": {
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("ratio", "width", "height")
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    def do_it(self, aspect_ratio, **kwargs):
        ratio, dims = aspect_ratio.split(" (")
        dims = dims[:-1]  # Remove the closing parenthesis
        width, height = map(int, dims.split("x"))
        return ratio, width, height


class VixUiCheckbox:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "state": ("BOOLEAN", {"default": False}),
                "display_name": ("STRING", {"default": "Display Name"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "order": ("INT", {"default": 99}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("BOOLEAN", "INT")
    RETURN_NAMES = ("bool", "int")
    CATEGORY = "Visionatrix/UI"
    FUNCTION = "do_it"

    @classmethod
    def do_it(cls, state, **kwargs) -> tuple:
        return state, int(state)


class VixUiRangeFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 4.0, "step": 0.01, "round": False}),
                "display_name": ("STRING", {"default": "Display Range"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "min": ("FLOAT", {"default": 1.0, "step": 0.01, "round": False}),
                "max": ("FLOAT", {"default": 9.0, "step": 0.01, "round": False}),
                "step": ("FLOAT", {"default": 0.1, "step": 0.01, "round": False}),
                "order": ("INT", {"default": 99}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }

    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"
    RETURN_TYPES = ("FLOAT",)

    @classmethod
    def do_it(cls, value, **kwargs) -> tuple:
        return (value,)


class VixUiRangeScaleFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 4.0, "step": 0.01, "round": False}),
                "display_name": ("STRING", {"default": "Image Size Factor"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "source_input_name": ("STRING", {"default": ""}),
                "min": ("FLOAT", {"default": 1.0, "step": 0.01, "round": False}),
                "max": ("FLOAT", {"default": 9.0, "step": 0.01, "round": False}),
                "step": ("FLOAT", {"default": 0.1, "step": 0.01, "round": False}),
                "order": ("INT", {"default": 99}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }

    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"
    RETURN_TYPES = ("FLOAT",)

    @classmethod
    def do_it(cls, value, **kwargs) -> tuple:
        return (value,)


class VixUiRangeInt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("INT", {"default": 10}),
                "display_name": ("STRING", {"default": "Display Range"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "min": ("INT", {"default": 1}),
                "max": ("INT", {"default": 20}),
                "step": ("INT", {"default": 1}),
                "order": ("INT", {"default": 99}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }

    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"
    RETURN_TYPES = ("INT",)

    @classmethod
    def do_it(cls, value, **kwargs) -> tuple:
        return (value,)


class VixUiList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "default_value": ("STRING", {}),
                "possible_values": ("STRING", {"default": "[]", "multiline": True}),
                "display_name": ("STRING", {"default": "Dropdown list"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "order": ("INT", {"default": 99}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = (any_typ,)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    @classmethod
    def do_it(cls, default_value, **kwargs) -> tuple:
        possible_values = json.loads(kwargs["possible_values"])
        if isinstance(possible_values, dict) and default_value in possible_values:
            return (possible_values[default_value],)
        return (default_value,)


class VixUiPrompt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True, "dynamicPrompts": True}),
                "display_name": ("STRING", {"default": "Prompt"}),
                "optional": ("BOOLEAN", {"default": False}),
                "advanced": ("BOOLEAN", {"default": False}),
                "order": ("INT", {"default": 10}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "hidden": ("BOOLEAN", {"default": False}),
                "translatable": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    @classmethod
    def do_it(cls, text, **kwargs) -> tuple:
        return (text,)


class VixUiCheckboxLogic:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "state": ("BOOLEAN", {"default": False}),
                "display_name": ("STRING", {"default": "Display Name"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "order": ("INT", {"default": 99}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "input_off_state": (any_typ, {"lazy": True}),
                "input_on_state": (any_typ, {"lazy": True}),
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ("output_to",)
    CATEGORY = "Visionatrix/UI"
    FUNCTION = "do_it"

    @classmethod
    def do_it(cls, state, **kwargs) -> tuple:
        if state is False:
            return (kwargs.get("input_off_state", None),)
        return (kwargs.get("input_on_state", None),)

    @staticmethod
    def check_lazy_status(state, **kwargs):
        if state is False:
            return ["input_off_state"]
        return ["input_on_state"]


class VixUiListLogic:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "default_value": ("STRING", {}),
                "possible_values": ("STRING", {"default": "[]", "multiline": True}),
                "display_name": ("STRING", {"default": "Display Name"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "order": ("INT", {"default": 99}),
                "custom_id": ("STRING", {"default": ""}),
            },
            "optional": {
                "input_first": (any_typ, {"lazy": True}),
                "input_second": (any_typ, {"lazy": True}),
                "input_third": (any_typ, {"lazy": True}),
                "input_fourth": (any_typ, {"lazy": True}),
                "input_fifth": (any_typ, {"lazy": True}),
                "input_sixth": (any_typ, {"lazy": True}),
                "hidden": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ("output_to",)
    CATEGORY = "Visionatrix/UI"
    FUNCTION = "do_it"

    @classmethod
    def do_it(cls, default_value, **kwargs) -> tuple:
        list_with_values: list = json.loads(kwargs["possible_values"])
        index_to_return = list_with_values.index(default_value)
        if index_to_return == 0:
            return (kwargs["input_first"],)
        if index_to_return == 1:
            return (kwargs["input_second"],)
        if index_to_return == 2:
            return (kwargs["input_third"],)
        if index_to_return == 3:
            return (kwargs["input_fourth"],)
        if index_to_return == 4:
            return (kwargs["input_fifth"],)
        if index_to_return == 5:
            return (kwargs["input_sixth"],)
        raise RuntimeError("Workflow logic error")

    @staticmethod
    def check_lazy_status(default_value, **kwargs):
        list_with_values: list = json.loads(kwargs["possible_values"])
        index_to_return = list_with_values.index(default_value)
        if index_to_return == 0:
            return ["input_first"]
        if index_to_return == 1:
            return ["input_second"]
        if index_to_return == 2:
            return ["input_third"]
        if index_to_return == 3:
            return ["input_fourth"]
        if index_to_return == 4:
            return ["input_fifth"]
        if index_to_return == 5:
            return ["input_sixth"]
        raise RuntimeError("Workflow logic error")


class VixUiWorkflowMetadata:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {}),
                "display_name": ("STRING", {}),
                "description": ("STRING", {"default": ""}),
                "author": ("STRING", {}),
                "homepage": ("STRING", {"default": ""}),
                "documentation": ("STRING", {"default": ""}),
                "license": ("STRING", {"default": ""}),
                "tags": ("STRING", {"default": "[\"general\"]", "multiline": True}),
                "version": ("STRING", {"default": "1.0.0"})
            },
            "optional": {
                "requires": ("STRING", {"default": "[]", "multiline": True}),
                "is_seed_supported": ("BOOLEAN", {"default": True}),
                "is_count_supported": ("BOOLEAN", {"default": True}),
                "is_translations_supported": ("BOOLEAN", {"default": False}),
                "is_macos_supported": ("BOOLEAN", {"default": True}),
                "required_memory_gb": ("FLOAT", {"default": 0.0, "step": 0.1, "round": False}),
                "hidden": ("BOOLEAN", {"default": False}),
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    @classmethod
    def do_it(cls, text, **kwargs) -> tuple:
        return (text,)


class VixDynamicLoraDefinition:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL", {"tooltip": "The diffusion model the LoRA will be applied to."}),
                "clip": ("CLIP", {"tooltip": "The CLIP model the LoRA will be applied to."}),
                "base_model_type": ("STRING", {"tooltip": "The base type of model in CivitAI format."}),
                "description": ("STRING", {"tooltip": "Brief explanation of LoRA functionality at the added place."}),
            },
        }

    RETURN_TYPES = ("MODEL", "CLIP")
    OUTPUT_TOOLTIPS = ("The modified diffusion model.", "The modified CLIP model.")
    CATEGORY = "Visionatrix/UI"
    FUNCTION = "do_it"
    DESCRIPTION = "Node that allows dynamic selection of any supported LoRAs from CivitAI in the Visionatrix UI."

    @classmethod
    def do_it(cls, model, clip, **kwargs) -> tuple:
        return model, clip


class VixCheckboxLogic:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "state": ("BOOLEAN", {"default": False}),
                "input_off_state": (any_typ, {"lazy": True}),
                "input_on_state": (any_typ, {"lazy": True}),
            },
            "optional": {},
        }

    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ("output_to",)
    CATEGORY = "Visionatrix/Logic"
    FUNCTION = "do_it"

    @classmethod
    def do_it(cls, state, **kwargs) -> tuple:
        if state is False:
            return (kwargs.get("input_off_state", None),)
        return (kwargs.get("input_on_state", None),)

    @staticmethod
    def check_lazy_status(state, **kwargs):
        if state is False:
            return ["input_off_state"]
        return ["input_on_state"]


NODE_CLASS_MAPPINGS = {
    "VixUiAspectRatioSelector": VixUiAspectRatioSelector,
    "VixUiCheckbox": VixUiCheckbox,
    "VixUiRangeFloat": VixUiRangeFloat,
    "VixUiRangeScaleFloat": VixUiRangeScaleFloat,
    "VixUiRangeInt": VixUiRangeInt,
    "VixUiList": VixUiList,
    "VixUiPrompt": VixUiPrompt,
    "VixUiCheckboxLogic": VixUiCheckboxLogic,
    "VixUiListLogic": VixUiListLogic,
    "VixUiWorkflowMetadata": VixUiWorkflowMetadata,
    "VixDynamicLoraDefinition": VixDynamicLoraDefinition,
    "VixCheckboxLogic": VixCheckboxLogic,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VixUiAspectRatioSelector": "VixUI-Aspect Ratio",
    "VixUiCheckbox": "VixUI-Checkbox",
    "VixUiRangeFloat": "VixUI-RangeFloat",
    "VixUiRangeScaleFloat": "VixUI-RangeScaleFloat",
    "VixUiRangeInt": "VixUI-RangeInt",
    "VixUiList": "VixUI-List",
    "VixUiPrompt": "VixUI-Prompt",
    "VixUiCheckboxLogic": "VixUI-CheckboxLogic",
    "VixUiListLogic": "VixUI-ListLogic",
    "VixUiWorkflowMetadata": "VixUI-WorkflowMetadata",
    "VixDynamicLoraDefinition": "Vix-DynamicLoraDefinition",
    "VixCheckboxLogic": "Vix-CheckboxLogic",
}
