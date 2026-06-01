accuracy_set = [
    {
        "query": "What is the current price of gold and silver in USD",
        "verify_items": ["gold price USD per gram", "silver price USD per gram"],
        "tools_needed": ["get_metal_prices"],
    },
    {
        "query": "How are VFV.TO, RY.TO, GOOGL and TSM doing today?",
        "verify_items": [
            "VFV.TO current price",
            "RY.TO current price",
            "GOOGL current price",
            "TSM current price",
        ],
        "tools_needed": ["get_stock_prices"],
    },
    {
        "query": "What is the current gold price and how are Canadian bank stocks doing?",
        "verify_items": [
            "gold price USD",
            "RY.TO price",
            "TD.TO price",
            "BMO.TO price",
        ],
        "tools_needed": ["get_metal_prices", "get_stock_prices"],
    },
    {
        "query": "Give me a full financial snapshot -- metals and my key stocks",
        "verify_items": ["gold price", "silver price", "VFV.TO price", "GOOGL price"],
        "tools_needed": ["get_metal_prices", "get_stock_prices"],
    },
]
