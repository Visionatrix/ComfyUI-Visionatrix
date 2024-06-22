class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


any_typ = AnyType("*")


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
            },
            "optional": {
                "input_off_state": (any_typ,),
                "input_on_state": (any_typ,),
            }
        }

    RETURN_TYPES = (any_typ,)
    RETURN_NAMES = ("output_to",)
    CATEGORY = "Visionatrix/UI"
    FUNCTION = "do_it"

    @classmethod
    def do_it(cls, state, **kwargs):
        if state is False:
            return (kwargs["input_off_state"],)
        return (kwargs["input_on_state"],)


class VixUiRangeFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 4.0}),
                "display_name": ("STRING", {"default": "Display Range"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "min": ("FLOAT", {"default": 1.0}),
                "max": ("FLOAT", {"default": 9.0}),
                "step": ("FLOAT", {"default": 0.1}),
                "order": ("INT", {"default": 99}),
            },
        }

    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"
    RETURN_TYPES = ("FLOAT", )

    @classmethod
    def do_it(cls, value, **kwargs):
        return (value, )


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
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    @classmethod
    def do_it(cls, default_value, **kwargs):
        return (default_value, )


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
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    @classmethod
    def do_it(cls, text, **kwargs):
        return (text, )


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
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    @classmethod
    def do_it(cls, text, **kwargs):
        return (text, )


NODE_CLASS_MAPPINGS = {
    "VixUiCheckbox": VixUiCheckbox,
    "VixUiRangeFloat": VixUiRangeFloat,
    "VixUiList": VixUiList,
    "VixUiPrompt": VixUiPrompt,
    "VixUiWorkflowMetadata": VixUiWorkflowMetadata,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VixUiCheckbox": "VixUI-Checkbox",
    "VixUiRangeFloat": "VixUI-RangeFloat",
    "VixUiList": "VixUI-List",
    "VixUiPrompt": "VixUI-Prompt",
    "VixUiWorkflowMetadata": "VixUI-WorkflowMetadata",
}
