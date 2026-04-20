"""Example 8 (STUB): Remote gate-server client.

Shows how to talk to a running gate-server over HTTP.
Requires: gate-server running at http://localhost:8000

Run: python examples/08_remote_server_stub.py
"""

# import httpx
#
# BASE = "http://localhost:8000"
#
# # Register tools
# httpx.post(f"{BASE}/v1/tools", json={"tools": [
#     {"name": "read_file", "execution_class": "read_only"},
#     {"name": "deploy", "execution_class": "high_impact"},
# ]})
#
# # Filter at elevated mode
# r = httpx.post(f"{BASE}/v1/filter", json={"mode": 0.5})
# print(r.json())
#
# # Build an envelope
# r = httpx.post(f"{BASE}/v1/envelope", json={
#     "tool_name": "read_file", "context_id": "demo", "mode": 0.2
# })
# print(r.json())

print("STUB: Requires gate-server running. See gate-server/ for setup.")
print("Endpoints: POST /v1/tools, POST /v1/filter, POST /v1/envelope")
