import json


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
                "value": ("FLOAT", {"default": 4.0}),
                "display_name": ("STRING", {"default": "Display Range"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "min": ("FLOAT", {"default": 1.0}),
                "max": ("FLOAT", {"default": 9.0}),
                "step": ("FLOAT", {"default": 0.1}),
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
                "value": ("FLOAT", {"default": 4.0}),
                "display_name": ("STRING", {"default": "Image Size Factor"}),
                "optional": ("BOOLEAN", {"default": True}),
                "advanced": ("BOOLEAN", {"default": True}),
                "source_input_name": ("STRING", {"default": ""}),
                "min": ("FLOAT", {"default": 1.0}),
                "max": ("FLOAT", {"default": 9.0}),
                "step": ("FLOAT", {"default": 0.1}),
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
                "input_off_state": (any_typ,),
                "input_on_state": (any_typ,),
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
                "input_first": (any_typ,),
                "input_second": (any_typ,),
                "input_third": (any_typ,),
                "input_fourth": (any_typ,),
                "input_fifth": (any_typ,),
                "input_sixth": (any_typ,),
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
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/UI"

    @classmethod
    def do_it(cls, text, **kwargs) -> tuple:
        return (text,)


NODE_CLASS_MAPPINGS = {
    "VixUiCheckbox": VixUiCheckbox,
    "VixUiRangeFloat": VixUiRangeFloat,
    "VixUiRangeScaleFloat": VixUiRangeScaleFloat,
    "VixUiRangeInt": VixUiRangeInt,
    "VixUiList": VixUiList,
    "VixUiPrompt": VixUiPrompt,
    "VixUiCheckboxLogic": VixUiCheckboxLogic,
    "VixUiListLogic": VixUiListLogic,
    "VixUiWorkflowMetadata": VixUiWorkflowMetadata,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VixUiCheckbox": "VixUI-Checkbox",
    "VixUiRangeFloat": "VixUI-RangeFloat",
    "VixUiRangeScaleFloat": "VixUI-RangeScaleFloat",
    "VixUiRangeInt": "VixUI-RangeInt",
    "VixUiList": "VixUI-List",
    "VixUiPrompt": "VixUI-Prompt",
    "VixUiCheckboxLogic": "VixUI-CheckboxLogic",
    "VixUiListLogic": "VixUI-ListLogic",
    "VixUiWorkflowMetadata": "VixUI-WorkflowMetadata",
}
