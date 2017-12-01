feedback_keyword_pairs = (

    (r'1_FOOD_ITM_(.*)',
     ("%1 contains <NUT_FOOD> it is good for you to eat them",
      "%1 are good for preventing from <GOD_FOOD> and bad for <BAD_FOOD>")),

    (r'1_BOOK_ITM_(.*)',
     ("%1 is written by <AUT_BOOK>",
      "%1 is a <LAN_BOOK> <TYP_BOOK> by <AUT_BOOK> it is a good choice of reed")),

    (r'1_MEDI_ITM_(.*)',
     ("it seems you are not feeling well today",
      "%1 will make you feel better",
      "you better rest and take care of your self")),

    (r'11_BOOK_ITM_(.*)',
     ("%1 is written by <AUT_BOOK>",
      "%1 is a <LAN_BOOK> <TYP_BOOK> by <AUT_BOOK> it is a good choice of reed"))

)
