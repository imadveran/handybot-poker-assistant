import unittest

from src.app import lambda_handler


def event(player="3", stage="turn"):
    return {
        "sessionState": {
            "intent": {
                "name": "GetOpponentHands",
                "state": "ReadyForFulfillment",
                "slots": {
                    "PlayerNumber": {"value": {"interpretedValue": player}},
                    "GameStage": {"value": {"interpretedValue": stage}},
                },
            }
        }
    }


class HandlerTests(unittest.TestCase):
    def test_fulfills_complete_request(self):
        response = lambda_handler(event(), None)
        self.assertEqual(response["sessionState"]["intent"]["state"], "Fulfilled")
        self.assertIn("Player 3", response["messages"][0]["content"])
        self.assertIn("turn", response["messages"][0]["content"])

    def test_delegates_when_slot_is_missing(self):
        request = event()
        request["sessionState"]["intent"]["slots"]["GameStage"] = None
        response = lambda_handler(request, None)
        self.assertEqual(response["sessionState"]["dialogAction"], {"type": "Delegate"})


if __name__ == "__main__":
    unittest.main()
