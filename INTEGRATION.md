# gate-examples — Integration Map

## What This Covers

| Example | Components Used | Layer Coverage |
|---------|----------------|---------------|
| 01_basic_gate | gate-core | L0 |
| 02_policy_rules | gate-core + gate-policy | L0 + L2 |
| 03_yaml_policy | gate-core + gate-policy (YAML loader) | L0 + L2 |
| 04_compose_policies | gate-core + gate-policy (composition) | L0 + L2 |
| 05_envelope_signing | gate-core (envelope module) | L0 |
| 06_sdk_client | gate-sdk | L1 |
| 07_full_pipeline | gate-core + gate-policy + envelope | L0 + L2 |

## What's Missing (integration gaps for Improvers)

- **gate-server example**: HTTP client hitting gate-server endpoints (needs gate-server running)
- **gate-compliance example**: show audit log ingestion and reporting
- **Multi-agent example**: two agents with different policies sharing one Gate
- **Framework example**: OpenAI/Anthropic adapter usage via gate-sdk
- **Remote mode source**: webhook-driven mode signal
