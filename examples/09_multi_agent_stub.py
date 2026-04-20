"""Example 9 (STUB): Multi-agent with different policies.

Two AI agents sharing one Gate instance but governed by
different policies — e.g., a research agent (permissive)
and a deployment agent (strict).

Run: python examples/09_multi_agent_stub.py
"""

# from maelstrom_gate.core import Gate, Tool
# from gate_policy.integration import PolicyGate
# from gate_policy.loader import load_policy_file
#
# gate = Gate()
# gate.add_tools([...])
#
# research_policy = load_policy_file("policies/research_permissive.yaml")
# deploy_policy = load_policy_file("policies/deploy_strict.yaml")
#
# research_agent = PolicyGate(gate, research_policy)
# deploy_agent = PolicyGate(gate, deploy_policy)
#
# # Same gate, same tools, different permissions
# r1 = research_agent.filter(0.3, {"role": "researcher"})
# r2 = deploy_agent.filter(0.3, {"role": "deployer"})

print("STUB: Multi-agent policy isolation.")
print("Pattern: one Gate, multiple PolicyGate wrappers with different policies.")
print("Each agent sees a different tool set based on its policy.")
