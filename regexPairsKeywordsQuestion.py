question_keyword_pairs = (

    (r'1_FOOD_TYP_(.*)',
     ("shall i bring your favourite %1 <FAV_FOOD> ",
      "you regularly eat <MEA_FOOD> shall i bring some",
      "what %1 should i bring",
      "shall i bring <MEA_FOOD>")),


    (r'1_BOOK_TYP_(.*)',
     ("what %1 should i bring",
      "shall i bring your favourite %1 <FAV_BOOK>",
      "you read <MRD_BOOK> again and again shall i bring that %1",
      "shall i bring the last read %1 <LRD_BOOK>")),

    (r'1_MEDI_TYP_(.*)',
     ("its good you reminded me",
      "how are you feeling now",
      "are you getting better now")),

    (r'11_BOOK_TYP_(.*)',
     ("what %1 should i read",
      "shall i read <FAV_BOOK>",
      "you like <MRD_BOOK> shall i read that %1",
      "shall i read <LRD_BOOK> the last read %1"))

)
