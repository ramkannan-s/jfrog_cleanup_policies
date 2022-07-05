{
  "files": [
    {
      "aql": {
        "items.find" : {
          "repo": "example-repo-local",
          "created": {"$before" : "10d"},
          "stat.downloads": {"$eq" : null}
	   }
      }
    }
  ]
}
