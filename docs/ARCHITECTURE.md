# Architecture

HandyBot is a serverless conversational demonstration for estimating broad,
illustrative Texas Hold'em hand ranges.

1. A user sends an utterance to the `live` Amazon Lex V2 alias.
2. Lex recognizes `GetOpponentHands` and collects `PlayerNumber` and `GameStage`.
3. Lex invokes the Python 3.12 Lambda fulfillment hook.
4. Lambda validates the slots and returns a Lex V2 response.
5. CloudWatch receives Lambda logs and standard service metrics.

The root `template.yaml` defines the Lambda function, least-privilege execution
role, Lex V2 bot/locale/intent/slots, immutable bot version, live alias, and
resource-based permission allowing only the created alias to invoke Lambda.

The files under `Lex/` and `Lambda/` are retained as the original Lex V1-era
prototype. Production deployment uses `src/app.py` and `template.yaml`.

## Optional prototypes

- `React/`: a small board-card display component.
- `StepFunctions/`: an early game-action orchestration sketch.
- `SageMaker/`: an early player-style endpoint sketch.

These are not deployed by the core SAM stack.

