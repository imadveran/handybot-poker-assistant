# HandyBot

HandyBot is a serverless poker assistant built with Amazon Lex V2 and AWS
Lambda. It collects a player number and game stage, then returns a concise,
illustrative Texas Hold'em hand range with a reminder that position, prior
actions, stack sizes, and bet sizing are necessary for serious analysis.

## AWS services

- **Amazon Lex V2** — intent recognition and slot collection
- **AWS Lambda** — Python fulfillment logic
- **AWS CloudFormation / SAM** — repeatable infrastructure deployment
- **Amazon CloudWatch** — logs, metrics, and tracing

## Repository map

| Path | Purpose |
| --- | --- |
| `src/app.py` | Lex V2 Lambda fulfillment hook |
| `template.yaml` | Deployable Lex/Lambda SAM stack |
| `events/` | Sample Lex V2 invocation |
| `tests/` | Unit tests |
| `docs/` | Architecture and deployment guides |
| `React/`, `StepFunctions/`, `SageMaker/` | Optional early prototypes |
| `Lex/`, `Lambda/` | Original Lex V1-era prototype files |

## Quick start

```bash
python -m unittest discover -s tests -v
sam validate --lint
sam build
sam deploy --guided --region us-east-1
```

See [AWS deployment](docs/DEPLOYMENT.md) and
[architecture](docs/ARCHITECTURE.md) for details.

## Example

> **User:** What hands could player 3 have on the turn?
>
> **HandyBot:** Player 3 could represent strong made hands, improved draws, or
> selected bluffs at the turn. That is a broad illustrative range; position,
> actions, stack sizes, and bet sizing are needed for a serious estimate.

## Status and scope

This repository is an AWS reference implementation. Its range logic is a
transparent rule-based demonstration, not a trained model or game-theory-optimal
solver. The optional SageMaker file is an undeployed prototype.

## License

MIT
