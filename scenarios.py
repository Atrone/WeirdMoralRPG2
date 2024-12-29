# Base scenarios for the RPG
base_scenarios = {
    "start": {
        "description":
        "You find yourself in a small village. A merchant's cart has been overturned, spilling valuable goods.",
        "choices": [{
            "text":
            "Help the merchant gather their goods",
            "moral_value":
            10,
            "capability_value":
            5,
            "next_scene":
            "village_square",
            "result":
            "The merchant thanks you profusely and offers a small reward."
        }, {
            "text": "Pretend not to notice and walk away",
            "moral_value": -5,
            "capability_value": 0,
            "next_scene": "village_square",
            "result": "You avoid the situation entirely."
        }, {
            "text":
            "Steal some valuable items while helping",
            "moral_value":
            -10,
            "capability_value":
            8,
            "next_scene":
            "village_square",
            "result":
            "You manage to pocket some items without being noticed."
        }]
    },
    "village_square": {
        "description":
        "In the village square, you witness a heated argument between two merchants over a rare artifact.",
        "choices": [{
            "text": "Mediate the dispute fairly",
            "moral_value": 10,
            "capability_value": 10,
            "next_scene": "end",
            "result": "Both merchants appreciate your fair judgment."
        }, {
            "text": "Side with the merchant offering you a bribe",
            "moral_value": -10,
            "capability_value": 15,
            "next_scene": "end",
            "result": "You receive a generous reward but feel guilty."
        }, {
            "text": "Steal the artifact during the confusion",
            "moral_value": -15,
            "capability_value": 20,
            "next_scene": "end",
            "result": "You successfully steal the valuable artifact."
        }]
    }
}
