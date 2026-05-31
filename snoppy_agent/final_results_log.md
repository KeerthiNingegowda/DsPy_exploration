Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:43<00:00,  3.13s/it]
2026/05/31 00:36:14 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:36:14 INFO dspy.teleprompt.mipro_optimizer_v2: Default program score: 100.0

/home/keerthi/Desktop/DsPy_exploration/.venv/lib/python3.12/site-packages/dspy/teleprompt/mipro_optimizer_v2.py:646: ExperimentalWarning: Argument ``multivariate`` is an experimental feature. The interface can change in the future.
  sampler = optuna.samplers.TPESampler(seed=seed, multivariate=True)
2026/05/31 00:36:14 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 2 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:36:16,565 - INFO - Fetching the latest news information
2026-05-31 00:36:17,001 - INFO - Fetching information about twitter topics through Tavily
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:05<01:08,  5.29s/it]2026-05-31 00:36:19,666 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:36:19,695 - INFO - Fetching the latest news information
['get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:07<00:43,  3.59s/it]2026-05-31 00:36:21,907 - INFO - Getting weather info 
2026-05-31 00:36:23,349 - INFO - Fetching the latest news information
['get_events', 'get_events', 'get_events']
[***********           22%                       ]  4 of 18 completed['get_watchlist_prices']                                                                    | 3/14 [00:10<00:37,  3.41s/it]
[*********************100%***********************]  18 of 18 completed████▌                                                                                      | 4/14 [00:11<00:23,  2.32s/it]
[]
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:13<00:18,  2.01s/it]2026-05-31 00:36:27,340 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_twitter_trends_info', 'get_news']
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:14<00:13,  1.68s/it][]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:16<00:13,  1.97s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
[*********************100%***********************]  18 of 18 completed███████████████████████████████████████▏                                                   | 8/14 [00:16<00:08,  1.38s/it]
[*********************100%***********************]  18 of 18 completed
[]
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:18<00:07,  1.58s/it]['get_news', 'get_weather_info', 'get_events', 'get_events']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:25<00:12,  3.13s/it]2026-05-31 00:36:39,914 - INFO - Getting weather info 
['get_stock_prices', 'get_stock_prices']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:31<00:11,  3.94s/it]['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:33<00:06,  3.45s/it]['get_metal_prices', 'get_stock_prices', 'get_news', 'get_stock_prices', 'get_stock_prices', 'get_metal_prices']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:34<00:02,  2.83s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:37<00:00,  2.65s/it]
2026/05/31 00:36:51 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:36:51 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 3', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:36:51 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0]
2026/05/31 00:36:51 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:36:51 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:36:51 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 3 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:36:53,783 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:36:54,483 - INFO - Fetching the latest news information
2026-05-31 00:36:54,830 - INFO - file_cache is only supported with oauth2client<4.0.0
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:05<01:07,  5.23s/it]2026-05-31 00:36:56,473 - INFO - Fetching the latest news information
['get_events', 'get_events']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:07<00:44,  3.70s/it]2026-05-31 00:36:59,373 - INFO - Fetching the latest news information
2026-05-31 00:36:59,505 - INFO - Getting weather info 
['get_metal_prices', 'get_metal_prices']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:08<00:26,  2.41s/it]['get_watchlist_prices']
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:12<00:27,  2.77s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:12<00:17,  1.97s/it]2026-05-31 00:37:04,358 - INFO - file_cache is only supported with oauth2client<4.0.0
[]
[********              17%                       ]  3 of 18 completed[]████████████████████▊                                                                     | 6/14 [00:13<00:14,  1.75s/it]
[****************      33%                       ]  6 of 18 completed['get_creditcard_due_dates', 'get_creditcard_due_dates']                                    | 7/14 [00:15<00:11,  1.69s/it]
[*********************100%***********************]  18 of 18 completed███████████████████████████████████████▏                                                   | 8/14 [00:15<00:07,  1.21s/it]
[]
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:19<00:10,  2.06s/it]['get_news', 'get_weather_info', 'get_events', 'get_events']
[*********************100%***********************]  18 of 18 completed████████████████████████████████████████████████████████▎                                 | 10/14 [00:22<00:09,  2.46s/it]
['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices']
Average Metric: 10.00 / 11 (90.9%):  79%|█████████████████████████████████████████████████████████████████████████████████████████████▌                         | 11/14 [00:27<00:09,  3.03s/it]2026-05-31 00:37:19,048 - INFO - Getting weather info 
['get_metal_prices', 'get_stock_prices', 'get_news', 'get_stock_prices', 'get_stock_prices']
Average Metric: 11.00 / 12 (91.7%):  86%|██████████████████████████████████████████████████████████████████████████████████████████████████████                 | 12/14 [00:30<00:06,  3.08s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 12.00 / 13 (92.3%):  93%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:37<00:04,  4.24s/it]['get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices']
Average Metric: 13.00 / 14 (92.9%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:39<00:00,  2.85s/it]
2026/05/31 00:37:31 INFO dspy.evaluate.evaluate: Average Metric: 13.0 / 14 (92.9%)
2026/05/31 00:37:31 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 92.86 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 5', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 2'].
2026/05/31 00:37:31 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86]
2026/05/31 00:37:31 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:37:31 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:37:31 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 4 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:37:33,344 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:37:33,517 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:37:33,734 - INFO - Fetching the latest news information
[*****                 11%                       ]  2 of 18 completed2026-05-31 00:37:36,225 - INFO - Fetching the latest news information
[*********************100%***********************]  18 of 18 completed
[********              17%                       ]  3 of 18 completed2026-05-31 00:37:37,188 - INFO - Getting weather info 
[**********************67%*******                ]  12 of 18 completed[]
[*********************100%***********************]  18 of 18 completed                                                                                           | 1/14 [00:06<01:25,  6.56s/it]
['get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:06<00:34,  2.89s/it]['get_events']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:09<00:29,  2.65s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:13<00:33,  3.36s/it]['get_watchlist_prices', 'get_watchlist_prices']
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:13<00:20,  2.26s/it][]
Average Metric: 6.00 / 6 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:14<00:20,  2.26s/it]2026-05-31 00:37:45,624 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_creditcard_due_dates']
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:14<00:08,  1.26s/it][]
[*********************100%***********************]  18 of 18 completed███████████████████████████████████████▏                                                   | 8/14 [00:15<00:07,  1.29s/it]
[]
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:19<00:10,  2.02s/it]['get_metal_prices', 'get_stock_prices']
Average Metric: 9.00 / 10 (90.0%):  71%|█████████████████████████████████████████████████████████████████████████████████████▋                                  | 10/14 [00:23<00:10,  2.50s/it]['get_news', 'get_weather_info', 'get_events']
Average Metric: 10.00 / 11 (90.9%):  79%|█████████████████████████████████████████████████████████████████████████████████████████████▌                         | 11/14 [00:25<00:07,  2.45s/it]['get_metal_prices', 'get_stock_prices']
Average Metric: 10.00 / 12 (83.3%):  86%|██████████████████████████████████████████████████████████████████████████████████████████████████████                 | 12/14 [00:26<00:03,  1.84s/it]2026-05-31 00:38:00,374 - INFO - Getting weather info 
['get_stock_prices']
Average Metric: 11.00 / 13 (84.6%):  93%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:34<00:03,  3.73s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 12.00 / 14 (85.7%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:38<00:00,  2.73s/it]
2026/05/31 00:38:09 INFO dspy.evaluate.evaluate: Average Metric: 12.0 / 14 (85.7%)
2026/05/31 00:38:09 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 5', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:38:09 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71]
2026/05/31 00:38:09 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:38:09 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:38:09 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 5 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:38:11,891 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:38:13,578 - INFO - Fetching the latest news information
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:04<01:02,  4.82s/it]2026-05-31 00:38:14,976 - INFO - Fetching the latest news information
2026-05-31 00:38:17,204 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:38:17,865 - INFO - Getting weather info 
['get_metal_prices', 'get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:09<00:58,  4.88s/it][]
Average Metric: 3.00 / 3 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:09<00:58,  4.88s/it]2026-05-31 00:38:20,242 - INFO - Fetching the latest news information
['get_watchlist_prices', 'get_watchlist_prices']
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:11<00:23,  2.37s/it]['get_todays_date', 'get_events', 'get_events', 'get_events']
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:11<00:15,  1.74s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:12<00:10,  1.29s/it]2026-05-31 00:38:22,583 - INFO - file_cache is only supported with oauth2client<4.0.0
[]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:16<00:15,  2.25s/it]2026/05/31 00:38:29 ERROR dspy.utils.parallelizer: Error for Example({'query': 'Can you send an email to my boss about my day off?', 'expected_tools': [], 'guardrail': True, 'user_preferences': {'news_questions': ['What are top advancements in the field of AI?', 'World economy latest news today', 'Latest news related to trade and tariffs', 'What are recent news in American politics?', 'What are recent news in Canadian politics?', 'What are recent news in Indian politics?', 'Latest Geo-political relations between China, Russia, India, USA and EU', 'What are recent advancements in the field of semi-conductor technology?', 'Which companies are scehduled to go to IPO this week?', 'What are top venture capital firms from Silicon valley investing in?'], 'twitter_tavily': ['AI', 'Politics', 'Science and Technology', 'AGI', 'Vibe coding', 'Mass layoffs', 'Anthropic, OpenAI, Google, Nvidia, Deepseek'], 'weather_location': ['Toronto, Ontario, Canada', 'Vancouver, British Columbia, Canada', 'Bengaluru, Karnataka, India'], 'days_lookahead': 10, 'metal_tickers': ['GC=F', 'SI=F'], 'stock_tickers': ['VFV.TO', 'XQQ.TO', 'SPY', 'RY.TO', 'TD.TO', 'BNS.TO', 'BMO.TO', 'CNQ.TO', 'SU.TO', 'CVE.TO', 'ENB.TO', 'XEG.TO', 'SHEL', 'CVX', 'GOOGL', 'TSM', 'HMC', 'TM'], 'stock_period_of_interest': '3d', 'credit_card_bill_due_dates': {'Amex card payment due date': '15th of every month', 'Visa card payment due date': '10th of every month', 'Master card payment due date': '25th of every month'}, 'payday_info': {'frequency': 'Monthly', 'paydate': 'Last day of every month'}, 'watchlist_items': [{'item': 'Samsung 4K monitor 27 inch', 'threshold': 350}, {'item': 'Sony WH1000XM5 headphones', 'threshold': 200}, {'item': 'Atomic Habits hardcover book', 'threshold': 15.0}], 'transit_info': {'src': 'Oakville', 'dest': 'Union Station'}, 'channel_metadata': [{'name': '3Blue1Brown', 'channel_id': 'UCYO_jab_esuFRV4b17AJtAw'}, {'name': 'AndrejKarpathy', 'channel_id': 'UCXUPKJO5MZQN11PqgIvyuvQ'}, {'name': 'aiDotEngineer', 'channel_id': 'UCLKPca3kwwd-B59HNr-_lvA'}, {'name': 'LennysPodcast', 'channel_id': 'UC6t1O76G0jYXOAoYCm153dA'}]}, 'chat_history': ''}) (input_keys={'chat_history', 'user_preferences', 'query'}): litellm.RateLimitError: AnthropicException - {"type":"error","error":{"type":"rate_limit_error","message":"This request would exceed your organization's rate limit of 450,000 input tokens per minute (org: c134beea-4623-4f6b-9413-17fff8d2e28a, model: claude-haiku-4-5-20251001). For details, refer to: https://docs.claude.com/en/api/rate-limits. You can see the response headers for current usage. Reduce the prompt length or the maximum tokens requested, or try again later. View your current limits at https://console.anthropic.com/settings/limits. To raise this limit, purchase credits to advance to the next usage tier at https://console.anthropic.com/settings/billing."},"request_id":"req_011Cba2dCq8nktcEGCT3PLLR"}. Set `provide_traceback=True` for traceback.
Average Metric: 7.00 / 7 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:19<00:15,  2.56s/it]2026/05/31 00:38:29 ERROR dspy.utils.parallelizer: Error for Example({'query': 'Should I leave now to get to downtown Toronto by 6pm? Also what is the weather like?', 'expected_tools': ['get_todays_date_and_time', 'get_transit_info', 'get_weather_info'], 'guardrail': False, 'user_preferences': {'news_questions': ['What are top advancements in the field of AI?', 'World economy latest news today', 'Latest news related to trade and tariffs', 'What are recent news in American politics?', 'What are recent news in Canadian politics?', 'What are recent news in Indian politics?', 'Latest Geo-political relations between China, Russia, India, USA and EU', 'What are recent advancements in the field of semi-conductor technology?', 'Which companies are scehduled to go to IPO this week?', 'What are top venture capital firms from Silicon valley investing in?'], 'twitter_tavily': ['AI', 'Politics', 'Science and Technology', 'AGI', 'Vibe coding', 'Mass layoffs', 'Anthropic, OpenAI, Google, Nvidia, Deepseek'], 'weather_location': ['Toronto, Ontario, Canada', 'Vancouver, British Columbia, Canada', 'Bengaluru, Karnataka, India'], 'days_lookahead': 10, 'metal_tickers': ['GC=F', 'SI=F'], 'stock_tickers': ['VFV.TO', 'XQQ.TO', 'SPY', 'RY.TO', 'TD.TO', 'BNS.TO', 'BMO.TO', 'CNQ.TO', 'SU.TO', 'CVE.TO', 'ENB.TO', 'XEG.TO', 'SHEL', 'CVX', 'GOOGL', 'TSM', 'HMC', 'TM'], 'stock_period_of_interest': '3d', 'credit_card_bill_due_dates': {'Amex card payment due date': '15th of every month', 'Visa card payment due date': '10th of every month', 'Master card payment due date': '25th of every month'}, 'payday_info': {'frequency': 'Monthly', 'paydate': 'Last day of every month'}, 'watchlist_items': [{'item': 'Samsung 4K monitor 27 inch', 'threshold': 350}, {'item': 'Sony WH1000XM5 headphones', 'threshold': 200}, {'item': 'Atomic Habits hardcover book', 'threshold': 15.0}], 'transit_info': {'src': 'Oakville', 'dest': 'Union Station'}, 'channel_metadata': [{'name': '3Blue1Brown', 'channel_id': 'UCYO_jab_esuFRV4b17AJtAw'}, {'name': 'AndrejKarpathy', 'channel_id': 'UCXUPKJO5MZQN11PqgIvyuvQ'}, {'name': 'aiDotEngineer', 'channel_id': 'UCLKPca3kwwd-B59HNr-_lvA'}, {'name': 'LennysPodcast', 'channel_id': 'UC6t1O76G0jYXOAoYCm153dA'}]}, 'chat_history': ''}) (input_keys={'chat_history', 'user_preferences', 'query'}): litellm.RateLimitError: AnthropicException - {"type":"error","error":{"type":"rate_limit_error","message":"This request would exceed your organization's rate limit of 450,000 input tokens per minute (org: c134beea-4623-4f6b-9413-17fff8d2e28a, model: claude-haiku-4-5-20251001). For details, refer to: https://docs.claude.com/en/api/rate-limits. You can see the response headers for current usage. Reduce the prompt length or the maximum tokens requested, or try again later. View your current limits at https://console.anthropic.com/settings/limits. To raise this limit, purchase credits to advance to the next usage tier at https://console.anthropic.com/settings/billing."},"request_id":"req_011Cba2dCuMCw5GQ267EXKSE"}. Set `provide_traceback=True` for traceback.
Average Metric: 7.00 / 7 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:19<00:15,  2.56s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
[**********************89%******************     ]  16 of 18 completed['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_news']                  | 10/14 [00:20<00:06,  1.57s/it]
[*********************100%***********************]  18 of 18 completed████████████████████████████████████████████████████████████████▎                         | 11/14 [00:23<00:05,  1.85s/it]
['get_news', 'get_weather_info', 'get_events', 'get_events']
Average Metric: 10.00 / 10 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:30<00:06,  3.20s/it]['get_stock_prices', 'get_stock_prices', 'get_stock_prices']
Average Metric: 11.00 / 11 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:37<00:04,  4.17s/it]['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_stock_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 12.00 / 12 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:58<00:00,  4.18s/it]
2026/05/31 00:39:08 INFO dspy.evaluate.evaluate: Average Metric: 12.0 / 14 (85.7%)
2026/05/31 00:39:08 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 5', 'Predictor 1: Instruction 1', 'Predictor 1: Few-Shot Set 4'].
2026/05/31 00:39:08 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71]
2026/05/31 00:39:08 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:39:08 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:39:08 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 6 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:39:08,109 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:39:08,125 - INFO - Fetching the latest news information
2026-05-31 00:39:08,220 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:39:08,734 - INFO - Fetching the latest news information
['get_todays_date', 'get_events', 'get_events', 'get_events']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:02<00:33,  2.57s/it]2026-05-31 00:39:10,764 - INFO - Fetching the latest news information
[]
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:03<00:15,  1.33s/it]['get_metal_prices', 'get_metal_prices']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:03<00:09,  1.12it/s]['get_watchlist_prices', 'get_watchlist_prices']
[*********************100%***********************]  18 of 18 completed████▌                                                                                      | 4/14 [00:03<00:06,  1.45it/s]
2026-05-31 00:39:13,939 - INFO - Getting weather info 
[]
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:06<00:11,  1.30s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:06<00:07,  1.00it/s][]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:07<00:06,  1.16it/s]['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_stock_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:10<00:09,  1.53s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:10<00:05,  1.18s/it][]
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:13<00:06,  1.60s/it]['get_stock_prices', 'get_stock_prices', 'get_stock_prices']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:13<00:04,  1.39s/it]['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_news']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:14<00:02,  1.06s/it]2026-05-31 00:39:25,036 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:39:27,497 - INFO - Getting weather info 
['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:28<00:04,  4.99s/it]['get_news', 'get_weather_info', 'get_events', 'get_events']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:28<00:00,  2.04s/it]
2026/05/31 00:39:36 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:39:36 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 5', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 2'].
2026/05/31 00:39:36 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0]
2026/05/31 00:39:36 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:39:36 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:39:36 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 7 / 20 =====
2026-05-31 00:39:36,806 - INFO - Fetching the latest news information
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:39:36,832 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:39:36,839 - INFO - Fetching information about twitter topics through Tavily
[*********************100%***********************]  18 of 18 completed
[*********************100%***********************]  18 of 18 completed
['get_events']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:02<00:29,  2.29s/it]2026-05-31 00:39:39,609 - INFO - Fetching the latest news information
['get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:02<00:15,  1.31s/it]2026-05-31 00:39:39,947 - INFO - Getting weather info 
[]
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:03<00:11,  1.09s/it]['get_creditcard_due_dates']
[*********************100%***********************]  18 of 18 completed████▌                                                                                      | 4/14 [00:05<00:12,  1.25s/it]
[]
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:06<00:10,  1.15s/it][]
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:06<00:07,  1.11it/s]['get_watchlist_prices', 'get_watchlist_prices']
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:07<00:07,  1.03s/it]['get_metal_prices', 'get_stock_prices']
Average Metric: 7.00 / 8 (87.5%):  57%|█████████████████████████████████████████████████████████████████████▋                                                    | 8/14 [00:09<00:07,  1.21s/it][]
Average Metric: 8.00 / 9 (88.9%):  64%|██████████████████████████████████████████████████████████████████████████████▍                                           | 9/14 [00:09<00:04,  1.07it/s]['get_twitter_trends_info', 'get_news']
Average Metric: 9.00 / 10 (90.0%):  71%|█████████████████████████████████████████████████████████████████████████████████████▋                                  | 10/14 [00:10<00:02,  1.42it/s]2026-05-31 00:39:48,201 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_metal_prices', 'get_stock_prices']
Average Metric: 9.00 / 11 (81.8%):  79%|██████████████████████████████████████████████████████████████████████████████████████████████▎                         | 11/14 [00:13<00:04,  1.49s/it]2026-05-31 00:39:51,166 - INFO - Getting weather info 
['get_stock_prices']
Average Metric: 10.00 / 12 (83.3%):  86%|██████████████████████████████████████████████████████████████████████████████████████████████████████                 | 12/14 [00:15<00:03,  1.79s/it]['get_news', 'get_weather_info', 'get_events']
Average Metric: 11.00 / 13 (84.6%):  93%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:19<00:02,  2.46s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 12.00 / 14 (85.7%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:22<00:00,  1.57s/it]
2026/05/31 00:39:58 INFO dspy.evaluate.evaluate: Average Metric: 12.0 / 14 (85.7%)
2026/05/31 00:39:58 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 5', 'Predictor 1: Instruction 0', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:39:58 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71]
2026/05/31 00:39:58 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:39:58 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:39:58 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 8 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:40:00,942 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:40:02,832 - INFO - Fetching the latest news information
2026-05-31 00:40:04,293 - INFO - Fetching the latest news information
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:05<01:13,  5.66s/it]2026-05-31 00:40:07,221 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_metal_prices', 'get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:08<00:50,  4.22s/it][]
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:11<00:37,  3.38s/it]['get_watchlist_prices']
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:11<00:21,  2.14s/it]['get_events', 'get_events', 'get_events']
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:12<00:15,  1.72s/it]2026-05-31 00:40:11,564 - INFO - Getting weather info 
['get_twitter_trends_info', 'get_news']
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:13<00:12,  1.56s/it][]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:16<00:14,  2.01s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:17<00:10,  1.68s/it][]
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:17<00:05,  1.20s/it]2026-05-31 00:40:17,957 - INFO - file_cache is only supported with oauth2client<4.0.0
[*********************100%***********************]  18 of 18 completed
['get_metal_prices', 'get_stock_prices']
[*********************100%***********************]  18 of 18 completed███████████████████████████████████████████████████████▋                                  | 10/14 [00:24<00:11,  2.97s/it]
2026-05-31 00:40:25,176 - INFO - Getting weather info 
['get_news', 'get_weather_info', 'get_events', 'get_events']
Average Metric: 10.00 / 11 (90.9%):  79%|█████████████████████████████████████████████████████████████████████████████████████████████▌                         | 11/14 [00:30<00:11,  3.73s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 11.00 / 12 (91.7%):  86%|██████████████████████████████████████████████████████████████████████████████████████████████████████                 | 12/14 [00:35<00:08,  4.14s/it]['get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices']
Average Metric: 12.00 / 13 (92.3%):  93%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:37<00:03,  3.70s/it]['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices']
Average Metric: 13.00 / 14 (92.9%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:44<00:00,  3.21s/it]
2026/05/31 00:40:43 INFO dspy.evaluate.evaluate: Average Metric: 13.0 / 14 (92.9%)
2026/05/31 00:40:43 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 92.86 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 2', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 1'].
2026/05/31 00:40:43 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86]
2026/05/31 00:40:43 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:40:43 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:40:43 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 9 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:40:48,568 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:40:50,118 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_metal_prices']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:06<01:22,  6.38s/it][]
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:07<00:42,  3.51s/it]['get_events', 'get_events', 'get_events']
[*********************100%***********************]  18 of 18 completed                                                                                           | 3/14 [00:10<00:31,  2.88s/it]
[]
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:13<00:31,  3.14s/it]['get_watchlist_prices']
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:14<00:19,  2.21s/it][]
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:15<00:16,  2.01s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:16<00:11,  1.70s/it]2026-05-31 00:41:01,085 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_news']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:17<00:08,  1.48s/it][]
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:20<00:09,  1.85s/it]2026-05-31 00:41:09,109 - INFO - Fetching the latest news information
['get_twitter_trends_info', 'get_twitter_trends_info', 'get_news', 'get_news']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:26<00:12,  3.14s/it]['get_stock_prices', 'get_stock_prices', 'get_stock_prices']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:32<00:12,  4.05s/it]2026-05-31 00:41:22,487 - INFO - Getting weather info 
['get_todays_date_and_time', 'get_transit_info', 'get_transit_info', 'get_weather_info']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:40<00:10,  5.19s/it]['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:43<00:04,  4.47s/it]['get_todays_date_and_time', 'get_news', 'get_weather_info', 'get_events', 'get_events', 'get_news', 'get_news', 'get_weather_info', 'get_weather_info']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [01:00<00:00,  4.35s/it]
2026/05/31 00:41:44 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:41:44 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 0', 'Predictor 1: Instruction 0', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:41:44 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0]
2026/05/31 00:41:44 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:41:44 INFO dspy.teleprompt.mipro_optimizer_v2: ========================


2026/05/31 00:41:44 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 10 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:41:44,886 - INFO - Fetching the latest news information
2026-05-31 00:41:44,917 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:41:44,920 - INFO - file_cache is only supported with oauth2client<4.0.0
[*********************100%***********************]  18 of 18 completed
[*********************100%***********************]  18 of 18 completed
['get_metal_prices']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:02<00:35,  2.75s/it]2026-05-31 00:41:47,649 - INFO - Fetching the latest news information
['get_events']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:02<00:14,  1.22s/it][]
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:03<00:09,  1.16it/s]2026-05-31 00:41:48,663 - INFO - Fetching the latest news information
['get_creditcard_due_dates']
[****************      33%                       ]  6 of 18 completed[]███▌                                                                                      | 4/14 [00:05<00:12,  1.27s/it]
[*********************100%***********************]  18 of 18 completed█████████████▏                                                                             | 5/14 [00:05<00:08,  1.03it/s]
[]
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:06<00:07,  1.06it/s]2026-05-31 00:41:51,454 - INFO - Getting weather info 
[]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:08<00:09,  1.31s/it]2026-05-31 00:41:53,706 - INFO - Getting weather info 
['get_twitter_trends_info', 'get_news']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:09<00:06,  1.07s/it]['get_watchlist_prices', 'get_watchlist_prices']
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:10<00:06,  1.30s/it]['get_stock_prices']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:13<00:06,  1.67s/it]2026-05-31 00:42:01,008 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_todays_date_and_time', 'get_metal_prices', 'get_stock_prices', 'get_news']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:18<00:07,  2.63s/it]['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:20<00:05,  2.52s/it]['get_todays_date_and_time', 'get_weather_info', 'get_transit_info']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:26<00:03,  3.49s/it]['get_news', 'get_weather_info', 'get_events']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:32<00:00,  2.30s/it]
2026/05/31 00:42:17 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:42:17 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 0', 'Predictor 1: Instruction 1', 'Predictor 1: Few-Shot Set 4'].
2026/05/31 00:42:17 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0]
2026/05/31 00:42:17 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:42:17 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:42:17 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 11 / 20 =====
2026-05-31 00:42:17,124 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:42:17,139 - INFO - Fetching the latest news information
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:42:17,177 - INFO - file_cache is only supported with oauth2client<4.0.0
[*********************100%***********************]  18 of 18 completed
[*********************100%***********************]  18 of 18 completed
['get_events']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:02<00:34,  2.68s/it]2026-05-31 00:42:19,958 - INFO - Fetching the latest news information
[]
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:02<00:14,  1.19s/it]['get_metal_prices']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:03<00:08,  1.29it/s]2026-05-31 00:42:20,617 - INFO - Fetching the latest news information
['get_creditcard_due_dates']
[*********************100%***********************]  18 of 18 completed████▌                                                                                      | 4/14 [00:05<00:13,  1.39s/it]
[]
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:06<00:11,  1.23s/it][]
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:06<00:06,  1.18it/s]2026-05-31 00:42:23,652 - INFO - Getting weather info 
2026-05-31 00:42:26,322 - INFO - Getting weather info 
[]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:09<00:10,  1.50s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:10<00:08,  1.38s/it]['get_watchlist_prices', 'get_watchlist_prices']
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:10<00:05,  1.09s/it]['get_stock_prices']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:13<00:06,  1.50s/it]2026-05-31 00:42:33,113 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_todays_date_and_time', 'get_metal_prices', 'get_stock_prices', 'get_news']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:17<00:07,  2.39s/it]['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:22<00:06,  3.00s/it]['get_todays_date_and_time', 'get_weather_info', 'get_transit_info']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:26<00:03,  3.27s/it]['get_news', 'get_weather_info', 'get_events']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:32<00:00,  2.35s/it]
2026/05/31 00:42:50 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:42:50 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 0', 'Predictor 1: Instruction 0', 'Predictor 1: Few-Shot Set 2'].
2026/05/31 00:42:50 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0]
2026/05/31 00:42:50 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:42:50 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:42:50 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 12 / 20 =====
2026-05-31 00:42:50,122 - INFO - Fetching information about twitter topics through Tavily
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:42:50,149 - INFO - Fetching the latest news information
2026-05-31 00:42:50,177 - INFO - Fetching the latest news information
2026-05-31 00:42:50,203 - INFO - file_cache is only supported with oauth2client<4.0.0
[*********************100%***********************]  18 of 18 completed
2026-05-31 00:42:52,764 - INFO - Fetching the latest news information
['get_events', 'get_events', 'get_events']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:03<00:39,  3.01s/it][]
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:03<00:15,  1.30s/it]['get_metal_prices']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:04<00:12,  1.13s/it]2026-05-31 00:42:55,533 - INFO - Getting weather info 
['get_creditcard_due_dates', 'get_creditcard_due_dates']
[*********************100%***********************]  18 of 18 completed████▌                                                                                      | 4/14 [00:05<00:12,  1.26s/it]
[]
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:06<00:10,  1.18s/it][]
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:07<00:09,  1.21s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:10<00:10,  1.53s/it][]
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:10<00:06,  1.13s/it]2026-05-31 00:43:01,392 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_watchlist_prices']
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:11<00:05,  1.09s/it]['get_stock_prices', 'get_stock_prices']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:14<00:06,  1.67s/it]2026-05-31 00:43:07,669 - INFO - Getting weather info 
['get_metal_prices', 'get_stock_prices', 'get_news', 'get_metal_prices', 'get_metal_prices', 'get_stock_prices']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:19<00:08,  2.84s/it]['get_news', 'get_weather_info', 'get_events', 'get_events']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:22<00:05,  2.79s/it]['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:24<00:02,  2.57s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:26<00:00,  1.92s/it]
2026/05/31 00:43:17 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:43:17 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 3', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 3'].
2026/05/31 00:43:17 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0]
2026/05/31 00:43:17 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:43:17 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:43:17 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 13 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:43:19,136 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:43:19,876 - INFO - Fetching information about twitter topics through Tavily
[*********************100%***********************]  18 of 18 completed
2026-05-31 00:43:22,494 - INFO - Fetching the latest news information
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:06<01:19,  6.08s/it]['get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:06<00:32,  2.67s/it]2026-05-31 00:43:24,624 - INFO - Fetching the latest news information
['get_events']
[*********************100%***********************]  18 of 18 completed                                                                                           | 3/14 [00:07<00:23,  2.10s/it]
2026-05-31 00:43:29,226 - INFO - Getting weather info 
['get_creditcard_due_dates']
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:13<00:33,  3.39s/it][]
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:13<00:20,  2.29s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 6.00 / 6 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:13<00:20,  2.29s/it][]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:13<00:08,  1.22s/it]['get_watchlist_prices', 'get_watchlist_prices']
[*********************100%***********************]  18 of 18 completed██████████████████████████████▌                                                            | 7/14 [00:13<00:08,  1.22s/it]
2026-05-31 00:43:35,320 - INFO - Fetching the latest news information
[]
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:19<00:09,  1.81s/it]['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices']
Average Metric: 9.00 / 10 (90.0%):  71%|█████████████████████████████████████████████████████████████████████████████████████▋                                  | 10/14 [00:23<00:09,  2.31s/it]2026-05-31 00:43:43,307 - INFO - Getting weather info 
['get_stock_prices']
Average Metric: 10.00 / 11 (90.9%):  79%|█████████████████████████████████████████████████████████████████████████████████████████████▌                         | 11/14 [00:27<00:08,  2.73s/it]['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_news']
Average Metric: 11.00 / 12 (91.7%):  86%|██████████████████████████████████████████████████████████████████████████████████████████████████████                 | 12/14 [00:28<00:04,  2.44s/it]['get_todays_date_and_time', 'get_news', 'get_weather_info']
Average Metric: 11.00 / 13 (84.6%):  93%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:29<00:02,  2.03s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 12.00 / 14 (85.7%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:35<00:00,  2.54s/it]
2026/05/31 00:43:52 INFO dspy.evaluate.evaluate: Average Metric: 12.0 / 14 (85.7%)
2026/05/31 00:43:52 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 3', 'Predictor 1: Instruction 1', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:43:52 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71]
2026/05/31 00:43:52 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:43:52 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:43:52 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 14 / 20 =====
2026-05-31 00:43:52,663 - INFO - Fetching information about twitter topics through Tavily
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:43:52,704 - INFO - Fetching the latest news information
[]
Average Metric: 1.00 / 1 (100.0%):   0%|                                                                                                                                 | 0/14 [00:00<?, ?it/s]2026-05-31 00:43:52,744 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:43:52,752 - INFO - Fetching the latest news information
[]
Average Metric: 2.00 / 2 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:00<00:01, 10.29it/s]['get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:00<00:00, 22.29it/s][]
[*****                 11%                       ]  2 of 18 completed['get_events', 'get_events', 'get_events']                                                  | 3/14 [00:00<00:00, 22.29it/s]
Average Metric: 5.00 / 5 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:00<00:00, 22.29it/s][]
[**********************61%****                   ]  11 of 18 completed['get_metal_prices']█▊                                                                     | 6/14 [00:00<00:00, 12.06it/s]
[*********************100%***********************]  18 of 18 completed█████████████████████▊                                                                     | 6/14 [00:01<00:00, 12.06it/s]
[*********************100%***********************]  18 of 18 completed
2026-05-31 00:43:55,750 - INFO - Fetching the latest news information
['get_stock_prices', 'get_stock_prices']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:03<00:03,  1.62it/s]2026-05-31 00:43:58,879 - INFO - Getting weather info 
['get_watchlist_prices']
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:07<00:06,  1.35s/it]2026-05-31 00:44:02,462 - INFO - Getting weather info 
[*********************100%***********************]  18 of 18 completed
['get_twitter_trends_info', 'get_news']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:10<00:06,  1.72s/it]2026-05-31 00:44:04,246 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:21<00:11,  3.82s/it]['get_news', 'get_weather_info', 'get_events', 'get_events']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:22<00:06,  3.10s/it]['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:23<00:02,  2.65s/it]['get_metal_prices', 'get_stock_prices', 'get_news', 'get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_metal_prices', 'get_metal_prices', 'get_metal_prices']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:31<00:00,  2.23s/it]
2026/05/31 00:44:23 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:44:23 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 3', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:44:23 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0]
2026/05/31 00:44:23 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:44:23 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:44:23 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 15 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:44:25,929 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:44:26,046 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:44:26,617 - INFO - Fetching the latest news information
[*********************100%***********************]  18 of 18 completed
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:05<01:10,  5.40s/it]['get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:05<00:29,  2.50s/it]['get_events']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:06<00:19,  1.74s/it]2026-05-31 00:44:32,338 - INFO - Fetching the latest news information
[]
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:11<00:27,  2.75s/it][]
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:11<00:17,  1.93s/it]['get_watchlist_prices']
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:11<00:11,  1.39s/it]2026-05-31 00:44:36,149 - INFO - Getting weather info 
['get_creditcard_due_dates']
[*********************100%***********************]  18 of 18 completed██████████████████████████████▌                                                            | 7/14 [00:13<00:09,  1.39s/it]
['get_twitter_trends_info', 'get_news']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:15<00:10,  1.71s/it][]
Average Metric: 9.00 / 9 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:15<00:10,  1.71s/it]['get_metal_prices']
Average Metric: 9.00 / 10 (90.0%):  71%|█████████████████████████████████████████████████████████████████████████████████████▋                                  | 10/14 [00:19<00:07,  1.85s/it]2026-05-31 00:44:47,884 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_stock_prices']
Average Metric: 10.00 / 11 (90.9%):  79%|█████████████████████████████████████████████████████████████████████████████████████████████▌                         | 11/14 [00:27<00:10,  3.46s/it]2026-05-31 00:44:52,423 - INFO - Getting weather info 
['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices']
Average Metric: 10.00 / 12 (83.3%):  86%|██████████████████████████████████████████████████████████████████████████████████████████████████████                 | 12/14 [00:32<00:07,  3.90s/it]['get_news', 'get_weather_info', 'get_events']
Average Metric: 11.00 / 13 (84.6%):  93%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:36<00:03,  3.82s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 12.00 / 14 (85.7%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:39<00:00,  2.81s/it]
2026/05/31 00:45:03 INFO dspy.evaluate.evaluate: Average Metric: 12.0 / 14 (85.7%)
2026/05/31 00:45:03 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 4', 'Predictor 1: Instruction 0', 'Predictor 1: Few-Shot Set 5'].
2026/05/31 00:45:03 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0, 85.71]
2026/05/31 00:45:03 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:45:03 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:45:03 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 16 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:45:06,934 - INFO - Fetching the latest news information
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:04<01:04,  4.95s/it]2026-05-31 00:45:08,517 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:45:08,698 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_metal_prices', 'get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:07<00:41,  3.48s/it]2026-05-31 00:45:11,687 - INFO - Getting weather info 
2026-05-31 00:45:11,805 - INFO - Fetching the latest news information
['get_events', 'get_events', 'get_events']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:08<00:28,  2.61s/it][]
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:10<00:22,  2.26s/it]['get_watchlist_prices']
Average Metric: 5.00 / 5 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:10<00:22,  2.26s/it]2026-05-31 00:45:16,436 - INFO - file_cache is only supported with oauth2client<4.0.0
[]
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:14<00:16,  2.12s/it][]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:15<00:11,  1.70s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:15<00:07,  1.26s/it]['get_twitter_trends_info', 'get_news']
[*********************100%***********************]  18 of 18 completed███████████████████████████████████████▏                                                   | 8/14 [00:15<00:07,  1.26s/it]
2026-05-31 00:45:25,508 - INFO - Fetching the latest news information
['get_news', 'get_weather_info', 'get_events', 'get_events']
[*********************100%***********************]  18 of 18 completed████████████████████████████████████████████████████████▎                                 | 10/14 [00:22<00:09,  2.35s/it]
2026-05-31 00:45:32,154 - INFO - Getting weather info 
['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_news']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:31<00:11,  3.78s/it]['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates', 'get_stock_prices', 'get_stock_prices']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:34<00:07,  3.65s/it]['get_stock_prices', 'get_todays_date_and_time', 'get_stock_prices', 'get_stock_prices']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:36<00:03,  3.24s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:38<00:00,  2.73s/it]
2026/05/31 00:45:41 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:45:41 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 2', 'Predictor 1: Instruction 0', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:45:41 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0, 85.71, 100.0]
2026/05/31 00:45:41 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:45:41 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:45:41 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 17 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:45:41,670 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:45:41,687 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:45:41,704 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:45:42,023 - INFO - Fetching the latest news information
[*********************100%***********************]  18 of 18 completed
['get_events', 'get_events', 'get_events']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:02<00:34,  2.68s/it]['get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:03<00:17,  1.45s/it][]
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:03<00:11,  1.05s/it][]
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:06<00:14,  1.49s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:06<00:09,  1.02s/it]['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_news']
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:06<00:05,  1.35it/s][]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:06<00:03,  1.86it/s][]
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:09<00:07,  1.31s/it]['get_stock_prices', 'get_stock_prices', 'get_stock_prices']
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:11<00:07,  1.52s/it]['get_watchlist_prices']
Average Metric: 10.00 / 10 (100.0%):  64%|████████████████████████████████████████████████████████████████████████████▌                                          | 9/14 [00:11<00:07,  1.52s/it]2026-05-31 00:46:04,420 - INFO - Getting weather info 
['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:24<00:11,  3.77s/it]['get_twitter_trends_info', 'get_twitter_trends_info', 'get_news', 'get_news']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:24<00:06,  3.03s/it]['get_todays_date_and_time', 'get_transit_info', 'get_transit_info', 'get_weather_info']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:29<00:03,  3.36s/it]['get_todays_date_and_time', 'get_news', 'get_weather_info', 'get_events', 'get_events', 'get_news', 'get_news', 'get_weather_info', 'get_weather_info', 'get_weather_info']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:36<00:00,  2.62s/it]
2026/05/31 00:46:18 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:46:18 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 1', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 5'].
2026/05/31 00:46:18 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0, 85.71, 100.0, 100.0]
2026/05/31 00:46:18 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:46:18 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:46:18 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 18 / 20 =====
2026-05-31 00:46:18,281 - INFO - Fetching the latest news information
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:46:18,311 - INFO - file_cache is only supported with oauth2client<4.0.0
[]
Average Metric: 1.00 / 1 (100.0%):   0%|                                                                                                                                 | 0/14 [00:00<?, ?it/s]2026-05-31 00:46:18,346 - INFO - Fetching information about twitter topics through Tavily
[]
Average Metric: 2.00 / 2 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:00<00:00, 16.16it/s]['get_creditcard_due_dates']
Average Metric: 3.00 / 3 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:00<00:00, 23.29it/s][]
[                       0%                       ]['get_events']██████████▌                                                                                      | 4/14 [00:00<00:00, 39.53it/s]
Average Metric: 5.00 / 5 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:00<00:00, 39.53it/s][]
[********              17%                       ]  3 of 18 completed2026-05-31 00:46:18,748 - INFO - Getting weather info                                       | 5/14 [00:00<00:00, 39.53it/s]
[********************* 44%                       ]  8 of 18 completed['get_metal_prices']
[*********************100%***********************]  18 of 18 completed█████████████████████▊                                                                     | 6/14 [00:00<00:00, 39.53it/s]
[*********************100%***********************]  18 of 18 completed
[**********************83%***************        ]  15 of 18 completed2026-05-31 00:46:21,203 - INFO - Fetching the latest news information
[*********************100%***********************]  18 of 18 completed
['get_stock_prices']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:03<00:03,  1.86it/s]2026-05-31 00:46:23,054 - INFO - Fetching the latest news information
2026-05-31 00:46:27,396 - INFO - Getting weather info 
['get_watchlist_prices', 'get_watchlist_prices']
Average Metric: 9.00 / 9 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:10<00:03,  1.86it/s]['get_twitter_trends_info', 'get_news']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:11<00:05,  1.48s/it]2026-05-31 00:46:34,545 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_todays_date_and_time', 'get_weather_info', 'get_transit_info']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:17<00:06,  2.30s/it]['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:18<00:04,  2.18s/it]['get_todays_date_and_time', 'get_metal_prices', 'get_stock_prices', 'get_news']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:21<00:02,  2.28s/it]['get_news', 'get_weather_info', 'get_events']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:35<00:00,  2.53s/it]
2026/05/31 00:46:53 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:46:53 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 0', 'Predictor 1: Instruction 0', 'Predictor 1: Few-Shot Set 0'].
2026/05/31 00:46:53 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0, 85.71, 100.0, 100.0, 100.0]
2026/05/31 00:46:53 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:46:53 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:46:53 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 19 / 20 =====
2026-05-31 00:46:53,718 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:46:53,722 - INFO - Fetching the latest news information
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:46:53,773 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:46:53,804 - INFO - Fetching the latest news information
[*********************100%***********************]  18 of 18 completed
['get_metal_prices']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:02<00:32,  2.54s/it][]
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:02<00:15,  1.27s/it]2026-05-31 00:46:56,743 - INFO - Fetching the latest news information
['get_events', 'get_events', 'get_events']
Average Metric: 3.00 / 3 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:03<00:15,  1.27s/it]2026-05-31 00:46:58,630 - INFO - Getting weather info 
['get_creditcard_due_dates', 'get_creditcard_due_dates']
[********************* 44%                       ]  8 of 18 completed[]███▌                                                                                      | 4/14 [00:05<00:12,  1.26s/it]
[**********************67%*******                ]  12 of 18 completed[]███████████▏                                                                             | 5/14 [00:05<00:09,  1.02s/it]
[*********************100%***********************]  18 of 18 completed█████████████████████▊                                                                     | 6/14 [00:06<00:06,  1.29it/s]
['get_watchlist_prices']
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:08<00:08,  1.15s/it][]
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:09<00:06,  1.08s/it]['get_twitter_trends_info', 'get_news']
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:09<00:04,  1.13it/s]2026-05-31 00:47:03,654 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:47:05,862 - INFO - Getting weather info 
['get_metal_prices', 'get_stock_prices', 'get_news', 'get_stock_prices']
Average Metric: 10.00 / 10 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:13<00:07,  1.94s/it]['get_stock_prices', 'get_stock_prices']
Average Metric: 11.00 / 11 (100.0%):  71%|████████████████████████████████████████████████████████████████████████████████████▎                                 | 10/14 [00:13<00:07,  1.94s/it]['get_news', 'get_weather_info', 'get_events', 'get_events']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:19<00:04,  2.41s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:20<00:02,  2.09s/it]['get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:23<00:00,  1.68s/it]
2026/05/31 00:47:17 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:47:17 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 1', 'Predictor 0: Few-Shot Set 3', 'Predictor 1: Instruction 0', 'Predictor 1: Few-Shot Set 1'].
2026/05/31 00:47:17 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0, 85.71, 100.0, 100.0, 100.0, 100.0]
2026/05/31 00:47:17 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:47:17 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:47:17 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 20 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:47:19,318 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:47:20,287 - INFO - Fetching the latest news information
[]
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:04<01:03,  4.87s/it]2026-05-31 00:47:22,159 - INFO - Fetching the latest news information
2026-05-31 00:47:24,533 - INFO - Getting weather info 
['get_metal_prices', 'get_metal_prices']
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:08<00:48,  4.05s/it]['get_events']
Average Metric: 3.00 / 3 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:08<00:48,  4.05s/it][]
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:09<00:19,  1.91s/it]['get_watchlist_prices']
Average Metric: 5.00 / 5 (100.0%):  36%|███████████████████████████████████████████▏                                                                             | 5/14 [00:10<00:15,  1.73s/it]2026-05-31 00:47:29,477 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_twitter_trends_info', 'get_news']
Average Metric: 6.00 / 6 (100.0%):  43%|███████████████████████████████████████████████████▊                                                                     | 6/14 [00:12<00:12,  1.60s/it]2026-05-31 00:47:30,315 - INFO - Fetching the latest news information
[]
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:13<00:10,  1.47s/it][]
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:15<00:10,  1.74s/it]['get_creditcard_due_dates', 'get_creditcard_due_dates']
[**********************50%                       ]  9 of 18 completed['get_news', 'get_weather_info', 'get_events', 'get_events']                                | 9/14 [00:17<00:08,  1.80s/it]
[*********************100%***********************]  18 of 18 completed████████████████████████████████████████████████████████▎                                 | 10/14 [00:22<00:11,  2.76s/it]
['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices', 'get_creditcard_due_dates', 'get_creditcard_due_dates']
Average Metric: 11.00 / 11 (100.0%):  79%|████████████████████████████████████████████████████████████████████████████████████████████▋                         | 11/14 [00:24<00:07,  2.58s/it]2026-05-31 00:47:46,500 - INFO - Getting weather info 
['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_stock_prices', 'get_news', 'get_stock_prices', 'get_stock_prices']
Average Metric: 12.00 / 12 (100.0%):  86%|█████████████████████████████████████████████████████████████████████████████████████████████████████▏                | 12/14 [00:32<00:07,  3.99s/it]['get_stock_prices', 'get_stock_prices', 'get_stock_prices', 'get_stock_prices']
Average Metric: 13.00 / 13 (100.0%):  93%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:37<00:04,  4.27s/it]['get_todays_date_and_time', 'get_transit_info', 'get_transit_info', 'get_transit_info', 'get_weather_info']
Average Metric: 14.00 / 14 (100.0%): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:39<00:00,  2.80s/it]
2026/05/31 00:47:56 INFO dspy.evaluate.evaluate: Average Metric: 14.0 / 14 (100.0%)
2026/05/31 00:47:56 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 100.0 with parameters ['Predictor 0: Instruction 2', 'Predictor 0: Few-Shot Set 3', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 4'].
2026/05/31 00:47:56 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0, 85.71, 100.0, 100.0, 100.0, 100.0, 100.0]
2026/05/31 00:47:56 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:47:56 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:47:56 INFO dspy.teleprompt.mipro_optimizer_v2: ===== Trial 21 / 20 =====
  0%|                                                                                                                                                                    | 0/14 [00:00<?, ?it/s]2026-05-31 00:47:56,488 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:47:56,529 - INFO - Fetching the latest news information
