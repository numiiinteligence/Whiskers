"""
Test suite for BasicCodeLM
Comprehensive tests for all functionality
"""

import pytest
from code_lm.model import BasicCodeLM


class TestBasicCodeLMInit:
    """Test BasicCodeLM initialization"""

    def test_initialization(self):
        """Test that BasicCodeLM initializes correctly"""
        lm = BasicCodeLM()
        assert lm is not None
        assert len(lm.templates) == 6

    def test_default_templates_exist(self):
        """Test that all default templates are initialized"""
        lm = BasicCodeLM()
        expected_templates = [
            "hello_world", "function", "class", 
            "for_loop", "if_statement", "try_except"
        ]
        for template in expected_templates:
            assert template in lm.templates


class TestListTemplates:
    """Test list_templates method"""

    def test_list_templates_returns_list(self):
        """Test that list_templates returns a list"""
        lm = BasicCodeLM()
        templates = lm.list_templates()
        assert isinstance(templates, list)
        assert len(templates) == 6

    def test_list_templates_contains_all(self):
        """Test that list includes all templates"""
        lm = BasicCodeLM()
        templates = lm.list_templates()
        assert "hello_world" in templates
        assert "function" in templates
        assert "class" in templates


class TestGetTemplateInfo:
    """Test get_template_info method"""

    def test_get_existing_template(self):
        """Test getting info for existing template"""
        lm = BasicCodeLM()
        info = lm.get_template_info("hello_world")
        assert info is not None
        assert "code" in info
        assert "description" in info
        assert "language" in info

    def test_get_nonexistent_template(self):
        """Test getting info for non-existent template"""
        lm = BasicCodeLM()
        info = lm.get_template_info("nonexistent")
        assert info is None


class TestGenerateCode:
    """Test generate_code method"""

    def test_generate_hello_world(self):
        """Test generating hello world code"""
        lm = BasicCodeLM()
        code = lm.generate_code("hello_world")
        assert code is not None
        assert 'print("Hello, World!")' in code

    def test_generate_function(self):
        """Test generating function code"""
        lm = BasicCodeLM()
        code = lm.generate_code(
            "function",
            func_name="add",
            params="a, b",
            doc="Add two numbers"
        )
        assert code is not None
        assert "def add(a, b):" in code
        assert "Add two numbers" in code

    def test_generate_class(self):
        """Test generating class code"""
        lm = BasicCodeLM()
        code = lm.generate_code(
            "class",
            class_name="MyClass",
            doc="My custom class"
        )
        assert code is not None
        assert "class MyClass:" in code
        assert "My custom class" in code

    def test_generate_for_loop(self):
        """Test generating for loop code"""
        lm = BasicCodeLM()
        code = lm.generate_code(
            "for_loop",
            var="item",
            iterable="items",
            body="print(item)"
        )
        assert code is not None
        assert "for item in items:" in code
        assert "print(item)" in code

    def test_generate_if_statement(self):
        """Test generating if statement code"""
        lm = BasicCodeLM()
        code = lm.generate_code(
            "if_statement",
            condition="x > 0",
            true_body="print('positive')",
            false_body="print('non-positive')"
        )
        assert code is not None
        assert "if x > 0:" in code
        assert "print('positive')" in code

    def test_generate_try_except(self):
        """Test generating try-except code"""
        lm = BasicCodeLM()
        code = lm.generate_code(
            "try_except",
            body="risky_operation()",
            exception_type="ValueError",
            error_handler="print('Error occurred')"
        )
        assert code is not None
        assert "try:" in code
        assert "except ValueError" in code

    def test_generate_nonexistent_template(self):
        """Test generating from non-existent template"""
        lm = BasicCodeLM()
        code = lm.generate_code("nonexistent")
        assert code is None

    def test_generate_missing_parameters(self):
        """Test that missing parameters raises error"""
        lm = BasicCodeLM()
        with pytest.raises(ValueError):
            lm.generate_code("function", func_name="test")


