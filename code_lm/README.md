# Basic Code Language Model

A lightweight Python library for generating basic code snippets using templates and natural language processing.

## Features

✨ **Template-Based Code Generation** - 6 ready-to-use templates
🗣️ **Natural Language Support** - Describe code in plain English
🔧 **Extensible** - Add custom templates easily
✅ **Well-Tested** - Comprehensive test coverage
📚 **Documented** - Full API documentation with examples

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from code_lm.model import BasicCodeLM

# Initialize the LM
lm = BasicCodeLM()

# Generate code from template
code = lm.generate_code(
    "function",
    func_name="add",
    params="a, b",
    doc="Add two numbers"
)
print(code)

# Or use natural language
code = lm.suggest_code("write a function")
print(code)

# List available templates
print(lm.list_templates())
```

## Available Templates

| Template | Language | Description |
|----------|----------|-------------|
| `hello_world` | Python | Simple hello world program |
| `function` | Python | Function with docstring |
| `class` | Python | Basic class definition |
| `for_loop` | Python | For loop template |
| `if_statement` | Python | If-else statement |
| `try_except` | Python | Try-except error handling |

## API Reference

### `BasicCodeLM()`

Main class for code generation.

#### Methods

**`list_templates() -> List[str]`**
Returns all available template names.

**`get_template_info(template_name: str) -> Optional[Dict]`**
Get detailed information about a specific template.

**`generate_code(template_name: str, **kwargs) -> Optional[str]`**
Generate code from a template with parameters.

```python
code = lm.generate_code(
    "function",
    func_name="my_func",
    params="x, y",
    doc="My function"
)
```

**`suggest_code(description: str) -> str`**
Generate code based on natural language description.

```python
code = lm.suggest_code("create a for loop")
```

**`add_template(name: str, code: str, language: str = "python", description: str = "", params: Optional[List[str]] = None) -> bool`**
Add a custom template.

```python
lm.add_template(
    "decorator",
    "def {decorator_name}(func):\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper",
    description="Function decorator template",
    params=["decorator_name"]
)
```

**`get_code_stats() -> Dict`**
Get statistics about available templates.

```python
stats = lm.get_code_stats()
# {'total_templates': 6, 'languages': ['python'], 'template_names': [...]}
```

## Examples

### Generate a Function

```python
code = lm.generate_code(
    "function",
    func_name="calculate_sum",
    params="numbers: list",
    doc="Calculate the sum of a list of numbers"
)
# Output:
# def calculate_sum(numbers: list):
#     """Calculate the sum of a list of numbers"""
#     pass
```

### Generate a Class

```python
code = lm.generate_code(
    "class",
    class_name="DataProcessor",
    doc="Processes data from various sources"
)
# Output:
# class DataProcessor:
#     """Processes data from various sources"""
#     def __init__(self):
#         pass
```

### Generate Error Handling

```python
code = lm.generate_code(
    "try_except",
    body="result = risky_operation()",
    exception_type="ValueError",
    error_handler="print(f'Invalid value: {e}')"
)
# Output:
# try:
#     result = risky_operation()
# except ValueError as e:
#     print(f'Invalid value: {e}')
```

## Testing

Run the test suite:

```bash
pytest code_lm/test_model.py -v
```

## Future Enhancements

- [ ] Multi-language support (JavaScript, Java, Go)
- [ ] Advanced NLP for better code suggestions
- [ ] Custom code style templates
- [ ] Integration with popular code formatters
- [ ] CLI interface

## License

MIT
