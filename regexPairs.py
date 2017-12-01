pairs = (

    (r'(?:can you |could you |)(?:please |)bring (?:me |)(?:a |an |the |this |that |some |my |)(.*)',
     ("ok", "sure", "sure i will", "just give me a minute, ill bring", "ok give me a minute", "sure give me a minute",
      "give me a minute ill bring", "ill be right back")),

    (r'(?:can you |could you |)(?:please |)(?:turn|switch) off (?:a|an|the) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 %2",
      "just give me a minute, ill turn on")),

    (r'(?:can you |could you |)(?:please |)(?:turn|switch) on (?:a|an|the) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 %2",
      "just give me a minute, ill turn on")),

    (r'(?:can you |could you |)(?:please |)move (?:the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill move",
      "just give me a minute, ill move")),

    (r'(?:can you |could you |)(?:please |)call (?:the |this |that |)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill call",
      "just give me a minute, ill call")),

    (r'(?:can you |could you |)(?:please |)(?:take|walk) me to (?:a|an|the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill %1 you",
      "just give me a minute, ill %1 you")),

    (r'(?:can you |could you |)(?:please |)wash (?:a|an|the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill wash",
      "just give me a minute, ill wash")),

    (r'(?:can you |could you |)(?:please |)clean (?:a|an|the|this|that) (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill clean",
      "just give me a minute, ill clean")),

    (r'(?:can you |could you |)(?:please |)brush my (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill brush",
      "just give me a minute, ill brush")),

    (r'(?:can you |could you |)(?:please |)comb (?:the |this |that |my |)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill comb",
      "just give me a minute, ill comb")),

    (r'(?:can you |could you |)(?:please |)read (?:me |)(?:a|an|the|this|that|)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill read",
      "just give me a minute, ill read")),

    (r'(?:can you |could you |)(?:please |)rub (?:the |this |that |some |)(.*) on (?:the |this |that |my |)(.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute", "give me a minute ill rub",
      "just give me a minute, ill rub")),

    (r'(?:can you |could you |)(?:please |)help (?:me |)to (.*)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute")),

    (r'(please|ok|okay|sure|of course|certainly)',
     ("ok", "sure", "sure i will", "ok give me a minute", "sure give me a minute")),

    (r'(?:can you |could you |)(?:please |)remind (?:me |)(?:in |by |)([0-9]{1,2}) (minutes|hours)(?: later|)(?: every day|)(?: please|)',
     ("ok", "sure", "sure i will")),

    (r'i would like to (?:have|take) my ([a-z]+) ([0-9]{1,2}) (minutes|hours) later(?: every day|)',
     ("ok", "sure", "sure i will")),

    (r'i would like to have(?: my|) ([a-z]+) (?:at |by |)([0-9]{1,2}) ([0-9]{1,2})(?: every day|)',
     ("ok", "sure", "sure i will")),

    (r'i would like to (?:have|take) my ([a-z ]*medicine) ([0-9]{1,2}) (minutes|hours) later(?: every day|)',
     ("ok", "sure", "sure i will")),

    (r'i would like to have(?: my|) ([a-z ]*medicine) (?:at |by |)([0-9]{1,2}) ([0-9]{1,2})(?: every day|)',
     ("ok", "sure", "sure i will")),

    (r'i would like to (?:have|take) my ([a-z]+)(?: now|)',
     ("ok", "sure", "i will bring your %1", "sure i will bring your %1"))
)
