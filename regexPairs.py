"""
    ############################################################
    Regular expressions response pairs matching language patterns and responses
"""


"""
    ############################################################
    Identifying keywords for initiating extended chat
"""

keyword_regex_pairs = (
    (r'(?:uganthaya|madol doova|oliver twist|harry potter|gamperaliya)',
     "BOOK_ITM"),

    (r'(?:book|story book|novel|short story|magazine|newspaper)',
     "BOOK_TYP"),

    (r'(?:apple|tea|rice|water)',
     "FOOD_ITM"),

    (r'(?:food|drink|sweet|fruit|candy|desert|fruit)',
     "FOOD_TYP"),

    (r'(?:paracitamol|piriton|zitrecine|metfomin)',
     "MEDI_ITM"),

    (r'(?:medicine|drugs)',
     "MEDI_TYP")

)


"""
    ############################################################
    Extended chat feedback responses
"""

feedback_regex_pairs = (

    (r'BRING_FOOD_ITM_(.*)',
     ("%1 contains <NUT_FOOD> it is good for you to eat them",
      "%1 are good for preventing from <GOD_FOOD> and bad for <BAD_FOOD>")),

    (r'BRING_BOOK_ITM_(.*)',
     ("%1 is written by <AUT_BOOK>",
      "%1 is a <LAN_BOOK> <TYP_BOOK> by <AUT_BOOK> it is a good choice of reed")),

    (r'BRING_MEDI_ITM_(.*)',
     ("it seems you are not feeling well today",
      "%1 will make you feel better",
      "you better rest and take care of your self")),

    (r'READ_BOOK_ITM_(.*)',
     ("%1 is written by <AUT_BOOK>",
      "%1 is a <LAN_BOOK> <TYP_BOOK> by <AUT_BOOK> it is a good choice of reed"))

)


"""
    ############################################################
    Extended chat question responses
"""

question_regex_pairs = (

    (r'BRING_FOOD_TYP_(.*)',
     ("shall i bring your favourite %1 <FAV_FOOD> ",
      "you regularly eat <MEA_FOOD> shall i bring some",
      "what %1 should i bring",
      "shall i bring <MEA_FOOD>")),


    (r'BRING_BOOK_TYP_(.*)',
     ("what %1 should i bring",
      "shall i bring your favourite %1 <FAV_BOOK>",
      "you read <MRD_BOOK> again and again shall i bring that %1",
      "shall i bring the last read %1 <LRD_BOOK>")),

    (r'BRING_MEDI_TYP_(.*)',
     ("its good you reminded me",
      "how are you feeling now",
      "are you getting better now")),

    (r'READ_BOOK_TYP_(.*)',
     ("what %1 should i read",
      "shall i read <FAV_BOOK>",
      "you like <MRD_BOOK> shall i read that %1",
      "shall i read <LRD_BOOK> the last read %1"))

)


"""
    ############################################################
    Chat inputs and responses
"""

regex_pairs = (
    # 1
    (r'(?:good morning)',
     ("good morning", "good morning to you")),
    # 2
    (r'(?:good afternoon)',
     ("good afternoon", "good afternoon to you")),
    # 3
    (r'(?:good evening)',
     ("good evening", "good evening to you")),
    # 4
    (r'(?:good night)',
     ("good night", "good night to you")),
    # 5
    (r'(?:hi|hey)',
     ("hello", "hi", "hey", "hello how are you", "hi how are you", "hey how are you")),
    # 6
    (r'(?:bye|goodbye|cheerio)',
     ("bye", "goodbye", "cheerio", "take care", "bye, take care", "see you later", "catch you later")),
    # 7
    (r'(?:can you |could you |)(?:please |)bring (?:me |)(?:a |an |the |this |that |some |my |)(.*)',
     ("ok", "sure", "sure i will", "just give me a minute, ill bring", "ok give me a minute", "sure give me a minute",
      "give me a minute ill bring", "ill be right back")),
    # 8
    (r'(?:can you |could you |)(?:please |)(turn|switch) off (a|an|the) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 off %2 %3",
      "just give me a minute, ill turn on")),
    # 9
    (r'(?:can you |could you |)(?:please |)(?:turn|switch) on (a|an|the) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 on %2 %3",
      "just give me a minute, ill turn on")),
    # 10
    (r'(?:can you |could you |)(?:please |)(turn|switch) (a|an|the) (.*) off',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 off %2 %3",
      "just give me a minute, ill turn on")),
    # 11
    (r'(?:can you |could you |)(?:please |)(?:turn|switch) (a|an|the) (.*) on',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 on %2 %3",
      "just give me a minute, ill turn on")),
    # 12
    (r'(?:can you |could you |)(?:please |)move (?:the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill move",
      "just give me a minute, ill move")),
    # 13
    (r'(?:can you |could you |)(?:please |)call (?:the |this |that |)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill call",
      "just give me a minute, ill call")),
    # 14
    (r'(?:can you |could you |)(?:please |)(take|walk) me to (?:a|an|the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 you",
      "just give me a minute, ill %1 you")),
    # 15
    (r'(?:can you |could you |)(?:please |)wash (?:a|an|the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill wash",
      "just give me a minute, ill wash")),
    # 16
    (r'(?:can you |could you |)(?:please |)clean (?:a|an|the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill clean",
      "just give me a minute, ill clean")),
    # 17
    (r'(?:can you |could you |)(?:please |)brush my (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill brush",
      "just give me a minute, ill brush")),
    # 18
    (r'(?:can you |could you |)(?:please |)comb (?:the |this |that |my |)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill comb",
      "just give me a minute, ill comb")),
    # 19
    (r'(?:can you |could you |)(?:please |)read (?:me |)(?:a|an|the|this|that|)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill read",
      "just give me a minute, ill read")),
    # 20
    (r'(?:can you |could you |)(?:please |)rub (?:the |this |that |some |)(.*) on (?:the |this |that |my |)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill rub",
      "just give me a minute, ill rub")),
    # 21
    (r'(?:can you |could you |)(?:please |)help (?:me |)to (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute")),
    # 22
    (r'(please|ok|okay|sure|of course|certainly)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute")),
    # 23
    (r'i would like to (?:have|take)(?: my|) ([a-z]+) ([0-9]{1,2}) (minutes|hours) later(?: every day|)',
     ("ok are you sure you want to change %1 time", "sure are you sure you want to change %1 time")),
    # 24
    (r'i would like to (?:have|take)(?: my|) ([a-z]+) (?:at |by |)([0-9]{1,2}) ([0-9]{1,2})(?: every day|)',
     ("ok are you sure you want to change %1 time", "sure are you sure you want to change %1 time")),
    # 25
    (r'i would like to (?:have|take)(?: my|) ([a-z ]*medicine) ([0-9]{1,2}) (minutes|hours) later(?: every day|)',
     ("ok are you sure you want to change %1 time", "sure are you sure you want to change %1 time")),
    # 26
    (r'i would like to (?:have|take)(?: my|) ([a-z ]*medicine) (?:at |by |)([0-9]{1,2}) ([0-9]{1,2})(?: every day|)',
     ("ok are you sure you want to change %1 time", "sure are you sure you want to change %1 time")),
    # 27
    (r'i would like to (?:have|take) my ([a-z]+)(?: now|)',
     ("ok", "sure", "i will bring your %1", "sure i will bring your %1"))
)
