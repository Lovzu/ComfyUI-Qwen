class Qwen3:
    @classmethod
    def INPUT_TYPES(cls):
        model_name = ['Qwen/Qwen3-4B-Instruct-2507']
        return {
            "required": {
                "model_name": (model_name, ),
                "max_tokens": ("INT", {"default": 16384, "min": 1024, "max": 81234, "step": 1}),
                "text_input": ("STRING", {"default": "", "multiline": True}),
            }
        }
    RETURN_TYPES = ("STRING", )
    FUNCTION = 'use_qwen'
    CATEGORY = "GPT_QWEN/Qwen"
    
    def use_qwen(self, model_name, max_tokens, text_input):
        from .qwen import get_request
        content = get_request(model_name, max_tokens, text_input)
        return (content, )


NODE_CLASS_MAPPINGS = {
    "Qwen": Qwen3,
     
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Qwen": "Qwen GPT",
}