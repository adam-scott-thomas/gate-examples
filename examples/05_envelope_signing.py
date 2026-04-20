"""Example 5: Authorization envelopes — signed, tamper-proof permissions.

Envelopes freeze a permission set and sign it with HMAC-SHA256.
The executor can verify the envelope wasn't tampered with.
Crisis mode automatically tightens budget and call limits.

Run: python examples/05_envelope_signing.py
"""

from dataclasses import replace
from maelstrom_gate.core import Tool
from maelstrom_gate.envelope import build_envelope, verify_envelope

SIGNING_KEY = "example-key-do-not-use-in-production"
read_file = Tool(name="read_file", execution_class="read_only")

# Build envelope at normal mode
env = build_envelope(read_file, mode=0.2, context_id="session_42", signing_key=SIGNING_KEY)

print("Envelope (normal mode):")
print(f"  tool:       {env.tool_name}")
print(f"  budget:     {env.budget_seconds}s")
print(f"  max_calls:  {env.max_tool_calls}")
print(f"  exec_mode:  {env.execution_mode}")
print(f"  signature:  {env.signature[:24]}...")

# Verify — should pass
print(f"\nValid: {verify_envelope(env, SIGNING_KEY)}")

# Tamper — change the tool name
tampered = replace(env, tool_name="deploy_production")
print(f"Tampered valid: {verify_envelope(tampered, SIGNING_KEY)}")

# Crisis mode — tighter constraints
crisis_env = build_envelope(read_file, mode=0.9, context_id="session_42", signing_key=SIGNING_KEY)
print(f"\nCrisis envelope:")
print(f"  budget:     {crisis_env.budget_seconds}s (was {env.budget_seconds}s)")
print(f"  max_calls:  {crisis_env.max_tool_calls} (was {env.max_tool_calls})")
print(f"  exec_mode:  {crisis_env.execution_mode} (was {env.execution_mode})")
