{
  "files": [
    {
      "aql": {
        "items.find" : {
          "repo": "example-repo-local",
          "created": {"$last" : "10d"},
          "stat.downloads": {"$eq" : null}
	   }
      }
    },
    {
      "pattern": "slipway-hello-world/1.0.1",
      "target" : "slipway-docker-dev-local"
    },
    {
      "pattern": "rabbit",
      "target": "example-repo-local"
    }
  ]
}

