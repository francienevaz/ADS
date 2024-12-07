MERGE (r: RU {ru: "4603354"});
CALL apoc.load.directory('*.json') YIELD value
WITH value AS arquivo
CALL apoc.load.json(arquivo) YIELD value
UNWIND value.data as tweet
UNWIND tweet.entities.hashtags as hashtag
MERGE (t:Tweet {tweet_id: tweet.id})
ON CREATE SET t.mensagem = tweet.text,
              t.created_at= datetime(tweet.created_at),
              t.conversation_id = tweet.conversation_id,
             // t.font = tweet.source
// Table: Retweets             
FOREACH (ref IN tweet.referenced_tweets |
    FOREACH(_ IN CASE WHEN ref.type = "retweeted" THEN [1] ELSE [] END |
    REMOVE t:Tweet
    SET t:Retweet
  )
)
//Table: Asks
FOREACH (ref IN tweet.referenced_tweets |
    FOREACH(_ IN CASE WHEN ref.type = "replied_to" THEN [1] ELSE [] END |
    REMOVE t:Tweet
    SET t:Resposta
  )
)
//Table: Quotes
FOREACH (ref IN tweet.referenced_tweets |
    FOREACH(_ IN CASE WHEN ref.type = "quoted" THEN [1] ELSE [] END |
    REMOVE t:Tweet
    SET t:Citacao
  )
)

MERGE (u:User {user_id: tweet.author_id})
MERGE (h:Hashtag {tag: apoc.text.replace(apoc.text.clean(hashtag.tag), '[^a-zA-Z0-9]', '')})
MERGE (t)-[:CONTAIN]->(h)
MERGE (u)-[:TWEETED]->(t);