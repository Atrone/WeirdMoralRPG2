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
base_scenarios = [{
    'start': {
        'description':
        "A bead of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite you. It's not just the merciless glare of the overhead lights that has him sweating.",
        'choices': [{
            'text':
            'Keep playing to gain trust at the table',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'find_angel',
            'result':
            "You gain the players' trust but the game drags on, allowing you to gather more intel."
        }, {
            'text':
            'Accuse the woman with the copper ring of cheating',
            'moral_value':
            -10,
            'capability_value':
            5,
            'next_scene':
            'security_intervention',
            'result':
            'An argument ensues, drawing attention to your table.'
        }, {
            'text': 'Leave the table discreetly',
            'moral_value': 10,
            'capability_value': 0,
            'next_scene': 'casino_search',
            'result': 'You leave quietly, unnoticed by most.'
        }]
    },
    'find_angel': {
        'description':
        "New intelligence puts a DIABLO agent known as Angel here tonight. It's crucial to identify or capture them.",
        'choices': [{
            'text':
            'Pretend to be a waiter to get close',
            'moral_value':
            10,
            'capability_value':
            15,
            'next_scene':
            'elevator_clue',
            'result':
            'You manage to blend in, getting close to the potential target.'
        }, {
            'text':
            'Use surveillance to find Angel',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'find_evidence',
            'result':
            'You expertly handle the cameras for a better view of the floor.'
        }, {
            'text': 'Confront random suspicious individuals',
            'moral_value': -5,
            'capability_value': 5,
            'next_scene': 'unexpected_conflict',
            'result': 'Your rash actions cause a few minor scuffles.'
        }]
    },
    'security_intervention': {
        'description':
        'Security has been alerted. The commotion might hinder or aid your mission.',
        'choices': [{
            'text':
            'Smooth things over with charm',
            'moral_value':
            10,
            'capability_value':
            15,
            'next_scene':
            'natural_resolve',
            'result':
            'Your charm calms the situation, allowing you to stay.'
        }, {
            'text': 'Cause further disruption to escape',
            'moral_value': -10,
            'capability_value': 20,
            'next_scene': 'escape_plan',
            'result': 'The chaos gives you cover to exit unscathed.'
        }, {
            'text': 'Submit to a search by security',
            'moral_value': 5,
            'capability_value': 0,
            'next_scene': 'thorough_check',
            'result': 'You comply, but it costs you precious time.'
        }]
    },
    'casino_search': {
        'description':
        'The busy casino floor is full of potential threats and allies.',
        'choices': [{
            'text': 'Seek help from known informants',
            'moral_value': 15,
            'capability_value': 10,
            'next_scene': 'informant_session',
            'result': 'Trusted informants provide new leads.'
        }, {
            'text':
            'Eavesdrop on various conversations',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'eavesdrop_insight',
            'result':
            'Catching snippets of conversation reveals a few secrets.'
        }, {
            'text':
            'Risk exposing yourself to gather all info',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'high_stakes_move',
            'result':
            'Your bold actions draw attention, for better or worse.'
        }]
    },
    'elevator_clue': {
        'description':
        "In the depths of the casino's network, the elevator holds secrets to your success or demise.",
        'choices': [{
            'text': 'Disable the security temporarily',
            'moral_value': -10,
            'capability_value': 20,
            'next_scene': 'hidden_access',
            'result': 'You create an opportunity with temporary chaos.'
        }, {
            'text':
            'Find an unauthorized access code',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'digital_breach',
            'result':
            'The code grants you deeper access into secure areas.'
        }, {
            'text': 'Charm the staff for access',
            'moral_value': 10,
            'capability_value': 10,
            'next_scene': 'often_forgiven',
            'result': 'Ingratiating yourself with the staff pays off.'
        }]
    }
}, {
    'casino_entrance': {
        'description':
        "The grand entrance of the casino is bustling with elegantly dressed guests. You're here with a mission to uncover the agent known as Angel.",
        'choices': [{
            'text':
            'Blend in with the crowd and observe',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'gaming_floor',
            'result':
            'You manage to go unnoticed while surveying the area.'
        }, {
            'text':
            'Head straight to the poker table',
            'moral_value':
            0,
            'capability_value':
            8,
            'next_scene':
            'poker_table',
            'result':
            'You join a high-stakes poker game, ready to spot your target.'
        }, {
            'text':
            'Seek out the bartender for information',
            'moral_value':
            0,
            'capability_value':
            3,
            'next_scene':
            'bar',
            'result':
            'The bartender gives you a knowing glance, ready to share some intel.'
        }]
    },
    'gaming_floor': {
        'description':
        'The heart of the casino, filled with tables of blackjack, slots, and more. Potential danger lurks beneath the glamour as you search for Angel.',
        'choices': [{
            'text':
            'Approach Frau Bergmann for her assistance',
            'moral_value':
            5,
            'capability_value':
            7,
            'next_scene':
            'vip_room',
            'result':
            'Frau Bergmann nods, discreetly guiding you to a secure location.'
        }, {
            'text':
            'Observe high-value games for suspects',
            'moral_value':
            0,
            'capability_value':
            6,
            'next_scene':
            'gaming_floor',
            'result':
            'You notice some suspicious behaviors, but nothing concrete.'
        }, {
            'text':
            'Call for backup using your hidden earpiece',
            'moral_value':
            2,
            'capability_value':
            4,
            'next_scene':
            'casino_entrance',
            'result':
            'Reinforcements are on standby, but you might lose precious time.'
        }]
    },
    'poker_table': {
        'description':
        "Three players at the table, heavy tension in the air. You're here to win more than just chips — information is the jackpot.",
        'choices': [{
            'text':
            'Play to win and gain access upstairs',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'vip_room',
            'result':
            'Your skill secures you a pass to the exclusive VIP area.'
        }, {
            'text':
            "Deal a shady hand and mark Angel's associate",
            'moral_value':
            -5,
            'capability_value':
            10,
            'next_scene':
            'gaming_floor',
            'result':
            "You've made a subtle alliance, though at some moral cost."
        }, {
            'text':
            'Fold and retreat to gather more intel',
            'moral_value':
            0,
            'capability_value':
            3,
            'next_scene':
            'casino_entrance',
            'result':
            'You quietly leave the table, hoping for another opportunity.'
        }]
    },
    'bar': {
        'description':
        'A corner of relaxation, where secrets often loosen with a drink or two.',
        'choices': [{
            'text':
            'Bribe the bartender for secrets',
            'moral_value':
            -3,
            'capability_value':
            5,
            'next_scene':
            'vip_room',
            'result':
            'The bartender spills some truth, pointing you towards Angel.'
        }, {
            'text': 'Order a signature drink and linger',
            'moral_value': 0,
            'capability_value': 2,
            'next_scene': 'gaming_floor',
            'result': 'You blend in, listening for useful gossip.'
        }, {
            'text':
            'Meet a contact for a gadget exchange',
            'moral_value':
            0,
            'capability_value':
            6,
            'next_scene':
            'poker_table',
            'result':
            'A small device changes hands, boosting your arsenal.'
        }]
    },
    'vip_room': {
        'description':
        'The epitome of luxury and secrecy, where only high-stakes guests can tread.',
        'choices': [{
            'text':
            'Confront the DIABLO agent',
            'moral_value':
            10,
            'capability_value':
            12,
            'next_scene':
            'end',
            'result':
            'You boldly face your adversary, ready for the outcome.'
        }, {
            'text':
            'Gather blackmail material discreetly',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'end',
            'result':
            'Your stealthy capture gives you leverage against them.'
        }, {
            'text':
            'Set up an escape route just in case',
            'moral_value':
            0,
            'capability_value':
            8,
            'next_scene':
            'end',
            'result':
            'Prepared for any scenario, you ensure a safe exit.'
        }]
    }
}, {
    'casino_entry': {
        'description':
        'You enter the bustling casino with a mission in mind, amidst glittering lights and the shuffling of cards.',
        'choices': [{
            'text':
            'Scout the casino for likely suspects',
            'moral_value':
            5,
            'capability_value':
            7,
            'next_scene':
            'table_game',
            'result':
            'You identify a few individuals who might be connected to DIABLO.'
        }, {
            'text':
            'Head directly to the high-stakes table',
            'moral_value':
            2,
            'capability_value':
            10,
            'next_scene':
            'table_game',
            'result':
            'The high-stakes table is where the action happens, you might catch someone important.'
        }, {
            'text':
            'Visit the bar to eavesdrop on conversations',
            'moral_value':
            3,
            'capability_value':
            5,
            'next_scene':
            'bar_scenario',
            'result':
            'You overhear snippets of shady dealings, possibly useful intel.'
        }]
    },
    'table_game': {
        'description':
        'Seated at the table, you eye your fellow players. The stakes are high, and so is the tension.',
        'choices': [{
            'text':
            'Play it safe and observe',
            'moral_value':
            6,
            'capability_value':
            4,
            'next_scene':
            'interrogation',
            'result':
            'Your cautious play earns you little attention but valuable insights.'
        }, {
            'text':
            'Take bold risks to win',
            'moral_value':
            2,
            'capability_value':
            9,
            'next_scene':
            'interrogation',
            'result':
            'Your aggressive strategy makes others nervous, revealing hidden connections.'
        }, {
            'text':
            'Sabotage another player subtly',
            'moral_value':
            -5,
            'capability_value':
            10,
            'next_scene':
            'deal_with_diablo',
            'result':
            "You subtly ruin a competitor's game, causing a noticeable stir."
        }]
    },
    'bar_scenario': {
        'description':
        'As you relax at the bar, snippets of conversation float by, one catching your attention.',
        'choices': [{
            'text':
            'Strike up a conversation with the bartender',
            'moral_value':
            7,
            'capability_value':
            5,
            'next_scene':
            'interrogation',
            'result':
            'The bartender shares some gossip, pointing you to a target.'
        }, {
            'text': 'Act inconspicuous and listen in',
            'moral_value': 4,
            'capability_value': 6,
            'next_scene': 'deal_with_diablo',
            'result': 'You gather intelligence with no one the wiser.'
        }, {
            'text':
            'Create a diversion to overhear secrets',
            'moral_value':
            -3,
            'capability_value':
            8,
            'next_scene':
            'casino_entry',
            'result':
            'In the chaos, several conversations reveal more than intended.'
        }]
    },
    'interrogation': {
        'description':
        "In a discreet room, you have your suspect. It's time for some answers.",
        'choices': [{
            'text':
            'Persuade them softly',
            'moral_value':
            8,
            'capability_value':
            4,
            'next_scene':
            'pursuit',
            'result':
            'Your gentle approach yields surprising cooperation.'
        }, {
            'text':
            'Use intimidation tactics',
            'moral_value':
            -6,
            'capability_value':
            7,
            'next_scene':
            'pursuit',
            'result':
            'Fear makes them spill partial truths; more work needed.'
        }, {
            'text':
            'Offer a bribe for their cooperation',
            'moral_value':
            -8,
            'capability_value':
            10,
            'next_scene':
            'end_game',
            'result':
            'Money talks, and it reveals hidden paths in the DIABLO network.'
        }]
    },
    'deal_with_diablo': {
        'description':
        "You know DIABLO's watching. Your next move could be a game-changer.",
        'choices': [{
            'text':
            'Double-cross DIABLO for the agency',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'pursuit',
            'result':
            'Your risky play rewards the mission, despite personal risk.'
        }, {
            'text':
            'Join DIABLO for personal gain',
            'moral_value':
            -10,
            'capability_value':
            12,
            'next_scene':
            'end_game',
            'result':
            'Aligning with DIABLO strengthens your position in the shadows.'
        }, {
            'text':
            'Negotiate a truce with DIABLO',
            'moral_value':
            0,
            'capability_value':
            8,
            'next_scene':
            'end_game',
            'result':
            'A tentative peace is brokered, serving both sides—temporarily.'
        }]
    }
}, {
    'casino': {
        'description':
        'You are in a bustling casino. A bead of sweat trickles down the face of an elderly gentleman opposite you at the poker table. ',
        'choices': [{
            'text': 'Focus on the game to win the pot.',
            'moral_value': 0,
            'capability_value': 5,
            'next_scene': 'infiltration',
            'result': 'You manage to win the pot, drawing attention.'
        }, {
            'text': 'Throw the game to maintain cover.',
            'moral_value': 5,
            'capability_value': 0,
            'next_scene': 'infiltration',
            'result': 'By losing purposefully, you avoid suspicion.'
        }, {
            'text':
            'Signal to the dealer for an advantage.',
            'moral_value':
            -5,
            'capability_value':
            3,
            'next_scene':
            'infiltration',
            'result':
            'With a discreet gesture, the odds are in your favor.'
        }]
    },
    'infiltration': {
        'description':
        'You move upstairs with the crowd none the wiser to your true mission: investigating DIABLO operations.',
        'choices': [{
            'text':
            'Access secured files using a stolen keycard',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'compound',
            'result':
            'With the keycard, you download crucial data from the server.'
        }, {
            'text':
            'Blackmail an executive for information',
            'moral_value':
            -15,
            'capability_value':
            15,
            'next_scene':
            'compound',
            'result':
            'The executive spills the secrets under pressure.'
        }, {
            'text': 'Make a discreet exit with minimal suspicion',
            'moral_value': 10,
            'capability_value': 5,
            'next_scene': 'compound',
            'result': 'You leave casually, leaving no trace behind.'
        }]
    },
    'compound': {
        'description':
        'The compound stretches ahead of you, its corridors filled with hidden dangers and opportunities.',
        'choices': [{
            'text':
            'Hack into the security system for an edge',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'showdown',
            'result':
            'You unlock passages and find critical blueprints.'
        }, {
            'text': 'Scout for enemy patrols and avoid detection',
            'moral_value': 5,
            'capability_value': 5,
            'next_scene': 'showdown',
            'result': 'You evade detection, learning their routine.'
        }, {
            'text':
            'Plant explosives to create a diversion',
            'moral_value':
            -15,
            'capability_value':
            10,
            'next_scene':
            'showdown',
            'result':
            'The explosion gives you the opportunity needed to proceed.'
        }]
    },
    'showdown': {
        'description':
        "The air is tense as you confront the DIABLO boss. This is the moment you've been waiting for.",
        'choices': [{
            'text':
            'Engage in a direct confrontation using brute force',
            'moral_value':
            -20,
            'capability_value':
            25,
            'next_scene':
            'denouement',
            'result':
            'A fierce battle ensues, but you come out on top.'
        }, {
            'text':
            'Negotiate a truce and gather intelligence',
            'moral_value':
            15,
            'capability_value':
            5,
            'next_scene':
            'denouement',
            'result':
            'You gain valuable intelligence after tense negotiations.'
        }, {
            'text':
            'Set an ambush for an unsuspecting operative',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'denouement',
            'result':
            'The ambush goes as planned, giving you the upper hand.'
        }]
    },
    'denouement': {
        'description':
        'The mission is concluding. The choices you made will determine your ultimate reward or consequence.',
        'choices': [{
            'text':
            'Report back to headquarters with the mission details',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'end',
            'result':
            'Your report is well-received, solidifying your reputation.'
        }, {
            'text':
            'Forge a new path with the intel acquired',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'end',
            'result':
            'Armed with new insights, you chart a bold new path.'
        }, {
            'text':
            'Hand the intel over to a third-party for personal gain',
            'moral_value':
            -15,
            'capability_value':
            15,
            'next_scene':
            'end',
            'result':
            'The transaction was lucrative, but at what cost?'
        }]
    }
}, {
    'casino_intro': {
        'description':
        "You find yourself seated at a high-stakes poker game in a bustling casino. Toppling stacks of chips and furtive glances hint at the underlying tension. You're not just here to play but to catch a killer.",
        'choices': [{
            'text':
            'Observe the German lady with the copper ring on her finger',
            'moral_value':
            2,
            'capability_value':
            5,
            'next_scene':
            'gather_information',
            'result':
            'You notice her discreetly signaling to someone across the room.'
        }, {
            'text':
            'Focus on winning the poker game',
            'moral_value':
            -1,
            'capability_value':
            7,
            'next_scene':
            'advance_to_vip_area',
            'result':
            'Your mind is solely on the game as you edge towards victory, inching closer to your true goal.'
        }]
    },
    'gather_information': {
        'description':
        "The casino's inherent chaos serves as a perfect cover for you to gather information about a DIABLO agent known as Angel, rumored to be here.",
        'choices': [{
            'text':
            'Eavesdrop on conversations nearby',
            'moral_value':
            3,
            'capability_value':
            4,
            'next_scene':
            'get_clues_on_angel',
            'result':
            "You pick up snippets of conversation mentioning the agent's alleged whereabouts."
        }, {
            'text':
            'Use your tech gadget to scan the area for signals',
            'moral_value':
            1,
            'capability_value':
            8,
            'next_scene':
            'locate_angel',
            'result':
            'Your gadget intercepts unusual chatter implicating someone in the crowd.'
        }]
    },
    'advance_to_vip_area': {
        'description':
        'With your poker earnings, you gain access to the exclusive VIP area of the casino, supposedly where high-profile targets meet.',
        'choices': [{
            'text':
            'Approach the poker game winner for information',
            'moral_value':
            1,
            'capability_value':
            3,
            'next_scene':
            'pursue_lead',
            'result':
            'The winner, seeing your intent, reluctantly shares a valuable lead.'
        }, {
            'text':
            'Blend into the crowd and observe the elite',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'spot_the_suspect',
            'result':
            'Your eyes catch a suspicious figure trying to remain inconspicuous.'
        }]
    },
    'get_clues_on_angel': {
        'description':
        "Using the information you've gathered, you try to piece together Angel's identity and intentions at the casino.",
        'choices': [{
            'text':
            'Confront a dubious-looking individual',
            'moral_value':
            -2,
            'capability_value':
            6,
            'next_scene':
            'angel_revelaed',
            'result':
            'The individual deflects and reveals they are an informant.'
        }, {
            'text':
            'Send a covert message to your handler',
            'moral_value':
            3,
            'capability_value':
            2,
            'next_scene':
            'await_response',
            'result':
            "Your handler confirms the target's identity and appearance."
        }]
    },
    'spot_the_suspect': {
        'description':
        'In the VIP area, a suspect catches your attention. Every second counts as you weigh your options.',
        'choices': [{
            'text':
            'Follow them discreetly out of the room',
            'moral_value':
            1,
            'capability_value':
            5,
            'next_scene':
            'vip_extraction',
            'result':
            'You tail them unnoticed and discover a plot unfurling.'
        }, {
            'text':
            'Alert security to the potential threat',
            'moral_value':
            2,
            'capability_value':
            3,
            'next_scene':
            'secure_the_area',
            'result':
            'Security pads the area, disrupting an emergent sinister plan.'
        }]
    }
}, {
    'casino_beginning': {
        'description':
        "A bead of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite you. He mops it away with a silk handkerchief and looks down again at the small island of chips in the green felt sea of the table. But, of course, you're here to catch a killer.",
        'choices': [{
            'text':
            'Maintain your cover by playing conservatively',
            'moral_value':
            5,
            'capability_value':
            2,
            'next_scene':
            'identifying_angel',
            'result':
            'You keep a low profile while gaining the trust of the players.'
        }, {
            'text':
            'Risk it all in a bold play',
            'moral_value':
            0,
            'capability_value':
            8,
            'next_scene':
            'identifying_angel',
            'result':
            'Your risky maneuver draws attention but could pay off.'
        }]
    },
    'identifying_angel': {
        'description':
        'New intelligence indicates a DIABLO agent known as Angel is among the casino crowd tonight.',
        'choices': [{
            'text':
            'Subtly observe the patrons',
            'moral_value':
            8,
            'capability_value':
            6,
            'next_scene':
            'confrontation_in_casino',
            'result':
            'You manage to identify Angel without raising suspicion.'
        }, {
            'text':
            'Confront a suspicious individual directly',
            'moral_value':
            -5,
            'capability_value':
            9,
            'next_scene':
            'confrontation_in_casino',
            'result':
            'Your confrontation is bold but risky, you attract unwanted attention.'
        }]
    },
    'confrontation_in_casino': {
        'description':
        'A tense atmosphere grips the casino as you prepare to confront Angel.',
        'choices': [{
            'text':
            'Attempt to arrest Angel discreetly',
            'moral_value':
            10,
            'capability_value':
            7,
            'next_scene':
            'casino_escape',
            'result':
            'You manage to subdue Angel quietly, limiting the chaos.'
        }, {
            'text':
            'Engage openly in a fight',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'casino_escape',
            'result':
            'A fight ensues, causing panic and chaos in the casino.'
        }]
    },
    'casino_escape': {
        'description':
        'With or without Angel, you must escape the casino amidst the brewing chaos.',
        'choices': [{
            'text':
            'Sneak out using the staff passage',
            'moral_value':
            7,
            'capability_value':
            5,
            'next_scene':
            'safe_house',
            'result':
            'You exit the casino without any further incident.'
        }, {
            'text': 'Make a daring escape through the main entrance',
            'moral_value': 0,
            'capability_value': 8,
            'next_scene': 'safe_house',
            'result': 'Your exit is flashy, attracting more attention.'
        }]
    },
    'safe_house': {
        'description':
        "You've reached a safe house where you can regroup and assess your next move.",
        'choices': [{
            'text':
            'Plan your next move with a calculated approach',
            'moral_value':
            15,
            'capability_value':
            10,
            'next_scene':
            'mission_debrief',
            'result':
            'Your strategic planning pays off as you prepare for the next phase.'
        }, {
            'text':
            'Take a break and gather your thoughts',
            'moral_value':
            0,
            'capability_value':
            3,
            'next_scene':
            'mission_debrief',
            'result':
            'A pause allows you to clear your mind but delays your plans.'
        }]
    }
}, {
    'casino_entrance': {
        'description':
        'As the suave Agent 180, you approach the glittering lights of the luxurious casino. Your mission is to identify and capture a DIABLO agent known as Angel.',
        'choices': [{
            'text':
            'Enter the casino and blend in with the crowd',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'gaming_floor',
            'result':
            'You manage to enter unnoticed and scan the room for potential threats.'
        }, {
            'text':
            'Attempt to sneak in through a side entrance',
            'moral_value':
            0,
            'capability_value':
            15,
            'next_scene':
            'side_corridor',
            'result':
            'You successfully find a hidden entrance, avoiding the main crowd.'
        }]
    },
    'gaming_floor': {
        'description':
        'The gaming floor is bustling with high rollers and shady deals. An elderly gentleman with a large pile of chips catches your eye.',
        'choices': [{
            'text':
            'Engage the elderly man in conversation to gather intel',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'poker_table',
            'result':
            'The man lets slip that a dangerous player is in the VIP section.'
        }, {
            'text':
            'Observe quietly from a distance',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'vip_section',
            'result':
            'You spot a familiar face making their way to the VIP area.'
        }]
    },
    'side_corridor': {
        'description':
        'The corridor is dimly lit, with doors leading to various offices and security rooms.',
        'choices': [{
            'text':
            'Disable a security system to avoid detection',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'security_room',
            'result':
            'You successfully disable the cameras, moving safely through the corridor.'
        }, {
            'text':
            'Proceed stealthily down the corridor',
            'moral_value':
            5,
            'capability_value':
            15,
            'next_scene':
            'office_b',
            'result':
            'Your stealth pays off, allowing you to bypass a patrolling guard.'
        }]
    },
    'poker_table': {
        'description':
        'The poker table is filled with intense players, each eyeing their opponents suspiciously.',
        'choices': [{
            'text':
            'Participate in the game to win a favor from an influential player',
            'moral_value':
            5,
            'capability_value':
            20,
            'next_scene':
            'vip_section',
            'result':
            'You win the game and earn a place in the VIP section.'
        }, {
            'text':
            "Secretly analyze player's interactions for clues",
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'gaming_floor',
            'result':
            "You gather valuable insights about the players' connections."
        }]
    },
    'vip_section': {
        'description':
        'The VIP section is exclusive and discretely luxurious, where deals go beyond monetary exchanges.',
        'choices': [{
            'text':
            'Initiate contact with a potential DIABLO agent',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'mission_climax',
            'result':
            "The exchange reveals critical information about Angel's plans."
        }, {
            'text':
            'Eavesdrop on a conversation between high-profile targets',
            'moral_value':
            0,
            'capability_value':
            15,
            'next_scene':
            'mission_climax',
            'result':
            'You overhear a discussion confirming the presence of Angel.'
        }]
    }
}, {
    'casino': {
        'description':
        "You're sitting in a bustling casino. An air of tension hangs as players wage fortunes over the cards.",
        'choices': [{
            'text':
            'Play the game discreetly, gathering intel',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'upstairs',
            'result':
            'Your subtle observations provide valuable insights.'
        }, {
            'text':
            'Accuse a player publicly to cause a distraction',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'chaos',
            'result':
            'Commotion ensues, giving you a brief window to act.'
        }, {
            'text':
            'Quietly slip from the table, unnoticed',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'escape_out',
            'result':
            'You manage to slip away without raising suspicion.'
        }]
    },
    'upstairs': {
        'description':
        "You've made it past the casino floor, reaching the more secure areas.",
        'choices': [{
            'text': 'Hack the security terminal',
            'moral_value': -10,
            'capability_value': 15,
            'next_scene': 'data_room',
            'result': 'Access granted to restricted information.'
        }, {
            'text': 'Sneak past the guards',
            'moral_value': 5,
            'capability_value': 10,
            'next_scene': 'labs',
            'result': 'You silently bypass the security checkpoints.'
        }]
    },
    'chaos': {
        'description':
        'The room erupts into chaos, a perfect cover for your next move.',
        'choices': [{
            'text': 'Blend into the shadows, avoiding detection',
            'moral_value': 0,
            'capability_value': 5,
            'next_scene': 'hidden_passage',
            'result': 'You remain unseen amidst the turmoil.'
        }, {
            'text':
            'Take advantage and plant a bug',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'planted_bug',
            'result':
            'The device is discreetly placed, capturing critical data.'
        }]
    },
    'labs': {
        'description':
        "You're now in the heart of the enemy's research division.",
        'choices': [{
            'text':
            'Investigate the experimental gadgets',
            'moral_value':
            0,
            'capability_value':
            15,
            'next_scene':
            'found_research',
            'result':
            "You've uncovered the secrets of their innovations."
        }, {
            'text': 'Sabotage their operations',
            'moral_value': -10,
            'capability_value': 25,
            'next_scene': 'sabotaged',
            'result': 'A critical blow dealt to their research.'
        }]
    },
    'escape_out': {
        'description':
        "With the intel in hand, it's time to make a swift exit.",
        'choices': [{
            'text': 'Dash to the emergency exit',
            'moral_value': 0,
            'capability_value': 5,
            'next_scene': 'freedom',
            'result': 'You manage a clean getaway.'
        }, {
            'text': 'Create a diversion using a small explosive',
            'moral_value': -15,
            'capability_value': 30,
            'next_scene': 'chaos_ensues',
            'result': 'The explosion buys you precious seconds.'
        }]
    }
}, {
    'casino_stakeout': {
        'description':
        'You find yourself at a bustling casino teeming with gamblers and potential suspects. Your mission is to identify an undercover agent from the DIABLO syndicate.',
        'choices': [{
            'text':
            'Blend in with the gamblers and observe quietly.',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'alley_confrontation',
            'result':
            "Your discretion pays off as you identify a suspicious individual matching the agent's description."
        }, {
            'text':
            'Confront a suspicious character directly.',
            'moral_value':
            -5,
            'capability_value':
            -15,
            'next_scene':
            'alley_confrontation',
            'result':
            'Your confrontation startles the suspect, leading to an unexpected chase.'
        }]
    },
    'alley_confrontation': {
        'description':
        'In the dimly lit alley behind the casino, the suspect stands before you, cornered but dangerous.',
        'choices': [{
            'text':
            'Try to talk him into surrendering peacefully.',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'interrogation_room',
            'result':
            'Your words persuade the suspect to lay down his arms.'
        }, {
            'text':
            'Engage in a physical confrontation.',
            'moral_value':
            -10,
            'capability_value':
            15,
            'next_scene':
            'interrogation_room',
            'result':
            'After a tough fight, you successfully apprehend the suspect.'
        }]
    },
    'interrogation_room': {
        'description':
        'The suspect sits in the interrogation room, silent and defiant. Your task is to extract crucial information.',
        'choices': [{
            'text':
            'Offer a deal for reduced charges in exchange for information.',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'corporate_espionage',
            'result':
            'The suspect agrees to talk, revealing a key location.'
        }, {
            'text':
            'Use psychological pressure to break their silence.',
            'moral_value':
            -5,
            'capability_value':
            10,
            'next_scene':
            'corporate_espionage',
            'result':
            'Under pressure, the suspect caves and spills everything they know.'
        }]
    },
    'corporate_espionage': {
        'description':
        'Infiltrating the corporation connected to DIABLO, you navigate through high-security corridors.',
        'choices': [{
            'text':
            'Hack into their security system for data access.',
            'moral_value':
            0,
            'capability_value':
            15,
            'next_scene':
            'rooftop_escape',
            'result':
            'You successfully access confidential files without raising alarms.'
        }, {
            'text':
            'Bribe an employee for inside information.',
            'moral_value':
            -5,
            'capability_value':
            5,
            'next_scene':
            'rooftop_escape',
            'result':
            'An employee reluctantly hands over sensitive data.'
        }]
    },
    'rooftop_escape': {
        'description':
        'On the rooftop, you must find a way to escape with the gathered information as DIABLO agents close in.',
        'choices': [{
            'text':
            'Use a zipline to escape to the neighboring building.',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'mission_complete',
            'result':
            'You zip line across the cityscape, escaping capture.'
        }, {
            'text':
            'Fight through the agents to reach a helicopter.',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'mission_complete',
            'result':
            'Despite heavy opposition, you make it to safety.'
        }]
    }
}, {
    'casino': {
        'description':
        'You find yourself at a busy casino, tasked with identifying the DIABLO agent known as Angel.',
        'choices': [{
            'text':
            'Blend in and observe carefully',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'meeting_room',
            'result':
            'You manage to gather some useful information without drawing attention.'
        }, {
            'text':
            'Try to approach Frau Bergmann for assistance',
            'moral_value':
            10,
            'capability_value':
            10,
            'next_scene':
            'exclusive_area',
            'result':
            'Bergmann agrees to help, and you gain access to restricted areas.'
        }, {
            'text': "Attempt to hack the casino's security to trace Angel",
            'moral_value': -5,
            'capability_value': 15,
            'next_scene': 'security_office',
            'result': 'You bypass the systems but risk exposure.'
        }]
    },
    'meeting_room': {
        'description':
        'In a meeting room, you confront the chaos of secretive dealings and espionage.',
        'choices': [{
            'text':
            'Confront a suspicious contact directly',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'interrogation_chamber',
            'result':
            'Your confrontation yields some information but makes enemies.'
        }, {
            'text':
            'Secretly plant surveillance devices',
            'moral_value':
            -5,
            'capability_value':
            8,
            'next_scene':
            'intelsuccess',
            'result':
            'The devices are in place, gathering vital information.'
        }, {
            'text':
            'Pose as another faction to gather intel',
            'moral_value':
            15,
            'capability_value':
            5,
            'next_scene':
            'protected',
            'result':
            'Your acting pays off, gaining trust and new intel.'
        }]
    },
    'security_office': {
        'description':
        "You've infiltrated the casino's security office, brimming with top-tier technology.",
        'choices': [{
            'text':
            'Download secret files and escape',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'data_bank',
            'result':
            'The files reveal significant secrets, but you leave traces.'
        }, {
            'text': 'Deactivate camera systems for stealth operations',
            'moral_value': 0,
            'capability_value': 15,
            'next_scene': 'back_hallways',
            'result': "You're now invisible to the eye of the law."
        }, {
            'text':
            'Set up a distraction to cover your tracks',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'sleekexit',
            'result':
            'A timed chaos helps your escape, but others are endangered.'
        }]
    },
    'exclusive_area': {
        'description':
        'A discreet, restricted area of the casino where important players meet.',
        'choices': [{
            'text':
            'Eavesdrop on a heated negotiation',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'negotiation',
            'result':
            "You gather crucial information on the opposition's strategies."
        }, {
            'text':
            'Join the conversation under a false identity',
            'moral_value':
            -15,
            'capability_value':
            20,
            'next_scene':
            'expose',
            'result':
            'Your disguise fools everyone, unlocking hidden agendas.'
        }, {
            'text':
            'Intercept a message delivery to learn more',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'interception',
            'result':
            'The intercepted message provides valuable leads.'
        }]
    },
    'intelsuccess': {
        'description':
        'Your planted devices have successfully captured critical dialogues.',
        'choices': [{
            'text':
            'Analyze the data in a safehouse',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'analysis',
            'result':
            'The safe environment lets you connect the dots without risk.'
        }, {
            'text':
            'Sell the intel to the highest bidder',
            'moral_value':
            -20,
            'capability_value':
            25,
            'next_scene':
            'deal_gone_wrong',
            'result':
            'You make a fortune, but at the cost of your conscience.'
        }, {
            'text':
            'Share insights with your agency for strategic planning',
            'moral_value':
            15,
            'capability_value':
            10,
            'next_scene':
            'agency_network',
            'result':
            'The agency uses the insights to dismantle enemy operations.'
        }]
    }
}, {
    'casino_ep4': {
        'description':
        "You're at a bustling casino with a mission to identify a key DIABLO agent.",
        'choices': [{
            'text':
            'Blend in and gather intel from the crowd.',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'vip_room_access',
            'result':
            'You overhear crucial details about a secret meeting.'
        }, {
            'text':
            'Hack into the security system for surveillance data.',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'security_breach',
            'result':
            'You gain access to camera feeds throughout the casino.'
        }, {
            'text':
            'Confront the suspicious high rollers directly.',
            'moral_value':
            0,
            'capability_value':
            20,
            'next_scene':
            'high_stakes_showdown',
            'result':
            "You have everyone's attention, for better or worse."
        }]
    },
    'vip_room_access': {
        'description':
        "You've managed to sneak into the VIP room, where the stakes are higher.",
        'choices': [{
            'text':
            'Pose as a wealthy gambler to eavesdrop.',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'vip_room_intel',
            'result':
            'You gain valuable information while keeping a low profile.'
        }, {
            'text': 'Start a conversation with the bartender.',
            'moral_value': 10,
            'capability_value': 5,
            'next_scene': 'bartender_confidant',
            'result': 'The bartender shares some intriguing rumors.'
        }, {
            'text':
            'Plant a listening device under the table.',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'device_planted',
            'result':
            'You now have a bug in place to monitor future conversations.'
        }]
    },
    'high_stakes_showdown': {
        'description':
        'Face-to-face with potential DIABLO agents, tensions are high.',
        'choices': [{
            'text': 'Challenge them to a game to gather more clues.',
            'moral_value': 5,
            'capability_value': 15,
            'next_scene': 'game_of_wits',
            'result': 'Winning their respect might open doors.'
        }, {
            'text': 'Bluff to force a confession.',
            'moral_value': 0,
            'capability_value': 20,
            'next_scene': 'bluff_called',
            'result': 'They start to crack under the pressure.'
        }]
    },
    'security_breach': {
        'description':
        "You've hacked into the casino's security network.",
        'choices': [{
            'text':
            'Download critical files for evidence.',
            'moral_value':
            -5,
            'capability_value':
            10,
            'next_scene':
            'data_downloaded',
            'result':
            'Files secured, containing possibly incriminating details.'
        }, {
            'text':
            'Spy on live footage for immediate threats.',
            'moral_value':
            0,
            'capability_value':
            8,
            'next_scene':
            'footage_review',
            'result':
            'You spot a known DIABLO operative entering the building.'
        }]
    }
}, {
    'casino_start': {
        'description':
        'Under the sparkling chandeliers of the Grand Casino, you find yourself seated at a poker table. Gear up to catch a high-profile DIABLO operative.',
        'choices': [{
            'text':
            'Play cautiously and observe the guests',
            'moral_value':
            5,
            'capability_value':
            8,
            'next_scene':
            'informant_meeting',
            'result':
            'You gather useful intel about a suspicious figure.'
        }, {
            'text':
            'Dive into the game to impress others',
            'moral_value':
            2,
            'capability_value':
            10,
            'next_scene':
            'informant_meeting',
            'result':
            'Your bold plays turn heads, and someone is paying attention.'
        }, {
            'text':
            'Tip the dealer for inside information',
            'moral_value':
            -5,
            'capability_value':
            5,
            'next_scene':
            'informant_meeting',
            'result':
            'The dealer spills a rumor about an important auction.'
        }]
    },
    'informant_meeting': {
        'description':
        "You've been given a lead - a backroom meeting with a crucial informant. The air is tense and thick with the scent of cigar smoke.",
        'choices': [{
            'text':
            'Listen carefully and take notes',
            'moral_value':
            10,
            'capability_value':
            10,
            'next_scene':
            'lab_breakin',
            'result':
            'You learn about a secret lab hidden in plain sight.'
        }, {
            'text':
            'Press the informant for more details',
            'moral_value':
            0,
            'capability_value':
            12,
            'next_scene':
            'lab_breakin',
            'result':
            'The informant is hesitant but reveals a potential entry point.'
        }, {
            'text':
            'Threaten them for cooperation',
            'moral_value':
            -10,
            'capability_value':
            15,
            'next_scene':
            'lab_breakin',
            'result':
            'Intimidation works; you get the secrets, but at a potential cost.'
        }]
    },
    'lab_breakin': {
        'description':
        "Under cover of night, you stand before the ominous entrance of Aegis Labs. It's time to infiltrate and uncover what lies within.",
        'choices': [{
            'text':
            'Utilize advanced tech to bypass security',
            'moral_value':
            10,
            'capability_value':
            20,
            'next_scene':
            'data_extraction',
            'result':
            'You smoothly disable the alarms without leaving a trace.'
        }, {
            'text':
            'Brute force your way inside',
            'moral_value':
            -15,
            'capability_value':
            25,
            'next_scene':
            'data_extraction',
            'result':
            "The alarms blare, but you're inside just in time."
        }, {
            'text':
            'Wait for a delivery and slip in',
            'moral_value':
            5,
            'capability_value':
            15,
            'next_scene':
            'data_extraction',
            'result':
            'You blend in with the delivery team and make it past the guards.'
        }]
    },
    'data_extraction': {
        'description':
        'Rows of blinking machinery greet you. The critical data files are encrypted and heavily protected.',
        'choices': [{
            'text':
            'Hack into the system using a decryption tool',
            'moral_value':
            10,
            'capability_value':
            25,
            'next_scene':
            'escape_route',
            'result':
            'The data is yours; your tech skills prove invaluable.'
        }, {
            'text':
            'Physically extract the hard drives',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'escape_route',
            'result':
            "It's a risky move, but you now have the evidence in hand."
        }, {
            'text':
            'Send a false signal to cover your activity',
            'moral_value':
            0,
            'capability_value':
            18,
            'next_scene':
            'escape_route',
            'result':
            'The security team is misled, and your tracks are covered.'
        }]
    },
    'escape_route': {
        'description':
        'Alarm bells echo as you make a swift decision. Your routes for escape are closing.',
        'choices': [{
            'text':
            'Exit through the rooftop and call for backup',
            'moral_value':
            10,
            'capability_value':
            15,
            'next_scene':
            'end',
            'result':
            'Extraction is a success, and the intel is secure.'
        }, {
            'text': 'Blend back with casino patrons unnoticed',
            'moral_value': 5,
            'capability_value': 10,
            'next_scene': 'end',
            'result': 'You slip past unnoticed, with nobody the wiser.'
        }, {
            'text':
            'Fight your way through the main exit',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'end',
            'result':
            'Your calculated aggression clears the path to freedom.'
        }]
    }
}, {
    'casino_start': {
        'description':
        "A bead of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite you. He mops it away with a silk handkerchief and looks down again at the small island of chips in the green felt sea of the table.You're here to catch a killer, not just play cards.",
        'choices': [{
            'text':
            'Attempt to win the poker game to gain access upstairs',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'upstairs_access',
            'result':
            'You win the game and earn access to the upstairs area.'
        }, {
            'text':
            'Try to bribe the dealer for information',
            'moral_value':
            -5,
            'capability_value':
            5,
            'next_scene':
            'dealer_bribe',
            'result':
            'The dealer accepts the bribe and gives you the information.'
        }, {
            'text': 'Observe the players for peculiar behavior',
            'moral_value': 0,
            'capability_value': 8,
            'next_scene': 'observe_players',
            'result': 'You notice someone acting strangely.'
        }]
    },
    'upstairs_access': {
        'description':
        "You have access to the private area of the casino where it's rumored that high-profile meetings occur.Keep an eye out for suspicious activities.",
        'choices': [{
            'text':
            'Eavesdrop on a conversation between two executives',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'executives_conversation',
            'result':
            'You gather crucial intel about their operations.'
        }, {
            'text': 'Search the rooms discreetly',
            'moral_value': -5,
            'capability_value': 15,
            'next_scene': 'search_rooms',
            'result': 'You find a key document in one of the offices.'
        }]
    },
    'dealer_bribe': {
        'description':
        'The dealer seems receptive to a little persuasion. It might just uncover what you need to know.',
        'choices': [{
            'text':
            'Bribe with a large sum for full cooperation',
            'moral_value':
            -15,
            'capability_value':
            20,
            'next_scene':
            'full_cooperation',
            'result':
            'Dealer spills everything and becomes an informant.'
        }, {
            'text':
            'Threaten the dealer for information',
            'moral_value':
            -20,
            'capability_value':
            5,
            'next_scene':
            'dealer_threat',
            'result':
            'The dealer, visibly shaken, gives minimal information.'
        }]
    },
    'observe_players': {
        'description':
        'Keeping a low profile, you observe the players at the table, noting their reactions and behavior.',
        'choices': [{
            'text': 'Notice a potential mark leaving the table nervously',
            'moral_value': 0,
            'capability_value': 5,
            'next_scene': 'follow_mark',
            'result': 'You decide to follow the mark out of curiosity.'
        }, {
            'text':
            'Engage in conversation with a woman who keeps eyeing you',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'engage_in_conversation',
            'result':
            'She provides a clue, seemingly aware of more than she lets on.'
        }]
    },
    'executives_conversation': {
        'description':
        'Listening intently, you overhear two executives discussing plans that hint at a sinister plot.',
        'choices': [{
            'text': 'Record the conversation for evidence',
            'moral_value': 8,
            'capability_value': 12,
            'next_scene': 'record_evidence',
            'result': 'You have a recording that could prove crucial.'
        }, {
            'text':
            'Confront them with the knowledge',
            'moral_value':
            -10,
            'capability_value':
            15,
            'next_scene':
            'direct_confrontation',
            'result':
            'They seem surprised, yet not entirely unprepared for confrontation.'
        }]
    }
}, {
    'casino': {
        'description':
        'You find yourself seated at a bustling casino, tasked with finding a dangerous DIABLO agent known as Angel.',
        'choices': [{
            'text':
            'Watch the elderly gentleman closely',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'identify_foe',
            'result':
            'He becomes uneasy, revealing more about his intentions.'
        }, {
            'text':
            'Charm Frau Bergmann for information',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'gather_info',
            'result':
            'She is impressed by your charm and decides to help.'
        }, {
            'text':
            "Try to identify Angel using the crowd's behavior",
            'moral_value':
            0,
            'capability_value':
            15,
            'next_scene':
            'identify_foe',
            'result':
            'You notice suspicious behavior that might point to Angel.'
        }]
    },
    'identify_foe': {
        'description':
        "In the dense crowd, you attempt to pinpoint Angel's identity using cues you've gathered.",
        'choices': [{
            'text':
            'Confront the suspected agent',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'confrontation',
            'result':
            'Tension rises as you approach the potential threat.'
        }, {
            'text':
            'Alert your backup to watch the suspect',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'backup_plan',
            'result':
            'Your team takes strategic positions ensuring your safety.'
        }, {
            'text':
            'Plant a tracking device discreetly',
            'moral_value':
            -10,
            'capability_value':
            15,
            'next_scene':
            'track_and_trace',
            'result':
            'You manage to successfully plant the device unnoticed.'
        }]
    },
    'gather_info': {
        'description':
        "Frau Bergmann shares valuable intel that could change the game's outcome.",
        'choices': [{
            'text':
            "Follow Bergmann's lead through the VIP section",
            'moral_value':
            5,
            'capability_value':
            20,
            'next_scene':
            'vip_access',
            'result':
            'You get exclusive access to crucial areas of the casino.'
        }, {
            'text':
            'Discuss your findings with Bergmann further',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'deepen_understanding',
            'result':
            'A clearer picture of the DIABLO network emerges.'
        }]
    },
    'confrontation': {
        'description':
        'The situation becomes tense as you confront a potential DIABLO operative.',
        'choices': [{
            'text': 'Engage in a tactical conversation',
            'moral_value': 0,
            'capability_value': 15,
            'next_scene': 'negotiation',
            'result': 'The agent begins to reveal useful information.'
        }, {
            'text':
            'Prepare for a physical altercation',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'physical_conflict',
            'result':
            'The situation escalates quickly into a confrontation.'
        }]
    }
}, {
    'casino_entrance': {
        'description':
        'You step into the bustling casino, lights flashing and the sound of coins clinking. Your mission is clear: identify the DIABLO agent known as Angel.',
        'choices': [{
            'text':
            'Blend into the crowd and observe',
            'moral_value':
            5,
            'capability_value':
            8,
            'next_scene':
            'poker_table',
            'result':
            'You blend into the crowd, carefully watching for any suspicious activity.'
        }, {
            'text':
            'Head directly to the VIP section',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'vip_section',
            'result':
            'You make your way toward the VIP section, drawing a few glances.'
        }, {
            'text':
            'Converse with the receptionist',
            'moral_value':
            2,
            'capability_value':
            4,
            'next_scene':
            'reception',
            'result':
            'The receptionist welcomes you warmly, offering additional insight into the guests.'
        }]
    },
    'poker_table': {
        'description':
        "The poker table is intense, with a mix of concentration and wealth exuding from the players. You're here under the guise of a fellow player.",
        'choices': [{
            'text':
            'Focus on the game to win the trust',
            'moral_value':
            3,
            'capability_value':
            10,
            'next_scene':
            'vip_access',
            'result':
            'You win a round with skillful play, gaining the attention of key players.'
        }, {
            'text':
            'Lose intentionally to gather intel',
            'moral_value':
            -2,
            'capability_value':
            3,
            'next_scene':
            'intel_gathering',
            'result':
            'Despite losing, you overhear crucial conversations.'
        }, {
            'text':
            'Accuse a player of cheating',
            'moral_value':
            -5,
            'capability_value':
            2,
            'next_scene':
            'table_conflict',
            'result':
            'A heated argument ensues, but you gain vital information amidst the chaos.'
        }]
    },
    'vip_section': {
        'description':
        'In the lavish VIP section, potential allies and enemies mingle. Your target could be nearby.',
        'choices': [{
            'text':
            'Join a conversation about art',
            'moral_value':
            4,
            'capability_value':
            4,
            'next_scene':
            'art_debate',
            'result':
            'You casually enter the discussion, building rapport with influential figures.'
        }, {
            'text':
            'Investigate the restricted access door',
            'moral_value':
            -1,
            'capability_value':
            7,
            'next_scene':
            'restricted_area',
            'result':
            'You approach the door subtly, noting its security features.'
        }, {
            'text':
            'Order an expensive drink to fit in',
            'moral_value':
            1,
            'capability_value':
            3,
            'next_scene':
            'drink_conversation',
            'result':
            'Your order draws a few nods of appreciation from those around you.'
        }]
    },
    'angel_identified': {
        'description':
        "You've identified Angel among the guests, their movements subtle but telling.",
        'choices': [{
            'text':
            'Confront Angel directly',
            'moral_value':
            -4,
            'capability_value':
            12,
            'next_scene':
            'confrontation',
            'result':
            'Tension rises as you face Angel, ready for a critical encounter.'
        }, {
            'text':
            'Report back to your handler',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'communication_hub',
            'result':
            'You relay the information, strategizing the next move.'
        }, {
            'text':
            'Tail Angel discreetly',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'trail_escape',
            'result':
            'You carefully follow, avoiding detection in the crowded venue.'
        }]
    },
    'final_showdown': {
        'description':
        'The operation is reaching its climax. Everything you have done leads to this point.',
        'choices': [{
            'text':
            'Launch a distraction for a surprise attack',
            'moral_value':
            -6,
            'capability_value':
            15,
            'next_scene':
            'attack_success',
            'result':
            'The chaos works in your favor; you advance with the upper hand.'
        }, {
            'text':
            'Negotiate terms with Angel',
            'moral_value':
            3,
            'capability_value':
            6,
            'next_scene':
            'negotiation_table',
            'result':
            'Angel listens as you propose a deal, the atmosphere thick with tension.'
        }, {
            'text':
            'Call for reinforcements',
            'moral_value':
            2,
            'capability_value':
            8,
            'next_scene':
            'backup_arrival',
            'result':
            'Backup is on the way, granting you a window to reassess.'
        }]
    }
}, {
    'casino_intro': {
        'description':
        'You enter the bustling casino, the sound of chips clinking and people chattering fills the air. Tonight, you’re tasked with uncovering the identity of a DIABLO agent.',
        'choices': [{
            'text':
            'Blend into the crowd and observe',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'poker_game',
            'result':
            'You manage to stay unnoticed while gathering useful intel.'
        }, {
            'text':
            'Jump straight into a poker game to get acquainted',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'poker_game',
            'result':
            "You quickly become a part of the casino's nightlife."
        }]
    },
    'poker_game': {
        'description':
        'Sitting at the poker table, you are up against three formidable players. The stakes are high, not just in chips.',
        'choices': [{
            'text':
            'Play aggressively to identify potential threats',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'uncover_angel',
            'result':
            'Your bold moves unsettle others, revealing small but crucial details.'
        }, {
            'text':
            'Play conservatively and wait for tells',
            'moral_value':
            5,
            'capability_value':
            8,
            'next_scene':
            'uncover_angel',
            'result':
            'Your patience yields insight into the player behaviors.'
        }]
    },
    'uncover_angel': {
        'description':
        'Amid the ongoing poker game, a lead points you to a mysterious player nicknamed Angel.',
        'choices': [{
            'text':
            'Confront Angel with your suspicions',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'confrontation_scene',
            'result':
            'The confrontation turns the table tense, but you learn valuable information.'
        }, {
            'text':
            'Secretly cooperate with another player to corner Angel',
            'moral_value':
            10,
            'capability_value':
            15,
            'next_scene':
            'confrontation_scene',
            'result':
            'Your teamwork smoothly isolates Angel for questioning.'
        }]
    },
    'confrontation_scene': {
        'description':
        'In a secluded area of the casino, you confront Angel with your findings.',
        'choices': [{
            'text':
            'Offer a deal in exchange for more information',
            'moral_value':
            -15,
            'capability_value':
            25,
            'next_scene':
            'information_exchange',
            'result':
            'Angel considers your offer, willing to trade for secrets.'
        }, {
            'text':
            'Press Angel hard for the truth',
            'moral_value':
            -5,
            'capability_value':
            10,
            'next_scene':
            'information_exchange',
            'result':
            'Under pressure, Angel reluctantly admits known discrepancies.'
        }]
    },
    'information_exchange': {
        'description':
        'Angel reveals a plot involving an internal breach within IIA ranks.',
        'choices': [{
            'text':
            'Report the information to your superior',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'conclusion',
            'result':
            'Your integrity ensures the information is dealt with in an official capacity.'
        }, {
            'text':
            'Keep the information and exploit it for leverage',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'conclusion',
            'result':
            'You decide to keep the info under wraps, using it as a strategic advantage.'
        }]
    }
}, {
    'casino': {
        'description':
        "A high-stakes game of poker is underway and you're in the midst of it. The tension is palpable as everyone waits for the final card.",
        'choices': [{
            'text':
            'Bluff your way to victory',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'hotel_suite',
            'result':
            'You successfully bluff and win the game, giving you access to the hotel suite.'
        }, {
            'text':
            'Play cautiously',
            'moral_value':
            5,
            'capability_value':
            8,
            'next_scene':
            'hotel_suite',
            'result':
            'You play it safe and manage to stay in the game, securing your position.'
        }, {
            'text':
            'Throw the game to avoid suspicion',
            'moral_value':
            0,
            'capability_value':
            -5,
            'next_scene':
            'bar',
            'result':
            'You deliberately lose, which avoids unwanted attention.'
        }]
    },
    'hotel_suite': {
        'description':
        'In the luxurious suite, you must search for clues about the DIABLO agent known as Angel. Every second counts.',
        'choices': [{
            'text':
            'Ransack the room for evidence',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'rooftop',
            'result':
            'You find crucial evidence while leaving the room in disarray.'
        }, {
            'text':
            'Search methodically and leave everything in place',
            'moral_value':
            10,
            'capability_value':
            10,
            'next_scene':
            'rooftop',
            'result':
            'You find some evidence without drawing attention to your presence.'
        }, {
            'text':
            'Plant false evidence to mislead',
            'moral_value':
            -15,
            'capability_value':
            5,
            'next_scene':
            'exit',
            'result':
            'The planted evidence misleads others chasing the wrong lead.'
        }]
    },
    'bar': {
        'description':
        "At the bar, you're able to mingle with guests. A chance for subtle interrogation or forming alliances.",
        'choices': [{
            'text': 'Befriend a local informant',
            'moral_value': 5,
            'capability_value': 10,
            'next_scene': 'back_alley',
            'result': 'You gain useful information from the informant.'
        }, {
            'text':
            'Challenge a rival agent openly',
            'moral_value':
            -10,
            'capability_value':
            15,
            'next_scene':
            'back_alley',
            'result':
            'Your bold move sparks tension but gains respect.'
        }, {
            'text':
            'Listen quietly for leads',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'back_alley',
            'result':
            'You pick up valuable intel by staying under the radar.'
        }]
    },
    'rooftop': {
        'description':
        'In pursuit across the rooftop, danger looms as you close in on Angel.',
        'choices': [{
            'text': 'Take a risky shortcut',
            'moral_value': -5,
            'capability_value': 20,
            'next_scene': 'confrontation',
            'result': 'You gain ground but at great personal risk.'
        }, {
            'text':
            'Follow the safe route',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'confrontation',
            'result':
            'You pace yourself, maintaining a cautious approach.'
        }, {
            'text': 'Signal for backup',
            'moral_value': 0,
            'capability_value': 15,
            'next_scene': 'confrontation',
            'result': 'Reinforcements are on their way to assist.'
        }]
    },
    'confrontation': {
        'description':
        'At the moment of truth, you face Angel with all secrets laid bare and a chance for resolution.',
        'choices': [{
            'text':
            'Negotiate with Angel',
            'moral_value':
            10,
            'capability_value':
            15,
            'next_scene':
            'end',
            'result':
            'You broker a tenuous peace with uncertain future implications.'
        }, {
            'text': 'Engage in a battle of wits',
            'moral_value': 0,
            'capability_value': 20,
            'next_scene': 'end',
            'result': 'You outsmart Angel, gaining the upper hand.'
        }, {
            'text': 'Take down Angel by force',
            'moral_value': -20,
            'capability_value': 25,
            'next_scene': 'end',
            'result': 'Victory is yours, but at a ethical cost.'
        }]
    }
}, {
    'casino_intro': {
        'description':
        'You find yourself in a bustling casino, tracking down a DIABLO agent known as Angel. The stakes at the table are high, but the stakes in this room are even higher.',
        'choices': [{
            'text':
            'Observe the card players for suspicious activity',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'casino_observation',
            'result':
            'Your keen eye notices subtle signals between players.'
        }, {
            'text':
            'Join the poker game to gather intel',
            'moral_value':
            0,
            'capability_value':
            7,
            'next_scene':
            'poker_game',
            'result':
            'You settle into the game, ready to play your cards right.'
        }, {
            'text':
            'Confront a player you suspect is Angel',
            'moral_value':
            -5,
            'capability_value':
            12,
            'next_scene':
            'confrontation',
            'result':
            'Calling out the wrong person could blow your cover.'
        }]
    },
    'casino_observation': {
        'description':
        'Hidden behind a column, you discreetly observe the players, watching for any slips of identity.',
        'choices': [{
            'text': 'Approach a known associate of Angel',
            'moral_value': 5,
            'capability_value': 8,
            'next_scene': 'associate',
            'result': 'The associate tightens at your approach, wary.'
        }, {
            'text':
            'Keep observing for patterns',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'hidden_patterns',
            'result':
            'You spot a curious exchange that reveals a potential lead.'
        }]
    },
    'poker_game': {
        'description':
        "The felt-lined table carries the air of competition. It's more than just chips at stake here.",
        'choices': [{
            'text':
            'Play aggressively to draw attention',
            'moral_value':
            -2,
            'capability_value':
            15,
            'next_scene':
            'accusation',
            'result':
            'Your bold moves raise eyebrows and signal recognition.'
        }, {
            'text': 'Play cautiously, blending in',
            'moral_value': 3,
            'capability_value': 5,
            'next_scene': 'success',
            'result': 'Your careful play keeps you in the game longer.'
        }]
    },
    'confrontation': {
        'description':
        "Ready to make your move, you stop beside a player seemingly connected to Angel's network.",
        'choices': [{
            'text': 'Go straight for an arrest',
            'moral_value': 0,
            'capability_value': -5,
            'next_scene': 'arrest',
            'result': 'Your hunch was abrupt, causing chaos.'
        }, {
            'text':
            'Engage in conversation to feel out their identity',
            'moral_value':
            2,
            'capability_value':
            8,
            'next_scene':
            'conversation',
            'result':
            'You gather subtle hints, confirming your suspicions.'
        }]
    },
    'associate': {
        'description':
        "Up close, the associate's behavior is telling. Are they the key to Angel?",
        'choices': [{
            'text':
            'Coerce information from them',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'uncover_identity',
            'result':
            'Your forceful approach yields vital information.'
        }, {
            'text':
            'Attempt to befriend them',
            'moral_value':
            5,
            'capability_value':
            7,
            'next_scene':
            'trust_build',
            'result':
            'A rapport is built, potentially leading to useful insight.'
        }]
    }
}, {
    'casino_entrance': {
        'description':
        'You find yourself at the bustling entrance of a high-stakes casino. The air is thick with anticipation, and somewhere within is a DIABLO agent you must find.',
        'choices': [{
            'text':
            'Blend into the crowd and observe your surroundings',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'casino_floor',
            'result':
            'You smoothly join the throng of people, taking in potential threats and points of interest.'
        }, {
            'text':
            'Head straight to the VIP area',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'vip_lounge',
            'result':
            'Your confidence gets you past the velvet rope, closer to where the high rollers gather.'
        }, {
            'text':
            'Attempt to bypass security through the service entrance',
            'moral_value':
            -10,
            'capability_value':
            15,
            'next_scene':
            'back_of_house',
            'result':
            "With a bit of cunning, you slip past the guards unnoticed into the casino's operational areas."
        }]
    },
    'casino_floor': {
        'description':
        'The casino floor is a dazzling array of slot machines, card tables, and people all focused on their games. Somewhere here, a dangerous game is also being played.',
        'choices': [{
            'text':
            'Play a hand of poker to gather information',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'poker_table',
            'result':
            'Your skillful play draws attention, and you overhear a conversation about Angel.'
        }, {
            'text':
            'Distract a high roller to sneak past a security barrier',
            'moral_value':
            -5,
            'capability_value':
            10,
            'next_scene':
            'private_room',
            'result':
            'With a deft move, you cause enough distraction to slip into the restricted area.'
        }, {
            'text':
            'Engage a dealer to gather insider information',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'dealer_bond',
            'result':
            'The dealer, charmed by your approach, hints at clandestine activities in the casino.'
        }]
    },
    'vip_lounge': {
        'description':
        'The VIP lounge is quieter, but the stakes feel infinitely higher. Powerful figures are engaged in covert discussions.',
        'choices': [{
            'text':
            'Eavesdrop on a suspicious-looking group',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'eavesdrop_success',
            'result':
            'You catch snippets of a conversation about a planned meeting with Angel.'
        }, {
            'text':
            'Engage a potential ally in conversation',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'ally_encounter',
            'result':
            "Your charm works wonders, earning a potential ally's trust—and a crucial hint about the DIABLO operation."
        }, {
            'text':
            'Use a gadget to create a minor chaos',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'chaos_unleashed',
            'result':
            'The ensuing confusion allows you to access restricted information unnoticed.'
        }]
    },
    'back_of_house': {
        'description':
        'You navigate the maze of service corridors, where workers move unseen behind the glitzy facade of the casino.',
        'choices': [{
            'text':
            'Convince a worker to relay messages for you',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'worker_contact',
            'result':
            'The worker agrees, providing risky but valuable updates as events unfold.'
        }, {
            'text':
            'Hunt for a surveillance room for deeper insights',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'surveillance_room',
            'result':
            'You find the surveillance hub, gaining a clearer picture of Angel’s possible location.'
        }, {
            'text':
            "Tamper with the building's security systems",
            'moral_value':
            -15,
            'capability_value':
            25,
            'next_scene':
            'security_breach',
            'result':
            "Systems go haywire, potentially exposing Angel's hiding spots as guards scramble."
        }]
    },
    'poker_table': {
        'description':
        'At the poker table, the stakes are high and the players experienced. Winning here means more than just money.',
        'choices': [{
            'text':
            'Go all in to pressure the mysterious player',
            'moral_value':
            0,
            'capability_value':
            15,
            'next_scene':
            'all_in_result',
            'result':
            "The pressure reveals a hint of the player's connection to Angel."
        }, {
            'text':
            'Play conservatively to maintain your cover',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'conservative_game',
            'result':
            'You keep the mystery player comfortable, who then lets slip some valuable information.'
        }, {
            'text':
            'Cheat subtly to ensure you win',
            'moral_value':
            -10,
            'capability_value':
            20,
            'next_scene':
            'cheat_victory',
            'result':
            "Your clever play earns you significant winnings and a better chance at revealing Angel's identity."
        }]
    }
}, {
    'casino': {
        'description':
        'In the dim light of a luxury casino, the air is thick with suspense. You are here for more than just the thrill of gambling – a DIABLO agent known as Angel may be on the premises.',
        'choices': [{
            'text':
            'Play it smart and blend in with the crowd',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'high_stakes_table',
            'result':
            'You blend in smoothly, making it less likely for anyone to suspect your real intentions.'
        }, {
            'text':
            'Approach the table where Angel is rumored to be',
            'moral_value':
            -5,
            'capability_value':
            8,
            'next_scene':
            'confrontation',
            'result':
            'You zero in on your target, but risk drawing attention to yourself.'
        }]
    },
    'high_stakes_table': {
        'description':
        'At the high-stakes poker table, tension is palpable. Across from you sits Frau Bergmann, her sharp eyes never missing a beat.',
        'choices': [{
            'text':
            'Bet aggressively to gather intel',
            'moral_value':
            5,
            'capability_value':
            9,
            'next_scene':
            'executive_office',
            'result':
            'Your bold moves draw interest, leading to whispers that may reveal Angel’s whereabouts.'
        }, {
            'text':
            'Fold early and observe',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'surveillance_room',
            'result':
            'By staying low, you overhear a critical piece of intelligence.'
        }]
    },
    'confrontation': {
        'description':
        "You've locked eyes with someone who matches Angel’s description. A confrontation is inevitable.",
        'choices': [{
            'text':
            'Identify and detain Angel',
            'moral_value':
            10,
            'capability_value':
            15,
            'next_scene':
            'interrogation',
            'result':
            'With quick thinking, you manage to restrain Angel without causing a scene.'
        }, {
            'text':
            'Attempt to discreetly gather more intel',
            'moral_value':
            5,
            'capability_value':
            12,
            'next_scene':
            'executive_office',
            'result':
            'Your stealth allows you to tail Angel, gathering more clues along the way.'
        }]
    },
    'executive_office': {
        'description':
        'Inside the executive office, secrets are buried deep. This is where Angel’s trail leads.',
        'choices': [{
            'text':
            'Search for classified documents',
            'moral_value':
            8,
            'capability_value':
            11,
            'next_scene':
            'clandestine_meeting',
            'result':
            'Documents hinting at a broader conspiracy fall into your hands.'
        }, {
            'text':
            'Set up surveillance equipment',
            'moral_value':
            7,
            'capability_value':
            13,
            'next_scene':
            'clandestine_meeting',
            'result':
            "You've established a feed, allowing insight into clandestine communications."
        }]
    },
    'interrogation': {
        'description':
        'Angel sits across the table, expression unreadable. This might be your only chance to extract information.',
        'choices': [{
            'text':
            'Apply pressure with promises of immunity',
            'moral_value':
            10,
            'capability_value':
            10,
            'next_scene':
            'finale',
            'result':
            'Tempted by your offer, Angel divulges vital information.'
        }, {
            'text':
            'Pursue aggressive interrogation techniques',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'clandestine_meeting',
            'result':
            'Under duress, Angel crumbles, offering critical intel while trembling with fear.'
        }]
    }
}, {
    'casino_intro': {
        'description':
        'A bead of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite you at the poker table. Frau Bergmann, a shrewd-eyed German lady, sits next to you, her fingers tapping on her cards.',
        'choices': [{
            'text':
            'Attempt to bluff your way to winning the poker game',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'identify_diablo_agent',
            'result':
            'You manage to win over the table, gaining access to the VIP section.'
        }, {
            'text':
            'Lose on purpose to study the players',
            'moral_value':
            5,
            'capability_value':
            -5,
            'next_scene':
            'identify_diablo_agent',
            'result':
            'Your losses are not in vain; you gather some valuable intel.'
        }, {
            'text':
            'Challenge Frau Bergmann to a higher stakes game',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'identify_diablo_agent',
            'result':
            'She accepts and you step into a game of cat and mouse.'
        }]
    },
    'identify_diablo_agent': {
        'description':
        'New intelligence puts a DIABLO agent known as Angel in the casino. You must identify them without raising your cover.',
        'choices': [{
            'text':
            'Observe the patrons quietly',
            'moral_value':
            10,
            'capability_value':
            0,
            'next_scene':
            'conflict_with_agent',
            'result':
            'You spot someone acting overly cautious—it could be Angel.'
        }, {
            'text':
            'Start a ruckus to see who reacts',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'conflict_with_agent',
            'result':
            'The chaos reveals several potential agents; one might be Angel.'
        }, {
            'text':
            'Approach the staff for information',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'conflict_with_agent',
            'result':
            'A sympathetic bartender provides a tip on a suspicious character.'
        }]
    },
    'conflict_with_agent': {
        'description':
        "You've located Angel, the DIABLO agent. A confrontation is inevitable.",
        'choices': [{
            'text': 'Engage in a firefight',
            'moral_value': -15,
            'capability_value': 20,
            'next_scene': 'escape_scene',
            'result': 'Bullets fly and you hope your cover holds.'
        }, {
            'text': 'Attempt to arrest them quietly',
            'moral_value': 15,
            'capability_value': 15,
            'next_scene': 'escape_scene',
            'result': 'You discreetly subdue Angel with minimal noise.'
        }, {
            'text':
            'Negotiate to extract information',
            'moral_value':
            20,
            'capability_value':
            5,
            'next_scene':
            'escape_scene',
            'result':
            'Angel, intrigued, leaks valuable intel in exchange for a deal.'
        }]
    },
    'escape_scene': {
        'description':
        'With the information gathered, you need to exit the casino without drawing attention.',
        'choices': [{
            'text': 'Flee the scene through a backdoor',
            'moral_value': 0,
            'capability_value': 10,
            'next_scene': 'debriefing',
            'result': 'You make a stealthy exit into the night.'
        }, {
            'text': 'Create a diversion with a fire alarm',
            'moral_value': -5,
            'capability_value': 15,
            'next_scene': 'debriefing',
            'result': 'In the chaos, you slip out undetected.'
        }, {
            'text': 'Blend into a crowd exiting the casino',
            'moral_value': 5,
            'capability_value': 0,
            'next_scene': 'debriefing',
            'result': 'You casually leave, unnoticed amidst guests.'
        }]
    },
    'debriefing': {
        'description':
        'You return for a debrief on your actions and the intel gathered.',
        'choices': [{
            'text': 'Report everything truthfully',
            'moral_value': 20,
            'capability_value': 0,
            'next_scene': 'end',
            'result': 'Your superiors commend your honesty.'
        }, {
            'text': 'Hold back some information',
            'moral_value': -10,
            'capability_value': 10,
            'next_scene': 'end',
            'result': 'You keep a strategic advantage for yourself.'
        }, {
            'text':
            'Fabricate parts of the story',
            'moral_value':
            -20,
            'capability_value':
            15,
            'next_scene':
            'end',
            'result':
            'Your superiors suspect nothing, but lies may follow you.'
        }]
    }
}, {
    'casino_start': {
        'description':
        'You find yourself at a poker table, the room filled with tense players. Your mission: identify a DIABLO agent known as Angel.',
        'choices': [{
            'text': 'Play the game to win information.',
            'moral_value': 5,
            'capability_value': 10,
            'next_scene': 'identify_angel',
            'result': 'You gather valuable intel on Angel.'
        }, {
            'text': 'Sabotage the game for quick results.',
            'moral_value': -10,
            'capability_value': 5,
            'next_scene': 'identify_angel',
            'result': 'You disrupt the game but draw attention.'
        }, {
            'text':
            'Withdraw to observe from afar.',
            'moral_value':
            0,
            'capability_value':
            3,
            'next_scene':
            'identify_angel',
            'result':
            'You remain unseen, quietly gathering information.'
        }]
    },
    'identify_angel': {
        'description':
        'With the information gathered, you hone in on Angel. The next move requires precision.',
        'choices': [{
            'text':
            'Confront Angel openly.',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'capture_angel',
            'result':
            'Angel acknowledges the confrontation but escapes.'
        }, {
            'text': 'Shadow Angel discreetly.',
            'moral_value': 5,
            'capability_value': 10,
            'next_scene': 'capture_angel',
            'result': 'You gather evidence while remaining undetected.'
        }]
    },
    'capture_angel': {
        'description':
        'You find Angel in a secluded area, the perfect spot to make a move.',
        'choices': [{
            'text': 'Apprehend Angel with force.',
            'moral_value': -10,
            'capability_value': 20,
            'next_scene': 'mission_complete',
            'result': 'Angel is captured, but not without a struggle.'
        }, {
            'text': 'Negotiate with Angel for cooperation.',
            'moral_value': 10,
            'capability_value': 5,
            'next_scene': 'mission_complete',
            'result': 'Angel agrees to cooperate for leniency.'
        }]
    },
    'mission_complete': {
        'description':
        "With Angel secured, the mission nears completion. It's time to report back and weigh your actions.",
        'choices': [{
            'text':
            'Report success without details.',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'debriefing',
            'result':
            'Your superiors are satisfied but lack full insight.'
        }, {
            'text': 'Report with full transparency.',
            'moral_value': 15,
            'capability_value': -5,
            'next_scene': 'debriefing',
            'result': 'Your honesty adds to your integrity.'
        }]
    },
    'debriefing': {
        'description':
        'Back at headquarters, you recount the mission details. Your actions determine your standing with the agency.',
        'choices': [{
            'text':
            'Justify your methods regardless of outcome.',
            'moral_value':
            -5,
            'capability_value':
            10,
            'next_scene':
            'end',
            'result':
            'Your resolve impresses your superiors despite controversial choices.'
        }, {
            'text': 'Accept feedback and adjust future strategies.',
            'moral_value': 10,
            'capability_value': 5,
            'next_scene': 'end',
            'result': 'Your adaptability earns respect and trust.'
        }]
    }
}, {
    'casino_infiltration': {
        'description':
        "A bead of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite you. He mops it away with a silk handkerchief and looks down again at the small island of chips in the green felt sea of the table. It's not just the merciless glare of the overhead lights that has him sweating. You're not here for games. You're here to catch a killer.",
        'choices': [{
            'text':
            'Continue the poker game and observe',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'gather_intelligence',
            'result':
            'You continue the poker game, aiming to gather more information from your surroundings.'
        }, {
            'text':
            'Excuse yourself to visit the bar',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'bar_interaction',
            'result':
            'You casually excuse yourself from the table and head towards the bar to assess the scene from another angle.'
        }]
    },
    'gather_intelligence': {
        'description':
        'New intelligence puts a DIABLO agent known as Angel here tonight. DIABLO is a global crime syndicate as dangerous as it is shadowy—if you can capture or at least get a positive ID on one of their top operatives, it may give the IIA the edge it needs.',
        'choices': [{
            'text':
            'Try to blend in and eavesdrop on conversations',
            'moral_value':
            7,
            'capability_value':
            15,
            'next_scene':
            'discovered_information',
            'result':
            'You seamlessly blend in with the crowd, picking up snippets of vital information.'
        }, {
            'text':
            'Approach known contacts for intel',
            'moral_value':
            0,
            'capability_value':
            20,
            'next_scene':
            'contact_meeting',
            'result':
            'You approach a contact discreetly, setting up a brief meeting for sensitive intel.'
        }]
    },
    'bar_interaction': {
        'description':
        'The bar is busy, the chatter of guests mixed with clinking glasses. As you approach, you notice several high-profile figures, any of whom could be Godfrey, the target.',
        'choices': [{
            'text':
            'Order a drink and engage the bartender',
            'moral_value':
            3,
            'capability_value':
            10,
            'next_scene':
            'bartender_info',
            'result':
            'The bartender nods knowingly, offering subtle hints of what he believes is unfolding tonight.'
        }, {
            'text':
            'Survey the room without drawing attention',
            'moral_value':
            5,
            'capability_value':
            5,
            'next_scene':
            'unknown_presence',
            'result':
            'Your nonchalant demeanor allows you to make note of a suspicious figure without alerting anyone.'
        }]
    },
    'unknown_presence': {
        'description':
        'A mysterious presence catches your attention, seemingly out of place amidst the lively crowd. Their behavior raises alarm.',
        'choices': [{
            'text':
            'Confront the suspicious figure',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'confrontation',
            'result':
            'Your abrupt confrontation rattles the figure, leading to a tense exchange.'
        }, {
            'text':
            'Notch another observation and move on',
            'moral_value':
            8,
            'capability_value':
            8,
            'next_scene':
            'further_investigation',
            'result':
            'You decide against immediate action, instead, noting their characteristics for later.'
        }]
    }
}, {
    'casino_intro': {
        'description':
        'You find yourself in a bustling casino, the air thick with smoke and tension. Your target, a DIABLO agent, is among the gamblers.',
        'choices': [{
            'text':
            'Blend in with the gamblers',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'identify_target',
            'result':
            'You manage to not draw any attention to yourself.'
        }, {
            'text':
            'Directly approach and confront',
            'moral_value':
            -5,
            'capability_value':
            15,
            'next_scene':
            'casino_security',
            'result':
            'Your direct approach causes a commotion, attracting security.'
        }, {
            'text':
            'Observe from a distance',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'target_leaves',
            'result':
            'You remain undetected and gather valuable intelligence.'
        }]
    },
    'identify_target': {
        'description':
        'Amongst the players, one stands out—a mysterious figure matching the description of your DIABLO target.',
        'choices': [{
            'text': 'Confirm their identity discreetly',
            'moral_value': 7,
            'capability_value': 10,
            'next_scene': 'approach_target',
            'result': 'You confirm the identity without alerting them.'
        }, {
            'text':
            'Use a gadget to scan for hidden weapons',
            'moral_value':
            0,
            'capability_value':
            20,
            'next_scene':
            'confront_target',
            'result':
            'The gadget reveals concealed weapons, marking them as the target.'
        }, {
            'text':
            'Distract them with a card trick',
            'moral_value':
            5,
            'capability_value':
            7,
            'next_scene':
            'gain_trust',
            'result':
            'The distraction works, allowing time for further observation.'
        }]
    },
    'casino_security': {
        'description':
        'Casino security approaches due to your actions. You need to act fast.',
        'choices': [{
            'text': "Explain it's a misunderstanding",
            'moral_value': 0,
            'capability_value': 5,
            'next_scene': 'released',
            'result': 'Security lets you go with a warning.'
        }, {
            'text':
            'Bribe them to look the other way',
            'moral_value':
            -10,
            'capability_value':
            5,
            'next_scene':
            'back_to_mission',
            'result':
            'With money in their pockets, security backs off.'
        }, {
            'text':
            'Take them out quietly',
            'moral_value':
            -20,
            'capability_value':
            25,
            'next_scene':
            'escape',
            'result':
            'You incapacitate the guards and make a quick exit.'
        }]
    },
    'target_leaves': {
        'description':
        'Your target leaves the casino. You must decide your next move.',
        'choices': [{
            'text': 'Follow them discreetly',
            'moral_value': 10,
            'capability_value': 15,
            'next_scene': 'street_chase',
            'result': 'You follow them without being noticed.'
        }, {
            'text': 'Plant a bug on their vehicle',
            'moral_value': 5,
            'capability_value': 20,
            'next_scene': 'track_target',
            'result': 'The bug successfully tracks their movement.'
        }, {
            'text': 'Intervene immediately',
            'moral_value': -5,
            'capability_value': 15,
            'next_scene': 'car_confrontation',
            'result': 'They notice your presence and try to escape.'
        }]
    },
    'gain_trust': {
        'description':
        'Having gained their trust, you now have an opportunity to learn more.',
        'choices': [{
            'text': "Ask them about DIABLO's plans",
            'moral_value': 10,
            'capability_value': 10,
            'next_scene': 'info_gathered',
            'result': 'They share some critical information.'
        }, {
            'text': 'Suggest cooperation',
            'moral_value': -5,
            'capability_value': 15,
            'next_scene': 'ally',
            'result': 'They agree to discuss further cooperation.'
        }, {
            'text': 'Attempt to recruit them as a double agent',
            'moral_value': -10,
            'capability_value': 20,
            'next_scene': 'double_agent',
            'result': 'They seem interested in your offer.'
        }]
    }
}, {
    'casino_table': {
        'description':
        'A bead of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite you. He mops it away with a silk handkerchief. Frau Bergmann, a German lady, watches the table shrewdly.',
        'choices': [{
            'text':
            'Continue playing the poker game to gather intelligence.',
            'moral_value':
            5,
            'capability_value':
            8,
            'next_scene':
            'find_agent_angel',
            'result':
            'You maintain your cover and glean some useful information.'
        }, {
            'text':
            'Attempt to cheat and gain an advantage.',
            'moral_value':
            -8,
            'capability_value':
            10,
            'next_scene':
            'find_agent_angel',
            'result':
            'You are able to cheat without being caught, earning a temporary advantage.'
        }, {
            'text':
            'Fold and observe the others.',
            'moral_value':
            3,
            'capability_value':
            5,
            'next_scene':
            'find_agent_angel',
            'result':
            'You fold your hand and closely observe the other players.'
        }]
    },
    'find_agent_angel': {
        'description':
        'New intelligence puts a DIABLO agent known as Angel here. Capture or identify them to gain an edge for the IIA.',
        'choices': [{
            'text':
            'Discreetly gather more information about Angel.',
            'moral_value':
            10,
            'capability_value':
            7,
            'next_scene':
            'capture_angel',
            'result':
            "Your subtlety pays off, as you gather crucial information about Angel's whereabouts."
        }, {
            'text':
            'Confront a suspicious individual directly.',
            'moral_value':
            -5,
            'capability_value':
            12,
            'next_scene':
            'capture_angel',
            'result':
            'Your brash approach puts you face-to-face with Angel, but it might compromise your mission.'
        }]
    },
    'capture_angel': {
        'description':
        "It's time to capture Angel and potentially disrupt DIABLO's plans.",
        'choices': [{
            'text':
            'Ambush Angel at an opportune moment.',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'end',
            'result':
            'Your well-timed ambush results in successfully capturing Angel.'
        }, {
            'text':
            'Set a trap and wait patiently.',
            'moral_value':
            8,
            'capability_value':
            9,
            'next_scene':
            'end',
            'result':
            'Your carefully laid trap is a success, and Angel falls right into it.'
        }]
    }
}, {
    'casino': {
        'description':
        "A bead of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite you. He mops it away with a silk handkerchief and looks down again at the small island of chips. The cards haven't been kind to him tonight. But you're not here for games. You're here to catch a killer.",
        'choices': [{
            'text':
            'Win the poker game',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'upper_floor',
            'result':
            'You win the game, securing your invitation to the upper floors.'
        }, {
            'text':
            'Fold your hand and observe',
            'moral_value':
            0,
            'capability_value':
            5,
            'next_scene':
            'casino_observation',
            'result':
            'You fold, keeping a low profile and gathering intel.'
        }, {
            'text':
            'Challenge the dealer',
            'moral_value':
            -5,
            'capability_value':
            8,
            'next_scene':
            'casino_interrogation',
            'result':
            'Your confrontation startles the dealer, leading to some unexpected truths.'
        }]
    },
    'upper_floor': {
        'description':
        'Inside the gleaming lobby of the upper floor, the real players of the underworld gather here. The stakes are higher, and so are the risks.',
        'choices': [{
            'text':
            'Blend in and listen',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'boardroom_meeting',
            'result':
            'You manage to overhear critical conversations without drawing attention.'
        }, {
            'text':
            'Approach a suspicious figure',
            'moral_value':
            2,
            'capability_value':
            5,
            'next_scene':
            'confront_figure',
            'result':
            'Your cautious approach allows a brief but telling exchange.'
        }, {
            'text': 'Look for security vulnerabilities',
            'moral_value': -2,
            'capability_value': 15,
            'next_scene': 'security_breach',
            'result': 'You find a way to exploit a security gap.'
        }]
    },
    'casino_observation': {
        'description':
        "Situated quietly, you scan the room. Everyone here is a potential ally or enemy, and you intend to find out who's who.",
        'choices': [{
            'text':
            'Eavesdrop on conversations',
            'moral_value':
            5,
            'capability_value':
            7,
            'next_scene':
            'intel_analysis',
            'result':
            'You gain valuable snippets about alliances forming.'
        }, {
            'text':
            'Spot patterns of suspicious activity',
            'moral_value':
            0,
            'capability_value':
            10,
            'next_scene':
            'pattern_exploration',
            'result':
            'Your keen eye catches an unusual pattern in guest movement.'
        }, {
            'text': 'Follow a known spy',
            'moral_value': -3,
            'capability_value': 12,
            'next_scene': 'spy_chase',
            'result': 'You tail the spy, uncovering their plot.'
        }]
    },
    'boardroom_meeting': {
        'description':
        'The boardroom echoes with discussions of power plays and dangerous deals. The tension is palpable.',
        'choices': [{
            'text':
            'Join the conversation',
            'moral_value':
            3,
            'capability_value':
            6,
            'next_scene':
            'negotiate_terms',
            'result':
            'Your insights are well-received, earning you unexpected allies.'
        }, {
            'text':
            'Stay silent and observe',
            'moral_value':
            1,
            'capability_value':
            4,
            'next_scene':
            'silent_watch',
            'result':
            'You remain undetected, absorbing the strategic talks.'
        }, {
            'text':
            'Disrupt the conversation',
            'moral_value':
            -4,
            'capability_value':
            10,
            'next_scene':
            'create_diversion',
            'result':
            'The disruption causes chaos, offering a chance to slip away.'
        }]
    },
    'security_breach': {
        'description':
        'Accessing the high-security areas, you walk a tightrope between breaking and entering—and being caught.',
        'choices': [{
            'text':
            'Use a gadget to disable alarms',
            'moral_value':
            -5,
            'capability_value':
            12,
            'next_scene':
            'infiltration',
            'result':
            'Your device works like a charm—or perhaps magic.'
        }, {
            'text':
            'Pick a lock with finesse',
            'moral_value':
            0,
            'capability_value':
            8,
            'next_scene':
            'critical_area',
            'result':
            'The lock yields to your touch, admitting you to the secrets within.'
        }, {
            'text':
            'Bluff your way past security',
            'moral_value':
            2,
            'capability_value':
            10,
            'next_scene':
            'security_check',
            'result':
            'Your charm thwarts suspicion, allowing you deeper access.'
        }]
    }
}, {
    'casino_poker': {
        'description':
        "A beads of sweat trickles down the weathered-oak face of the elderly gentleman sitting opposite. You're deep in a game of poker, with stakes higher than just monetary gain.",
        'choices': [{
            'text':
            'Win the poker game to get upstairs',
            'moral_value':
            5,
            'capability_value':
            10,
            'next_scene':
            'upper_floor',
            'result':
            'You skillfully win the poker hand, gaining entry to the more restricted areas.'
        }, {
            'text':
            'Throw the game for information',
            'moral_value':
            10,
            'capability_value':
            5,
            'next_scene':
            'upper_floor',
            'result':
            'You let the elderly player win, but gain valuable intelligence in return.'
        }, {
            'text':
            'Cheat to ensure victory',
            'moral_value':
            -10,
            'capability_value':
            15,
            'next_scene':
            'upper_floor',
            'result':
            'You tactically cheat your way to victory, unnoticed.'
        }]
    },
    'upper_floor': {
        'description':
        "Reaching the upper floor, you're confronted by a DIABLO agent. The tension is high, and every decision could mean life or death.",
        'choices': [{
            'text':
            'Engage the DIABLO agent in combat',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'combat_session',
            'result':
            'Initiating a fierce confrontation with the agent.'
        }, {
            'text':
            'Attempt to negotiate with the agent',
            'moral_value':
            10,
            'capability_value':
            10,
            'next_scene':
            'negotiation_standoff',
            'result':
            'Dialogue opens with the agent, testing your negotiation skills.'
        }, {
            'text':
            'Retreat for reinforcements',
            'moral_value':
            0,
            'capability_value':
            -5,
            'next_scene':
            'base_camp',
            'result':
            'You wisely decide to gather more intel and support before engaging.'
        }]
    },
    'combat_session': {
        'description':
        'The fists are flying, and gadgets are sparking in this sudden outburst of violence. Your reflexes are put to the test.',
        'choices': [{
            'text':
            'Use gadgets to disable the agent',
            'moral_value':
            5,
            'capability_value':
            15,
            'next_scene':
            'agent_defeated',
            'result':
            'Your gadgets work flawlessly, subduing the agent with minimal fuss.'
        }, {
            'text':
            'Outsmart with clever tactics',
            'moral_value':
            10,
            'capability_value':
            10,
            'next_scene':
            'agent_neutralized',
            'result':
            "Cunning ideas lead to the agent's downfall without a weapon."
        }, {
            'text':
            'Go all out with brute force',
            'moral_value':
            -5,
            'capability_value':
            20,
            'next_scene':
            'agent_defeated',
            'result':
            'Brute action leaves the agent incapacitated, though with collateral damage.'
        }]
    },
    'negotiation_standoff': {
        'description':
        'Words are your weapons as you engage in a mental duel with the agent, each sentence a strategic exchange.',
        'choices': [{
            'text':
            'Convince the agent to defect',
            'moral_value':
            15,
            'capability_value':
            5,
            'next_scene':
            'agent_allied',
            'result':
            'The agent finds your vision compelling, becoming a potential ally.'
        }, {
            'text':
            'Deceive the agent convincingly',
            'moral_value':
            -10,
            'capability_value':
            10,
            'next_scene':
            'agent_confused',
            'result':
            'Your deceit misleads the agent, giving you the strategic advantage.'
        }, {
            'text':
            'Provoke the agent into making a mistake',
            'moral_value':
            5,
            'capability_value':
            15,
            'next_scene':
            'agent_revealed',
            'result':
            "Provocation works and the agent's blunder gives away their plans."
        }]
    },
    'base_camp': {
        'description':
        "Back at the base, plans are laid out as strategies shift under the new intelligence you've gathered.",
        'choices': [{
            'text':
            'Plan a covert operation',
            'moral_value':
            10,
            'capability_value':
            10,
            'next_scene':
            'covert_mission',
            'result':
            'A precise and stealthy strategy is formed, promising minimal detection.'
        }, {
            'text':
            'Request backup for a full assault',
            'moral_value':
            0,
            'capability_value':
            20,
            'next_scene':
            'assault_prep',
            'result':
            'Reinforcements prepare for a calculated take-down mission.'
        }, {
            'text':
            'Dissuade from action, opting for diplomacy',
            'moral_value':
            15,
            'capability_value':
            5,
            'next_scene':
            'diplomatic_talks',
            'result':
            'Diplomatic channels open as negotiations are set to take precedence.'
        }]
    }
}]
base_scenarios = base_scenarios + []
