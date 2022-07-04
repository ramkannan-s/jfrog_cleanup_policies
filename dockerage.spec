items.find({
  "name": "manifest.json",
  "created":{"$gt":"2022-01-01"}
}).include("path")

