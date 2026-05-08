"""Example 2: Policy rules — add role-based and time-based access control.

Layer gate-policy on top of gate-core. Tools must pass BOTH
mode suppression AND policy rules to be visible.

Run: python examples/02_policy_rules.py
"""

from datetime import datetime
from gatekeeper.core import Gate, Tool
from gate_policy.integration import PolicyGate
from gate_policy.models import Policy, Rule, Condition, Effect

# Define tools
gate = Gate()
gate.add_tools([
    Tool(name="read_logs", execution_class="read_only"),
    Tool(name="deploy", execution_class="high_impact"),
    Tool(name="update_config", execution_class="state_mutation"),
    Tool(name="send_alert", execution_class="external_action"),
])

# Define policy: require approval for high_impact
policy = Policy(
    name="require-approval",
    rules=(
        Rule(
            name="deny-unapproved-deploys",
            effect=Effect.DENY,
            execution_classes=frozenset({"high_impact"}),
            conditions=(Condition(field="human_approved", operator="neq", value=True),),
            priority=10,
        ),
    ),
    default_effect=Effect.ALLOW,
)

pg = PolicyGate(gate, policy)

# Developer without approval
print("Developer, no approval:")
r = pg.filter(0.1, {"role": "developer", "human_approved": False})
print(f"  Visible:       {r.visible_names}")
print(f"  Policy denied: {r.policy_denied_names}")

# Admin with approval
print("\nAdmin, approved:")
r = pg.filter(0.1, {"role": "admin", "human_approved": True})
print(f"  Visible:       {r.visible_names}")
print(f"  Policy denied: {r.policy_denied_names}")
