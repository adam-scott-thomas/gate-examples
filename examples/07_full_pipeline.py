"""Example 7: Full pipeline — gate-core + policy + envelope in one flow.

This is the complete Gate workflow:
1. Register tools
2. Apply policy
3. Filter by mode
4. Build signed envelope for the chosen tool
5. Verify the envelope

Run: python examples/07_full_pipeline.py
"""

from dataclasses import replace
from maelstrom_gate.core import Gate, Tool
from maelstrom_gate.envelope import build_envelope, verify_envelope
from gate_policy.integration import PolicyGate
from gate_policy.models import Policy, Rule, Condition, Effect

SIGNING_KEY = "pipeline-demo-key"

# 1. Register tools
gate = Gate()
tools = [
    Tool(name="read_logs", execution_class="read_only"),
    Tool(name="deploy", execution_class="high_impact"),
    Tool(name="update_config", execution_class="state_mutation"),
]
gate.add_tools(tools)

# 2. Apply policy
policy = Policy(
    name="pipeline-demo",
    rules=(
        Rule(name="require-approval", effect=Effect.DENY,
             execution_classes=frozenset({"high_impact"}),
             conditions=(Condition(field="human_approved", operator="neq", value=True),),
             priority=10),
    ),
    default_effect=Effect.ALLOW,
)
pg = PolicyGate(gate, policy)

# 3. Filter
mode = 0.3
context = {"role": "admin", "human_approved": True}
result = pg.filter(mode, context)

print(f"Mode: {mode} ({result.mode_zone})")
print(f"Visible tools: {result.visible_names}")

# 4. Build envelope for a visible tool
target = next(t for t in result.visible if t.name == "deploy")
env = build_envelope(target, mode=mode, context_id="demo_session", signing_key=SIGNING_KEY)

print(f"\nEnvelope for '{env.tool_name}':")
print(f"  Budget: {env.budget_seconds}s, Max calls: {env.max_tool_calls}")
print(f"  Execution mode: {env.execution_mode}")

# 5. Verify
print(f"  Signature valid: {verify_envelope(env, SIGNING_KEY)}")

# Bonus: what happens if someone tampers?
tampered = replace(env, tool_name="update_config")
print(f"  Tampered valid: {verify_envelope(tampered, SIGNING_KEY)}")
