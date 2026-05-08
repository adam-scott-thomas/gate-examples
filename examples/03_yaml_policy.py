"""Example 3: Load policy from YAML — config-driven access control.

Policies live in YAML files that ops teams can edit without
touching code. Load, evaluate, swap policies at runtime.

Run: python examples/03_yaml_policy.py
"""

from pathlib import Path
from gatekeeper.core import Gate, Tool
from gate_policy.integration import PolicyGate
from gate_policy.loader import load_policy_file

# Load the enterprise policy from gate-policy's examples
POLICY_DIR = Path(__file__).parent.parent.parent / "gate-policy" / "examples"

gate = Gate()
gate.add_tools([
    Tool(name="read_logs", execution_class="read_only"),
    Tool(name="deploy_production", execution_class="high_impact"),
    Tool(name="update_config", execution_class="state_mutation"),
    Tool(name="send_alert", execution_class="external_action"),
    Tool(name="rollback", execution_class="high_impact"),
])

for policy_file in ["enterprise_standard.yaml", "startup_permissive.yaml"]:
    path = POLICY_DIR / policy_file
    if not path.exists():
        print(f"  (skipping {policy_file} — not found at {path})")
        continue

    policy = load_policy_file(path)
    pg = PolicyGate(gate, policy)

    print(f"\nPolicy: {policy.name}")
    print(f"  Rules: {len(policy.rules)}")

    r = pg.filter(0.1, {"role": "developer", "human_approved": False})
    print(f"  Developer, normal mode:")
    print(f"    Visible: {r.visible_names}")
    print(f"    Denied:  {r.policy_denied_names}")
