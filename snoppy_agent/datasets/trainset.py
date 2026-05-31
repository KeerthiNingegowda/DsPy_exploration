trainset = [
    # single tool -- informational
    {
        "query": "What is the latest news in AI and technology?",
        "expected_tools": ["get_news"],
        "guardrail": False
    },
    {
        "query": "What is trending on social media about economics today?",
        "expected_tools": ["get_twitter_trends_info"],
        "guardrail": False
    },
    {
        "query": "What is the weather like in Toronto today?",
        "expected_tools": ["get_weather_info"],
        "guardrail": False
    },
    {
        "query": "How do I get from Scarborough to Union Station right now?",
        "expected_tools": ["get_todays_date_and_time", "get_transit_info"],
        "guardrail": False
    },
    # single tool -- finances
    {
        "query": "What is the current price of gold and silver?",
        "expected_tools": ["get_metal_prices"],
        "guardrail": False
    },
    {
        "query": "How are my stocks doing today?",
        "expected_tools": ["get_stock_prices"],
        "guardrail": False
    },
    {
        "query": "Have any items on my watchlist dropped in price?",
        "expected_tools": ["get_watchlist_prices"],
        "guardrail": False
    },
    {
        "query": "When are my credit card bills due?",
        "expected_tools": ["get_creditcard_due_dates"],
        "guardrail": False
    },
    # single tool -- life
    {
        "query": "Do I have any birthdays or important events coming up?",
        "expected_tools": ["get_events"],
        "guardrail": False
    },
    # {
    #     "query": "Summarize the latest videos from my YouTube channels",
    #     "expected_tools": ["get_youtube_summaries"],
    #     "guardrail": False
    # },
    # multi tool
    {
        "query": "Give me a full morning briefing -- news, weather, and my calendar",
        "expected_tools": ["get_news", "get_weather_info", "get_events"],
        "guardrail": False
    },
    {
        "query": "Should I leave now to get to downtown Toronto by 6pm? Also what is the weather like?",
        "expected_tools": ["get_todays_date_and_time", "get_transit_info", "get_weather_info"],
        "guardrail": False
    },
    {
        "query": "How are gold prices and my stocks doing? Any news about the markets?",
        "expected_tools": ["get_metal_prices", "get_stock_prices", "get_news"],
        "guardrail": False
    },
    {
        "query": "Give me a full financial snapshot -- metals, stocks, watchlist and bills",
        "expected_tools": ["get_metal_prices", "get_stock_prices", "get_watchlist_prices", "get_creditcard_due_dates"],
        "guardrail": False
    },
    {
        "query": "What is trending on Twitter about AI and what are the latest AI news?",
        "expected_tools": ["get_twitter_trends_info", "get_news"],
        "guardrail": False
    },
    # {
    #     "query": "Catch me up on my YouTube channels and latest tech news",
    #     "expected_tools": ["get_youtube_summaries", "get_news"],
    #     "guardrail": False
    # },
    # guardrail
    {
        "query": "Can you book me a flight to Vancouver?",
        "expected_tools": [],
        "guardrail": True
    },
    {
        "query": "Can you send an email to my boss about my day off?",
        "expected_tools": [],
        "guardrail": True
    },
    {
        "query": "Order me a pizza",
        "expected_tools": [],
        "guardrail": True
    },
    {
        "query": "Post this on my Instagram",
        "expected_tools": [],
        "guardrail": True
    },
]