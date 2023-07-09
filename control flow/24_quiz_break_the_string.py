# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

# Mine
# write your loop here
# for item in headlines:
#     news_ticker += item    
#     if len(news_ticker) >= 140:
#         break
#     print("Adding '{}'".format(item))

# print()
# print(news_ticker + ": {} chars".format(len(news_ticker)))

# while len(news_ticker) > 140:
#     split = news_ticker.split()
#     news_ticker = ""
#     for item in split:
#         news_ticker += item

# while len(news_ticker) != 140:
#     news_ticker += " "    

# Tutorial
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print()
print(news_ticker + ": {}".format(len(news_ticker)))