"""AWS Lambda fulfillment hook for the HandyBot Amazon Lex V2 bot."""

from __future__ import annotations

from typing import Any


VALID_STAGES = {"preflop", "flop", "turn", "river"}


def _slot_value(slots: dict[str, Any], name: str) -> str | None:
    slot = slots.get(name)
    if not slot:
        return None
    value = slot.get("value", {})
    return value.get("interpretedValue") or value.get("originalValue")


def _close(event: dict[str, Any], message: str) -> dict[str, Any]:
    session_state = event.get("sessionState", {})
    intent = session_state.get("intent", {})
    intent["state"] = "Fulfilled"
    session_state["intent"] = intent
    return {
        "sessionState": session_state,
        "messages": [{"contentType": "PlainText", "content": message}],
    }


def _delegate(event: dict[str, Any]) -> dict[str, Any]:
    session_state = event.get("sessionState", {})
    session_state["dialogAction"] = {"type": "Delegate"}
    return {"sessionState": session_state}


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Return a concise illustrative hand range for a player and game stage.

    This is educational demo logic, not a poker solver or gambling advice.
    """
    intent = event.get("sessionState", {}).get("intent", {})
    slots = intent.get("slots") or {}
    player = _slot_value(slots, "PlayerNumber")
    stage = (_slot_value(slots, "GameStage") or "").lower()

    if not player or stage not in VALID_STAGES:
        return _delegate(event)

    ranges = {
        "preflop": "premium pairs, strong broadway cards, or suited connectors",
        "flop": "made pairs, two-pair combinations, sets, and credible draws",
        "turn": "strong made hands, improved draws, or selected bluffs",
        "river": "value hands or missed draws being used as bluffs",
    }
    message = (
        f"Player {player} could represent {ranges[stage]} at the {stage}. "
        "That is a broad illustrative range; position, actions, stack sizes, "
        "and bet sizing are needed for a serious estimate."
    )
    return _close(event, message)

