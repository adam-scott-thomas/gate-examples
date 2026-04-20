"""Example 6: SDK client — middleware, callbacks, and mode overrides.

GateClient wraps the low-level Gate with developer ergonomics:
middleware hooks, suppress callbacks, and context manager overrides.

Run: python examples/06_sdk_client.py
"""

from gate_sdk.client import GateClient

client = GateClient(mode=0.0)
client.add_tool("read_file", "read_only", description="Read a file")
client.add_tool("deploy", "high_impact", description="Deploy to production")
client.add_tool("write_db", "state_mutation", description="Write to database")
client.add_tool("send_email", "external_action", description="Send email")

# Middleware: log every filter call
log = []
def audit_hook(mode, result):
    log.append({"mode": mode, "visible": len(result.visible), "suppressed": len(result.suppressed)})
    return result

client.use(audit_hook)

# Suppress callback: track what gets blocked
blocked = []
client.on_suppress(lambda tool, mode: blocked.append(tool.name))

# Normal mode
print("Normal mode (0.0):")
r = client.filter()
print(f"  Visible: {r.visible_names}")

# Override to crisis
print("\nCrisis override (0.9):")
with client.override_mode(0.9):
    r = client.filter()
    print(f"  Visible: {r.visible_names}")
    print(f"  Blocked: {blocked}")

# Back to normal
print("\nBack to normal:")
r = client.filter()
print(f"  Visible: {r.visible_names}")
print(f"  Audit log entries: {len(log)}")
