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
    },
    {
      "pattern": "slipway-docker-dev-local/slipway-hello-world/1.0.1/"
    },
    {
      "pattern": "example-repo-local/rabbit/"
    }
  ]
}
