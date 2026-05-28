#Note:- Verifiable means if the response can be evaluated programmatically or not


trainset = [
    # Informational
    {
        "query": "What is the latest news in AI and technology?",
        "expected_tools": ["get_news"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": False
    },
    {
        "query": "What is trending on social media about economics today?",
        "expected_tools": ["get_twitter_trends_info"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": False
    },
    {
        "query": "What is the weather like in Toronto today?",
        "expected_tools": ["get_weather_info"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": True
    },
    {
        "query": "How do I get from Scarborough to Union Station right now?",
        "expected_tools": ["get_todays_date_and_time", "get_transit_info"],
        "ordered_dependencies": [["get_todays_date_and_time", "get_transit_info"]],
        "guardrail": False,
        "verifiable": True
    },
    # Finance
    {
        "query": "What is the current price of gold and silver?",
        "expected_tools": ["get_metal_prices"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": True
    },
    {
        "query": "How are stocks of my interests doing today?",
        "expected_tools": ["get_stock_prices"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": True
    },
    {
        "query": "Have any items on my watchlist dropped in price?",
        "expected_tools": ["get_watchlist_prices"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": False
    },
    {
        "query": "When are my credit card bills due?",
        "expected_tools": ["get_todays_date", "get_creditcard_due_dates"],
        "ordered_dependencies": [["get_todays_date", "get_creditcard_due_dates"]],
        "guardrail": False,
        "verifiable": True
    },
    # Life
    {
        "query": "Do I have any birthdays or important events coming up?",
        "expected_tools": ["get_todays_date", "get_events"],
        "ordered_dependencies": [["get_todays_date", "get_events"]],
        "guardrail": False,
        "verifiable": True
    },
    {
        "query": "Summarize the latest videos from my YouTube channels",
        "expected_tools": ["get_youtube_summaries"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": False
    },
    # Multi tool
    {
        "query": "Give me a full morning briefing -- news, weather, and my calendar",
        "expected_tools": ["get_news", "get_weather_info", "get_todays_date", "get_events"],
        "ordered_dependencies": [["get_todays_date", "get_events"]],
        "guardrail": False,
        "verifiable": False
    },
    {
        "query": "Should I leave now to get to downtown Toronto by 6pm? Also what is the weather like?",
        "expected_tools": ["get_todays_date_and_time", "get_transit_info", "get_weather_info"],
        "ordered_dependencies": [["get_todays_date_and_time", "get_transit_info"]],
        "guardrail": False,
        "verifiable": True
    },
    {
        "query": "How are gold prices and my stocks doing? Any news about the markets?",
        "expected_tools": ["get_metal_prices", "get_stock_prices", "get_news"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": True
    },
    # Guardrail
    {
        "query": "Can you book me a flight to Vancouver?",
        "expected_tools": [],
        "ordered_dependencies": [],
        "guardrail": True,
        "verifiable": False
    },
    {
        "query": "Can you send an email to my boss about my day off?",
        "expected_tools": [],
        "ordered_dependencies": [],
        "guardrail": True,
        "verifiable": False
    },
    {
        "query": "Order me a pizza",
        "expected_tools": [],
        "ordered_dependencies": [],
        "guardrail": True,
        "verifiable": False
    },
]