class TestSuggestCode:
    """Test suggest_code method"""

    def test_suggest_function(self):
        """Test suggesting function code"""
        lm = BasicCodeLM()
        code = lm.suggest_code("write a function")
        assert code is not None
        assert "def" in code

    def test_suggest_class(self):
        """Test suggesting class code"""
        lm = BasicCodeLM()
        code = lm.suggest_code("create a class")
        assert code is not None
        assert "class" in code

    def test_suggest_loop(self):
        """Test suggesting loop code"""
        lm = BasicCodeLM()
        code = lm.suggest_code("make a loop")
        assert code is not None
        assert "for" in code

    def test_suggest_error_handling(self):
        """Test suggesting error handling code"""
        lm = BasicCodeLM()
        code = lm.suggest_code("handle errors")
        assert code is not None
        assert "try" in code

    def test_suggest_no_match(self):
        """Test suggesting with no match"""
        lm = BasicCodeLM()
        code = lm.suggest_code("something random")
        assert code is not None
        assert "Available templates" in code


class TestAddTemplate:
    """Test add_template method"""

    def test_add_valid_template(self):
        """Test adding a valid custom template"""
        lm = BasicCodeLM()
        success = lm.add_template(
            "decorator",
            "def decorator():\n    pass",
            description="A decorator template"
        )
        assert success is True
        assert "decorator" in lm.templates

    def test_add_duplicate_template(self):
        """Test adding duplicate template fails"""
        lm = BasicCodeLM()
        success = lm.add_template(
            "hello_world",
            "print('test')"
        )
        assert success is False

    def test_custom_template_info(self):
        """Test that custom template has correct info"""
        lm = BasicCodeLM()
        lm.add_template(
            "custom",
            "custom code",
            language="javascript",
            description="A custom template",
            params=["param1"]
        )
        info = lm.get_template_info("custom")
        assert info["language"] == "javascript"
        assert info["description"] == "A custom template"
        assert "param1" in info["params"]

    def test_generate_from_custom_template(self):
        """Test generating code from custom template"""
        lm = BasicCodeLM()
        lm.add_template(
            "simple",
            "console.log('{message}')",
            language="javascript",
            params=["message"]
        )
        code = lm.generate_code("simple", message="Hello")
        assert "console.log('Hello')" in code


class TestGetCodeStats:
    """Test get_code_stats method"""

    def test_stats_structure(self):
        """Test that stats has correct structure"""
        lm = BasicCodeLM()
        stats = lm.get_code_stats()
        assert "total_templates" in stats
        assert "languages" in stats
        assert "template_names" in stats

    def test_stats_values(self):
        """Test that stats has correct values"""
        lm = BasicCodeLM()
        stats = lm.get_code_stats()
        assert stats["total_templates"] == 6
        assert "python" in stats["languages"]
        assert len(stats["template_names"]) == 6

    def test_stats_after_adding_template(self):
        """Test stats update after adding template"""
        lm = BasicCodeLM()
        initial_count = lm.get_code_stats()["total_templates"]
        lm.add_template("new", "code")
        new_count = lm.get_code_stats()["total_templates"]
        assert new_count == initial_count + 1


class TestIntegration:
    """Integration tests"""

    def test_full_workflow(self):
        """Test complete workflow"""
        lm = BasicCodeLM()
        
        # List templates
        templates = lm.list_templates()
        assert len(templates) > 0
        
        # Get template info
        info = lm.get_template_info(templates[0])
        assert info is not None
        
        # Generate code
        if templates[0] == "hello_world":
            code = lm.generate_code(templates[0])
        else:
            code = lm.generate_code(
                "function",
                func_name="test",
                params="x",
                doc="Test"
            )
        assert code is not None

    def test_multiple_generations(self):
        """Test multiple code generations"""
        lm = BasicCodeLM()
        
        code1 = lm.generate_code(
            "function",
            func_name="func1",
            params="a",
            doc="First"
        )
        
        code2 = lm.generate_code(
            "function",
            func_name="func2",
            params="b",
            doc="Second"
        )
        
        assert code1 != code2
        assert "func1" in code1
        assert "func2" in code2
