# Qwen3 Node for GPT_QWEN

This Python class defines a custom node `Qwen3` designed to integrate with a GPT-based system under the category `GPT_QWEN/Qwen`. It serves as an interface to interact with the Qwen language model, specifically the `"Qwen/Qwen3-4B-Instruct-2507"` variant.

---

## Description

- The `Qwen3` class exposes a method `use_qwen` which takes in the model name, a maximum token count, and a text input string.
- It uses an internal function `get_request` (imported from a local module `.qwen`) to send the input to the Qwen model and receive a response.
- The node is configured with input types, return types, and metadata for integration with a node-based system (e.g., a visual programming or AI workflow environment).

---

## Input Parameters

- **model_name** (string):  
  Allowed values: `["Qwen/Qwen3-4B-Instruct-2507"]`  
  This selects the specific Qwen model to use.

- **max_tokens** (integer):  
  Range: 1024 to 81234 (default: 16384)  
  Defines the maximum number of tokens the model is allowed to generate or process.

- **text_input** (string):  
  Multiline text input (default empty string)  
  The prompt or input text to send to the Qwen model.

---

## Return Value

- A tuple containing a single string — the model's generated response.

---

## Integration Details

- The class method `INPUT_TYPES` defines the input interface for the node.
- `RETURN_TYPES` defines the output type.
- `FUNCTION` specifies the method name to call on execution.
- `CATEGORY` groups this node under `"GPT_QWEN/Qwen"`.
- `NODE_CLASS_MAPPINGS` maps the node identifier `"Qwen"` to the `Qwen3` class.
- `NODE_DISPLAY_NAME_MAPPINGS` provides a user-friendly name `"Qwen GPT"` for display in the interface.

---

## Usage Example

```python
# Example of calling the node method directly
qwen_node = Qwen3()
response, = qwen_node.use_qwen(
    model_name="Qwen/Qwen3-4B-Instruct-2507",
    max_tokens=16384,
    text_input="Explain the concept of recursion."
)
print(response)
