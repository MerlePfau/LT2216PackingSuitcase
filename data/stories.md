## happy path 
* greet
  - utter_greeting
* request_game OR affirm
  - action_setup_game
  - slot{"used_words": ["shoes"]}
  - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets"]}
* add_word
  - action_extract_input
  - slot{"user_words":"I am packing my suitcase and I'm bringing shoes, pants and sunglasses."}
  - action_play
  - slot{"used_words": ["shoes", "pants"]}
  - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets"]} 
* add_word
  - action_extract_input
  - slot{"user_words":"I am packing my suitcase and I'm bringing shoes, pants and sunglasses."}
  - action_play
  - slot{"used_words": ["shoes", "pants"]}
  - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets"]} 

  
## sad path
* greet
  - utter_greeting
* deny
  - action_restart
* request_game OR affirm
  - action_setup_game
  - slot{"used_words": ["shoes"]}
  - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets"]}
* add_word
  - action_extract_input
  - slot{"user_words":"I am packing my suitcase and I'm bringing shoes, pants and sunglasses."}
  - action_play
  - slot{"used_words": ["shoes", "pants"]}
  - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets"]} 
  
  


## restart story
* greet
    - utter_greeting
* affirm
    - action_setup_game
    - slot{"used_words": ["a toothbrush"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets", "socks", "pajamas", "speakers", "toothpaste", "tissues", "multivitamins", "eye drops", "a book", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing a toothbrush and soap"}
    - action_play
    - slot{"used_words": ["a toothbrush", "soap", "jackets"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "socks", "pajamas", "speakers", "toothpaste", "tissues", "multivitamins", "eye drops", "a book", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing a toothbrush, soap, and"}
    - action_play
    - slot{"used_words": null}
    - slot{"possible_words": null}
* affirm
    - action_setup_game
    - slot{"used_words": ["multivitamins"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets", "socks", "pajamas", "speakers", "toothpaste", "tissues", "eye drops", "a toothbrush", "a book", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing multivitamins and food."}
    - action_play
    - slot{"used_words": ["multivitamins", "food", "a book"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets", "socks", "pajamas", "speakers", "toothpaste", "tissues", "eye drops", "a toothbrush", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing multivitamins, food, and a"}
    - action_play
    - slot{"used_words": null}
    - slot{"possible_words": null}
* affirm
    - action_setup_game
    - slot{"used_words": ["jackets"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "socks", "pajamas", "speakers", "toothpaste", "tissues", "multivitamins", "eye drops", "a toothbrush", "a book", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing multivitamins, food, and a"}
    - action_play
    - slot{"used_words": null}
    - slot{"possible_words": null}
* affirm
    - action_setup_game
    - slot{"used_words": ["jackets"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "socks", "pajamas", "speakers", "toothpaste", "tissues", "multivitamins", "eye drops", "a toothbrush", "a book", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing multivitamins and food."}
    - action_play
    - slot{"used_words": ["multivitamins", "food", "a book"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets", "socks", "pajamas", "speakers", "toothpaste", "tissues", "eye drops", "a toothbrush", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}

## interactive_story_2
* greet
    - utter_greeting
* affirm
    - action_setup_game
    - slot{"used_words": ["socks"]}
    - slot{"possible_words": ["shoes", "sunglasses", "shirts", "jackets", "pajamas", "speakers", "toothpaste", "tissues", "multivitamins", "eye drops", "a toothbrush", "a book", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* affirm
    - action_restart
* request_game OR affirm
    - action_setup_game
    - slot{"used_words": ["shoes"]}
    - slot{"possible_words": ["sunglasses", "shirts", "jackets", "socks", "pajamas", "speakers", "toothpaste", "tissues", "multivitamins", "eye drops", "a toothbrush", "a book", "a phone charger", "shampoo", "pants", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing shoes and soap."}
    - action_play
    - slot{"used_words": ["shoes", "soap", "pants"]}
    - slot{"possible_words": ["sunglasses", "shirts", "jackets", "socks", "pajamas", "speakers", "toothpaste", "tissues", "multivitamins", "eye drops", "a toothbrush", "a book", "a phone charger", "shampoo", "snacks", "water", "headphones"]}
* add_word
    - action_extract_input
    - slot{"user_words": "I'm packing a suitcase and I'm bringing shoes, soap, and pants."}
    - action_play
    - slot{"used_words": null}
    - slot{"possible_words": null}
