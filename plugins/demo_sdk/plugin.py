"""
Demo SDK Plugin

Version: 1.0.0
"""

from core.sdk import tool


@tool(
    name="hello_sdk",
    description="Demo SDK tool"
)
def hello_sdk(name="World"):
    return f"Hello, {name}! This is the SDK plugin."
