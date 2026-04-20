"""Example 1: Basic Gate — filter tools by mode in 10 lines.

This is the simplest possible Gate usage. Register tools,
set a mode, see what's visible.

Run: python examples/01_basic_gate.py
"""

from maelstrom_gate.core import Gate, Tool

gate = Gate()
gate.add_tools([
    Tool(name="read_file", execution_class="read_only", description="Read a file"),
    Tool(name="write_file", execution_class="state_mutation", description="Write a file"),
    Tool(name="deploy", execution_class="high_impact", description="Deploy to production"),
    Tool(name="analyze", execution_class="advisory", description="Run analysis"),
    Tool(name="send_email", execution_class="external_action", description="Send email"),
])

for mode in [0.0, 0.4, 0.8]:
    result = gate.filter(mode)
    print(f"\nMode {mode:.1f} ({result.mode_zone}):")
    print(f"  Visible:    {result.visible_names}")
    print(f"  Suppressed: {result.suppressed_names}")
