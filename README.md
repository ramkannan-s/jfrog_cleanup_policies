
# JFROG Clean-Up Policies

Software development can be a messy business. Often, there will be many artifacts residing in Artifactory that will never be used. 
Artifactory’s built-in cleanup tools can help you to handle the majority of cases you’ll want to address.


## Install JFROG CLI
Link to Install [JFROG CLI](https://jfrog.com/getcli/) tool. 


## Ping the artifactory using JFROG CLI and REST API
```bash
curl -u admin:<password> -XGET https://ramkannans.jfrog.io/artifactory/api/system/ping 

jf rt curl -XGET api/system/ping #provided local config us updated using jf c add).
```


## Run Locally

Specific artifact - `jf rt curl -X DELETE default-maven-local/slipway-mvn/1.0.10/ramlab_hello-1.0.10.jar`

Specific folder - `jf rt del "default-maven-local/slipway-mvn/1.0.1"`

Specific Docer Tag - `jf rt curl -X DELETE slipway-docker-dev-local/slipway-hello-world/1.0.2225954912`

delete using spec 
```
Create a spec file called test.spec
run the test.spec using jf curl --> jf rt curl -X POST api/search/aql -T test.spec
run rt delete to apply the spec file for deleting the results found --> jf rt delete --spec=test.spec
```

delete using JFrog CLI Plugin
```
jf plugin install rt-cleanup
jf rt-cleanup clean sample-2-local --time-unit=day --no-dl=3 --server-id=eu
12:28:38 [🔵Info] [Thread 1] Deleting sample-2-local/avatar_1.jpg
12:28:38 [🔵Info] [Thread 0] Deleting sample-2-local/generic-local/avatar_1.jpg
12:28:38 [🔵Info] [Thread 2] Deleting sample-2-local/avatar_2.jpg
```


