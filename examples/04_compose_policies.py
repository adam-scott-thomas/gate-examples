"""Example 4: Compose multiple policies — strict vs permissive merge.

Combine policies from different teams. Strict merge means
any deny from any policy wins. Permissive means any allow wins.

Run: python examples/04_compose_policies.py
"""

from pathlib import Path
from gatekeeper.core import Gate, Tool
from gate_policy.integration import PolicyGate
from gate_policy.loader import load_policy_file
from gate_policy.compose import merge_policies

POLICY_DIR = Path(__file__).parent.parent.parent / "gate-policy" / "examples"

gate = Gate()
gate.add_tools([
    Tool(name="read_logs", execution_class="read_only"),
    Tool(name="deploy_production", execution_class="high_impact"),
    Tool(name="deploy_staging", execution_class="high_impact"),
    Tool(name="update_config", execution_class="state_mutation"),
    Tool(name="send_alert", execution_class="external_action"),
])

enterprise = load_policy_file(POLICY_DIR / "enterprise_standard.yaml")
startup = load_policy_file(POLICY_DIR / "startup_permissive.yaml")

for strategy in ["strict", "permissive"]:
    merged = merge_policies([enterprise, startup], strategy=strategy)
    pg = PolicyGate(gate, merged)

    # Friday 5pm, admin, approved
    r = pg.filter(0.1, {
        "role": "admin",
        "human_approved": True,
        "_now": __import__("datetime").datetime(2026, 4, 10, 17, 0),
    })

    print(f"\n{strategy.upper()} merge — Friday 5pm, admin, approved:")
    print(f"  Visible: {r.visible_names}")
    print(f"  Denied:  {r.policy_denied_names}")
