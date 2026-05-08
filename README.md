# gate-examples

[![status](https://img.shields.io/badge/status-v0.1.0-blue)]()
[![tests](https://img.shields.io/badge/tests-1_passing-brightgreen)]()
[![license](https://img.shields.io/badge/license-Apache_2.0-green)]()

> Ready-to-run integration examples for Gatekeeper. Zero to governed agent
> in 9 scripts.

Nine numbered examples, each runnable standalone. Start at `01_basic_gate.py`
and walk up to multi-agent policy composition. Each file is ~50 lines and
prints what's happening as it runs.

## Install

```bash
pip install gate-examples  # once published
# or from source:
pip install -e .[all]
```

## Run all

```bash
python run_all.py
```

## Run individual

```bash
python examples/01_basic_gate.py
python examples/05_envelope_signing.py
```

## The 9 examples

| # | File | What it shows |
|---|------|---------------|
| 01 | `01_basic_gate.py` | Register tools, set mode, filter |
| 02 | `02_policy_rules.py` | Add a policy engine |
| 03 | `03_yaml_policy.py` | Load policy from YAML |
| 04 | `04_compose_policies.py` | Merge org + team + project policies |
| 05 | `05_envelope_signing.py` | HMAC-signed authorization envelopes |
| 06 | `06_sdk_client.py` | `gate-sdk` with middleware + callbacks |
| 07 | `07_full_pipeline.py` | L0 → L1 → L2 end-to-end |
| 08 | `08_remote_server_stub.py` | Talk to `gate-server` over HTTP |
| 09 | `09_multi_agent_stub.py` | Multiple agents, shared policy |

## Tests

```bash
pytest tests/
```

1 test: every example runs to completion and exits 0. If an example breaks, CI
catches it before the spec does.

## How it fits

Reference for [Gatekeeper](https://github.com/adam-scott-thomas/gate-keeper).
Depends on `gate-keeper`, `gate-policy`. Optional extras (`all`) pull in
`gate-sdk` and `httpx` for the server examples.

## License

Apache-2.0.
