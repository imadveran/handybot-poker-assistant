# AWS deployment

## Prerequisites

- An AWS account and a principal allowed to create CloudFormation, IAM, Lambda,
  Lex V2, and CloudWatch resources.
- AWS CLI v2 and AWS SAM CLI.
- Credentials configured with `aws configure` or AWS IAM Identity Center.

## Deploy to us-east-1

```bash
aws sts get-caller-identity
sam validate --lint
sam build
sam deploy --guided --region us-east-1
```

For the first deployment, use stack name `handybot`, allow SAM to create IAM
roles, and save the arguments to `samconfig.toml`. Later deployments use:

```bash
sam build && sam deploy
```

After CloudFormation completes, copy `BotId` and `BotAliasId` from the stack
outputs. In the Amazon Lex V2 console, open the bot, select alias `live`, and
test: `What hands could player 3 have on the turn?`

## Local test

```bash
python -m unittest discover -s tests -v
sam local invoke FulfillmentFunction -e events/get-opponent-hands.json
```

## Cleanup

Deleting the stack removes the AWS resources and prevents ongoing usage:

```bash
sam delete --stack-name handybot --region us-east-1
```

Review CloudWatch retention and AWS billing separately. Lex and Lambda usage may
incur charges. The response is illustrative and is not a poker solver or
gambling advice.
