"""
Basic Code Language Model - A lightweight code generation system
Provides template-based and NLP-guided code generation for common patterns
"""

from typing import Dict, List, Optional


class BasicCodeLM:
    """
    A lightweight language model for generating basic code snippets.
    Supports template-based generation and natural language suggestions.
    """

    def __init__(self):
        """Initialize the code LM with predefined templates."""
        self.templates = {
            "hello_world": {
                "language": "python",
                "code": 'print("Hello, World!")',
                "description": "Simple hello world program"
            },
            "function": {
                "language": "python",
                "code": 'def {func_name}({params}):\n    """{doc}"""\n    pass',
                "description": "Function template with docstring",
                "params": ["func_name", "params", "doc"]
            },
            "class": {
                "language": "python",
                "code": 'class {class_name}:\n    """{doc}"""\n    def __init__(self):\n        pass',
                "description": "Basic class template",
                "params": ["class_name", "doc"]
            },
            "for_loop": {
                "language": "python",
                "code": 'for {var} in {iterable}:\n    {body}',
                "description": "For loop template",
                "params": ["var", "iterable", "body"]
            },
            "if_statement": {
                "language": "python",
                "code": 'if {condition}:\n    {true_body}\nelse:\n    {false_body}',
                "description": "If-else statement template",
                "params": ["condition", "true_body", "false_body"]
            },
            "try_except": {
                "language": "python",
                "code": 'try:\n    {body}\nexcept {exception_type} as e:\n    {error_handler}',
                "description": "Try-except error handling template",
                "params": ["body", "exception_type", "error_handler"]
            }
        }

        # Natural language to template mapping
        self.nl_mappings = {
            "hello": "hello_world",
            "function": "function",
            "def": "function",
            "class": "class",
            "loop": "for_loop",
            "if": "if_statement",
            "condition": "if_statement",
            "error": "try_except",
            "exception": "try_except",
            "try": "try_except"
        }

    def list_templates(self) -> List[str]:
        """
        List all available templates.

        Returns:
            List of template names
        """
        return list(self.templates.keys())

    def get_template_info(self, template_name: str) -> Optional[Dict]:
        """
        Get information about a specific template.

        Args:
            template_name: Name of the template

        Returns:
            Dictionary with template info or None if not found
        """
        return self.templates.get(template_name)

    def generate_code(self, template_name: str, **kwargs) -> Optional[str]:
        """
        Generate code from a template with given parameters.

        Args:
            template_name: Name of the template to use
            **kwargs: Parameters to substitute in the template

        Returns:
            Generated code string or None if template not found
        """
        if template_name not in self.templates:
            return None

        template_info = self.templates[template_name]
        code = template_info["code"]

        # Substitute parameters
        try:
            code = code.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required parameter: {e}")

        return code

    def suggest_code(self, description: str) -> str:
        """
        Suggest code based on natural language description.
        Matches keywords to appropriate templates.

        Args:
            description: Natural language description of desired code

        Returns:
            Generated code or a helpful message
        """
        description_lower = description.lower()

        # Find matching template
        matched_template = None
        for keyword, template_name in self.nl_mappings.items():
            if keyword in description_lower:
                matched_template = template_name
                break

        if matched_template:
            template_info = self.templates[matched_template]
            code = template_info["code"]

            # Provide basic example without full substitution
            if "params" in template_info:
                # Show with placeholders
                return code + "\n# Fill in the parameters above"
            return code

        # Default: list available options
        return (
            f"No direct match found. Available templates:\n"
            + "\n".join(f"- {name}: {info['description']}" 
                       for name, info in self.templates.items())
        )

    def add_template(self, name: str, code: str, language: str = "python",
                     description: str = "", params: Optional[List[str]] = None) -> bool:
        """
        Add a new custom template.

        Args:
            name: Template name
            code: Code template with {param} placeholders
            language: Programming language
            description: Template description
            params: List of parameter names

        Returns:
            True if added successfully
        """
        if name in self.templates:
            return False

        self.templates[name] = {
            "language": language,
            "code": code,
            "description": description,
            "params": params or []
        }
        return True

    def get_code_stats(self) -> Dict:
        """
        Get statistics about available templates.

        Returns:
            Dictionary with template statistics
        """
        languages = set(t["language"] for t in self.templates.values())
        return {
            "total_templates": len(self.templates),
            "languages": list(languages),
            "template_names": self.list_templates()
        }
