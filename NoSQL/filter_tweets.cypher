MERGE (r:RU {ru: "4603354"});
CALL apoc.load.directory('*.json') YIELD value
WITH value AS file_json
CALL apoc.load.json(file_json) YIELD value
UNWIND value.data AS tweet

//Creating tables
MERGE (t:Tweet {tweet_id: tweet.id})
  ON CREATE SET t.text = tweet.text,
                t.created_at = datetime(tweet.created_at),
                t.conversation_id = tweet.conversation_id

// Table: Retweets
FOREACH (ref IN tweet.referenced_tweets |
  FOREACH (_ IN CASE WHEN ref.type = "retweeted" THEN [1] ELSE [] END |
    REMOVE t:Tweet
    SET t:Retweet
  )
)

// Table: Asks
FOREACH (ref IN tweet.referenced_tweets |
  FOREACH (_ IN CASE WHEN ref.type = "replied_to" THEN [1] ELSE [] END |
    REMOVE t:Tweet
    SET t:Ask
  )
)

// Table: Quotes
FOREACH (ref IN tweet.referenced_tweets |
  FOREACH (_ IN CASE WHEN ref.type = "quoted" THEN [1] ELSE [] END |
    REMOVE t:Tweet
    SET t:Quote
  )
)

// Who tweeted?
MERGE (u:User {user_id: tweet.author_id})
MERGE (u)-[:TWEETED]->(t)

// Link hashtags to the tweet and the user
WITH t, tweet, tweet.entities.hashtags AS hashtags, u
UNWIND hashtags AS hashtag

WITH t, u, apoc.text.replace(apoc.text.clean(hashtag.tag), '[^a-zA-Z0-9]', '') AS cleanedHashtag
MERGE (h:Hashtag {tag: cleanedHashtag})
MERGE (t)-[:CONTAIN]->(h)
MERGE (u)-[:USED_HASHTAG]->(h);

