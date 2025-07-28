# Documentation Generation Tools:

"You can automatically generate documentation from well-written docstrings:"

# generate_docs.py
import pydoc
import os
from pathlib import Path

def generate_html_documentation(module_path: str, output_dir: str = "docs"):
    """
    Generate HTML documentation for all Python modules in a directory.
    
    Args:
        module_path: Path to the module or package
        output_dir: Directory to save HTML files
    """
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Generate documentation
    for py_file in Path(module_path).glob("**/*.py"):
        if "__pycache__" not in str(py_file):
            module_name = py_file.stem
            html_content = pydoc.html.page(
                pydoc.describe(py_file),
                pydoc.html.document(str(py_file))
            )
            
            output_path = Path(output_dir) / f"{module_name}.html"
            output_path.write_text(html_content)
            print(f"Generated: {output_path}")

# Alternative: Use built-in help system
def print_module_help(module_name: str):
    """Print formatted help for a module."""
    module = __import__(module_name)
    help(module)
