MATCH (ru:RU {ru: "4603354"})
MATCH (t:Tweet)-[:CONTAIN]->(h:Hashtag)
WHERE NOT EXISTS {
  MATCH (t)-[:REFERS_TO]->(:Retweet)
} AND NOT EXISTS {
  MATCH (t)-[:REFERS_TO]->(:Quote)
} AND NOT EXISTS {
  MATCH (t)-[:REFERS_TO]->(:Ask)
}
RETURN h.tag AS Hashtag, COUNT(h) AS MostUsed
ORDER BY MostUsed DESC
LIMIT 1;

// Command for generating graph:
MATCH (r:RU {ru: "4603354"})
MATCH (h:Hashtag {tag: "issoaglobonaomostra"})<-[:CONTAIN]-(t:Tweet)
RETURN h, t, r

// Most tweeted:
MATCH (r:RU {ru: "4603354"})
MATCH (t:Tweet)-[:HAS_PUBLIC_METRICS]->(m:PublicMetrics)
RETURN t.tweet_id, t.text, m.retweet_count
ORDER BY m.retweet_count DESC
LIMIT 1