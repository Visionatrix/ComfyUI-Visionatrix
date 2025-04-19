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

    @classmethod
    def do_it(cls, text: str, find: str, replace: str):
        modified_text, count = re.subn(find, replace, text)
        return modified_text, count, float(count), count


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
