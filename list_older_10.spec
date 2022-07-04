items.find({
    "created": {"$last" : "3d"},
    "stat.downloads": {"$eq" : null}
 })

