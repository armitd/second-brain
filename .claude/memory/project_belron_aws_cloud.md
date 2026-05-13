---
name: Belron AWS Cloud Provider
description: AWS is a confirmed Belron cloud provider — activates Claude Platform on AWS and Amazon Connect as primary architecture options
type: project
---

AWS is a confirmed Belron cloud provider (confirmed May 12, 2026).

**Why:** This was an open validation question across multiple active projects — MCP governance and CCOTF both had AWS-dependency conditionals.

**How to apply:**
- **MCP Governance:** Claude Platform on AWS (GA May 11, 2026) is now directly in scope. MCP governance can leverage AWS IAM, CloudTrail, and existing AWS billing — no separate Anthropic account needed. The MCP Connector on AWS should be assessed as a governance control point in the MCP Governance framework.
- **CCOTF:** Amazon Connect (rebranded as Amazon Connect Customer — full agentic AI suite with MCP support) is the front-runner CCaaS platform candidate. It runs natively on AWS, integrates with Bedrock for AI, and has confirmed agentic/MCP support.
- **AI Damage Assessment PoC:** AWS Bedrock is a live option for model inference; Rekognition Custom Labels for custom CV model training; SageMaker for MLOps.
- Note: AWS being a cloud provider does not rule out multi-cloud or other CCaaS platforms — Belron may use Genesys or Salesforce for contact centre regardless. The current CCaaS platform is still an open question.
