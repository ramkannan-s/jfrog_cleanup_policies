{
  "files": [
    "aql": {
      "items.find" : {
        "repo": "example-repo-local",
        "created": {"$last" : "10d"},
        "stat.downloads": {"$eq" : null}
	 }
    }
  ]
}

