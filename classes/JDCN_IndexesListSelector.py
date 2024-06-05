import os

class JDCN_IndexesListSelector:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "PathList": ("STRING", {"forceInput": True}),
                "Indexes": ("STRING", {"forceInput": True}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, PathList, Indexes):

        indexes = [int(i) - 1 for i in Indexes[0].split(",") if i.isdigit()]
        indexes = sorted(set(indexes))  # remove duplicates and sort

        if len(PathList) == 0:
            print("Error in List Variable")
            return None

        selected_files = [PathList[i] for i in indexes if 0 <= i < len(PathList)]

        return (selected_files,)


N_CLASS_MAPPINGS = {
    "JDCN_IndexesListSelector": JDCN_IndexesListSelector,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_IndexesListSelector": "JDCN_IndexesListSelector",
}