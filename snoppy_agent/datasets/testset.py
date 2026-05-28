#Note:- Verifiable means if the response can be evaluated programmatically or not


testset = [
    {
        "query": "What is happening in geopolitics today?",
        "expected_tools": ["get_news"],
        "ordered_dependencies": [],
        "guardrail": False,
        "verifiable": False
    },
    # {
    #     "query": "How do I get from Aurora GO to Union Station at 8am tomorrow?",
    #     "expected_tools": ["get_todays_date_and_time", "get_transit_info"],
    #     "ordered_dependencies": [["get_todays_date_and_time", "get_transit_info"]],
    #     "guardrail": False,
    #     "verifiable": True
    # },
    # {
    #     "query": "Is silver a good buy this week? What are people saying about it on social media?",
    #     "expected_tools": ["get_metal_prices", "get_twitter_trends_info"],
    #     "ordered_dependencies": [],
    #     "guardrail": False,
    #     "verifiable": False
    # },
    # {
    #     "query": "Give me a full financial snapshot -- metals, stocks, watchlist and any upcoming bills",
    #     "expected_tools": ["get_metal_prices", "get_stock_prices", "get_watchlist_prices", "get_todays_date", "get_creditcard_due_dates"],
    #     "ordered_dependencies": [["get_todays_date", "get_creditcard_due_dates"]],
    #     "guardrail": False,
    #     "verifiable": True
    # },
    # {
    #     "query": "Can you post on my Instagram for me?",
    #     "expected_tools": [],
    #     "ordered_dependencies": [],
    #     "guardrail": True,
    #     "verifiable": False
    # },
]