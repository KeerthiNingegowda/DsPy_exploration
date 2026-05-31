testset = [
    {
        "query": "What is happening in geopolitics today?",
        "expected_tools": ["get_news"],
        "guardrail": False
    },
    {
        "query": "How do I get from Aurora GO to Union Station at 8am?",
        "expected_tools": ["get_transit_info"],
        "guardrail": False
    },
    {
        "query": "Is silver a good buy? What are people saying about it online?",
        "expected_tools": ["get_metal_prices", "get_twitter_trends_info"],
        "guardrail": False
    },
    {
        "query": "Do I have anything important this week and what is the weather like?",
        "expected_tools": ["get_events", "get_weather_info"],
        "guardrail": False
    },
    {
        "query": "Can you post on my Instagram for me?",
        "expected_tools": [],
        "guardrail": True
    },
    {
        "query": "What should I watch on Netflix tonight?",
        "expected_tools": [],
        "guardrail": True
    },
    # ambiguous -- could trigger wrong tools
    {
        "query": "Am I rich enough to go out today?",
        "expected_tools": ["get_metal_prices", "get_stock_prices", "get_creditcard_due_dates", "get_weather_info"],
        "guardrail": False
    },
    {
        "query": "Is today a good day?",
        "expected_tools": ["get_weather_info", "get_events", "get_news"],
        "guardrail": False
    },
    # implicit tool need -- agent must infer transit needs time
    {
        "query": "I need to be at Union Station by 9am, when should I leave from Scarborough?",
        "expected_tools": ["get_todays_date_and_time", "get_transit_info"],
        "guardrail": False
    },
    # multi domain -- agent must not miss any
    {
        "query": "Catch me up on everything I missed today",
        "expected_tools": ["get_news", "get_twitter_trends_info", "get_events", "get_metal_prices", "get_stock_prices"],
        "guardrail": False
    },
    # sounds like it needs tools but does not
    {
        "query": "Can you remind me to call my doctor tomorrow?",
        "expected_tools": [],
        "guardrail": True
    },
    # partial guardrail -- one part is in scope, one is not
    {
        "query": "What is the gold price today and can you buy some for me?",
        "expected_tools": ["get_metal_prices"],
        "guardrail": False
    },
    # sounds financial but needs news
    {
        "query": "Should I be worried about my investments given what is happening in the world?",
        "expected_tools": ["get_news", "get_metal_prices", "get_stock_prices"],
        "guardrail": False
    },
   # #learning intent
    # {
    #     "query": "What should I be studying this week based on my YouTube channels?",
    #     "expected_tools": ["get_youtube_summaries"],
    #     "guardrail": False
    # }
]