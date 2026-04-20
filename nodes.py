import secrets


INT_MIN = -2147483648
INT_MAX = 2147483647


class EqualRandomInteger:
    """Return one uniformly selected integer from an inclusive range."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "minimum": (
                    "INT",
                    {
                        "default": 0,
                        "min": INT_MIN,
                        "max": INT_MAX,
                        "step": 1,
                        "display": "number",
                    },
                ),
                "maximum": (
                    "INT",
                    {
                        "default": 5,
                        "min": INT_MIN,
                        "max": INT_MAX,
                        "step": 1,
                        "display": "number",
                    },
                ),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("value",)
    FUNCTION = "generate"
    CATEGORY = "jieidan/random"
    SEARCH_ALIASES = ["random integer", "equal random", "uniform random"]

    @classmethod
    def VALIDATE_INPUTS(cls, minimum, maximum):
        if minimum > maximum:
            return "minimum must be less than or equal to maximum."
        return True

    @classmethod
    def IS_CHANGED(cls, minimum, maximum):
        return float("NaN")

    def generate(self, minimum, maximum):
        if minimum > maximum:
            raise ValueError("minimum must be less than or equal to maximum.")

        span = maximum - minimum + 1
        value = minimum + secrets.randbelow(span)
        return (value,)


NODE_CLASS_MAPPINGS = {
    "JieidanEqualRandomInteger": EqualRandomInteger,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JieidanEqualRandomInteger": "Equal Random Integer",
}
