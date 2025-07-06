import ast
import re


class VixMultilineText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": (
                    "STRING",
                    {"default": "", "multiline": True, "dynamicPrompts": False},
                ),
            },
            "optional": {},
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Text"
    DEPRECATED = True

    @classmethod
    def do_it(cls, text, **kwargs) -> tuple:
        return (text,)


class VixTextConcatenate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "delimiter": ("STRING", {"default": ", "}),
                "clean_whitespace": (["true", "false"],),
            },
            "optional": {
                "text_a": ("STRING", {"forceInput": True}),
                "text_b": ("STRING", {"forceInput": True}),
                "text_c": ("STRING", {"forceInput": True}),
                "text_d": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Text"
    DEPRECATED = True

    @classmethod
    def do_it(cls, delimiter: str, clean_whitespace: str, **kwargs):
        delim = "\n" if delimiter == "\\n" else delimiter
        strip = clean_whitespace.lower() == "true"
        parts = ((val.strip() if strip else val) for _, val in sorted(kwargs.items()) if isinstance(val, str))
        return (delim.join(filter(None, parts)),)


class VixTextReplace:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "find": ("STRING", {"default": "", "multiline": False}),
                "replace": ("STRING", {"default": "", "multiline": False}),
            },
            "optional": {},
        }

    RETURN_TYPES = ("STRING", "NUMBER", "FLOAT", "INT")
    RETURN_NAMES = (
        "result_text",
        "replacement_count_number",
        "replacement_count_float",
        "replacement_count_int",
    )
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Text"
    DEPRECATED = True

    @classmethod
    def do_it(cls, text: str, find: str, replace: str):
        modified_text, count = re.subn(find, replace, text)
        return modified_text, count, float(count), count


class VixDictionaryNew:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key_1": ("STRING", {"default": "", "multiline": False}),
                "value_1": ("STRING", {"default": "", "multiline": False}),
            },
            "optional": {
                "key_2": ("STRING", {"default": "", "multiline": False}),
                "value_2": ("STRING", {"default": "", "multiline": False}),
                "key_3": ("STRING", {"default": "", "multiline": False}),
                "value_3": ("STRING", {"default": "", "multiline": False}),
                "key_4": ("STRING", {"default": "", "multiline": False}),
                "value_4": ("STRING", {"default": "", "multiline": False}),
                "key_5": ("STRING", {"default": "", "multiline": False}),
                "value_5": ("STRING", {"default": "", "multiline": False}),
                "key_6": ("STRING", {"default": "", "multiline": False}),
                "value_6": ("STRING", {"default": "", "multiline": False}),
                "key_7": ("STRING", {"default": "", "multiline": False}),
                "value_7": ("STRING", {"default": "", "multiline": False}),
                "key_8": ("STRING", {"default": "", "multiline": False}),
                "value_8": ("STRING", {"default": "", "multiline": False}),
                "key_9": ("STRING", {"default": "", "multiline": False}),
                "value_9": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Text"

    @classmethod
    def do_it(
        cls,
        key_1: str,
        value_1: str,
        key_2: str,
        value_2: str,
        key_3: str,
        value_3: str,
        key_4: str,
        value_4: str,
        key_5: str,
        value_5: str,
        key_6: str,
        value_6: str,
        key_7: str,
        value_7: str,
        key_8: str,
        value_8: str,
        key_9: str,
        value_9: str,
    ):
        return (
            {
                k: v
                for k, v in [
                    (key_1, value_1),
                    (key_2, value_2),
                    (key_3, value_3),
                    (key_4, value_4),
                    (key_5, value_5),
                    (key_6, value_6),
                    (key_7, value_7),
                    (key_8, value_8),
                    (key_9, value_9),
                ]
                if k
            },
        )


class VixDictionaryConvert:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"dictionary_text": ("STRING", {"forceInput": True})},
            "optional": {},
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Text"

    @classmethod
    def do_it(cls, dictionary_text: str):
        return (ast.literal_eval(dictionary_text),)


class VixDictionaryGet:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "dictionary": ("DICT",),
                "key": ("STRING", {"default": "", "multiline": False}),
            },
            "optional": {
                "default_value": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Text"

    @classmethod
    def do_it(cls, dictionary: dict, key: str, default_value=""):
        return (str(dictionary.get(key, default_value)),)


class VixDictionaryUpdate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "dict_1": ("DICT",),
                "dict_2": ("DICT",),
            },
            "optional": {
                "dict_3": ("DICT",),
                "dict_4": ("DICT",),
            },
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "do_it"
    CATEGORY = "Visionatrix/Text"

    @classmethod
    def do_it(cls, dict_1: dict, dict_2: dict, dict_3: dict | None = None, dict_4: dict | None = None):
        return ({**dict_1, **dict_2, **(dict_3 or {}), **(dict_4 or {})},)