2026-05-31 00:47:56,538 - INFO - file_cache is only supported with oauth2client<4.0.0
[*********************100%***********************]  18 of 18 completed
[*********************100%***********************]  18 of 18 completed
2026-05-31 00:47:59,482 - INFO - Fetching the latest news information
['get_metal_prices']
Average Metric: 1.00 / 1 (100.0%):   7%|████████▋                                                                                                                | 1/14 [00:03<00:44,  3.39s/it][]
Average Metric: 2.00 / 2 (100.0%):  14%|█████████████████▎                                                                                                       | 2/14 [00:03<00:18,  1.57s/it]['get_events']
Average Metric: 3.00 / 3 (100.0%):  21%|█████████████████████████▉                                                                                               | 3/14 [00:03<00:10,  1.09it/s]2026-05-31 00:48:01,362 - INFO - Fetching the latest news information
[]
Average Metric: 4.00 / 4 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:07<00:21,  2.11s/it][]
Average Metric: 5.00 / 5 (100.0%):  29%|██████████████████████████████████▌                                                                                      | 4/14 [00:07<00:21,  2.11s/it]['get_creditcard_due_dates']
[*********************100%***********************]  18 of 18 completed█████████████▏                                                                             | 5/14 [00:07<00:18,  2.11s/it]
['get_watchlist_prices', 'get_watchlist_prices']
Average Metric: 7.00 / 7 (100.0%):  50%|████████████████████████████████████████████████████████████▌                                                            | 7/14 [00:09<00:08,  1.15s/it]2026-05-31 00:48:06,041 - INFO - Getting weather info 
['get_twitter_trends_info', 'get_news']
Average Metric: 8.00 / 8 (100.0%):  57%|█████████████████████████████████████████████████████████████████████▏                                                   | 8/14 [00:10<00:07,  1.20s/it][]
Average Metric: 9.00 / 9 (100.0%):  64%|█████████████████████████████████████████████████████████████████████████████▊                                           | 9/14 [00:11<00:05,  1.09s/it]['get_metal_prices', 'get_stock_prices', 'get_watchlist_prices']
2026-05-31 00:48:10,882 - INFO - Getting weather info 
Average Metric: 9.00 / 10 (90.0%):  71%|█████████████████████████████████████████████████████████████████████████████████████▋                                  | 10/14 [00:14<00:06,  1.53s/it]['get_stock_prices']
Average Metric: 10.00 / 11 (90.9%):  79%|█████████████████████████████████████████████████████████████████████████████████████████████▌                         | 11/14 [00:17<00:06,  2.06s/it]['get_metal_prices', 'get_metal_prices', 'get_stock_prices', 'get_news']
Average Metric: 11.00 / 12 (91.7%):  86%|██████████████████████████████████████████████████████████████████████████████████████████████████████                 | 12/14 [00:18<00:03,  1.57s/it]['get_todays_date_and_time', 'get_transit_info', 'get_weather_info']
Average Metric: 12.00 / 13 (92.3%):  93%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████▌        | 13/14 [00:24<00:02,  2.79s/it]['get_todays_date_and_time', 'get_news', 'get_weather_info']
Average Metric: 12.00 / 14 (85.7%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 14/14 [00:39<00:00,  2.81s/it]
2026/05/31 00:48:35 INFO dspy.evaluate.evaluate: Average Metric: 12.0 / 14 (85.7%)
2026/05/31 00:48:35 INFO dspy.teleprompt.mipro_optimizer_v2: Score: 85.71 with parameters ['Predictor 0: Instruction 0', 'Predictor 0: Few-Shot Set 3', 'Predictor 1: Instruction 2', 'Predictor 1: Few-Shot Set 1'].
2026/05/31 00:48:35 INFO dspy.teleprompt.mipro_optimizer_v2: Scores so far: [100.0, 100.0, 92.86, 85.71, 85.71, 100.0, 85.71, 92.86, 100.0, 100.0, 100.0, 100.0, 85.71, 100.0, 85.71, 100.0, 100.0, 100.0, 100.0, 100.0, 85.71]
2026/05/31 00:48:35 INFO dspy.teleprompt.mipro_optimizer_v2: Best score so far: 100.0
2026/05/31 00:48:35 INFO dspy.teleprompt.mipro_optimizer_v2: =========================


2026/05/31 00:48:35 INFO dspy.teleprompt.mipro_optimizer_v2: Returning best identified program with score 100.0!
  0%|                                                                                                                                                                    | 0/13 [00:00<?, ?it/s]2026-05-31 00:48:35,871 - INFO - Fetching the latest news information
['get_news']
Average Metric: 1.00 / 1 (100.0%):   8%|█████████▎                                                                                                               | 1/13 [00:08<01:36,  8.05s/it]['get_transit_info']
Average Metric: 2.00 / 2 (100.0%):  15%|██████████████████▌                                                                                                      | 2/13 [00:19<01:50, 10.02s/it]2026-05-31 00:48:55,957 - INFO - Fetching information about twitter topics through Tavily
['get_metal_prices', 'get_metal_prices', 'get_twitter_trends_info']
Average Metric: 3.00 / 3 (100.0%):  23%|███████████████████████████▉                                                                                             | 3/13 [00:31<01:48, 10.82s/it]2026-05-31 00:49:07,105 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:49:07,410 - INFO - Getting weather info 
['get_events', 'get_weather_info']
Average Metric: 4.00 / 4 (100.0%):  31%|█████████████████████████████████████▏                                                                                   | 4/13 [00:44<01:46, 11.80s/it][]
Average Metric: 5.00 / 5 (100.0%):  31%|█████████████████████████████████████▏                                                                                   | 4/13 [00:44<01:46, 11.80s/it][]
[*********************100%***********************]  18 of 18 completed████████████████▌                                                                          | 5/13 [00:44<01:34, 11.80s/it]
['get_todays_date', 'get_creditcard_due_dates', 'get_stock_prices']
Average Metric: 6.00 / 7 (85.7%):  54%|█████████████████████████████████████████████████████████████████▋                                                        | 7/13 [00:47<00:30,  5.00s/it]2026-05-31 00:49:23,351 - INFO - file_cache is only supported with oauth2client<4.0.0
2026-05-31 00:49:23,555 - INFO - Getting weather info 
['get_todays_date_and_time', 'get_events', 'get_weather_info']
Average Metric: 6.00 / 8 (75.0%):  62%|███████████████████████████████████████████████████████████████████████████                                               | 8/13 [01:03<00:37,  7.51s/it]['get_todays_date_and_time', 'get_transit_info']
Average Metric: 7.00 / 9 (77.8%):  69%|████████████████████████████████████████████████████████████████████████████████████▍                                     | 9/13 [01:23<00:42, 10.62s/it]2026-05-31 00:49:59,317 - INFO - Fetching the latest news information
2026-05-31 00:50:11,498 - INFO - Fetching information about twitter topics through Tavily
2026-05-31 00:50:28,495 - INFO - Getting weather info 
[*********************100%***********************]  18 of 18 completed
2026-05-31 00:50:47,032 - INFO - file_cache is only supported with oauth2client<4.0.0
['get_news', 'get_twitter_trends_info', 'get_weather_info', 'get_stock_prices', 'get_metal_prices', 'get_creditcard_due_dates', 'get_events', 'get_watchlist_prices']
Average Metric: 8.00 / 10 (80.0%):  77%|████████████████████████████████████████████████████████████████████████████████████████████▎                           | 10/13 [02:32<01:17, 25.77s/it][]
Average Metric: 9.00 / 11 (81.8%):  77%|████████████████████████████████████████████████████████████████████████████████████████████▎                           | 10/13 [02:32<01:17, 25.77s/it]['get_metal_prices']
[*********************100%***********************]  18 of 18 completed████████████████████████████████████████████████████████████████████████████████▊         | 12/13 [02:32<00:14, 14.84s/it]
2026-05-31 00:51:11,573 - INFO - Fetching the latest news information
['get_stock_prices', 'get_news']
Average Metric: 10.00 / 13 (76.9%): 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 13/13 [03:03<00:00, 14.14s/it]
2026/05/31 00:51:39 INFO dspy.evaluate.evaluate: Average Metric: 10.0 / 13 (76.9%)
Baseline accuracy on testset - EvaluationResult(score=76.92, results=<list of 13 results>)
Optimized agent accuracy on testset - EvaluationResult(score=76.92, results=<list of 13 results>)