# hpecfmaudits
Real time alarm and events from hpe composable fabric controller

This application uses the mongo db installed by StackStorm. Since the DB is secured
you will need to log into the StackStorm mongo DB as a StackStorm admin and create a separate DB

# To get hpecfmaudits to work with StackStorm mongo DB

log in with admin first
-------------------------------------------------------------------------------------
mongo -u admin -p UkIbDILcNbMhkh3KtN6xfr9h admin  (passwd in /etc/st2/st2.config)

# Then create a new user
db.createUser({user: "appUser",pwd: "passwordForAppUser",roles: [ { role: "readWrite", db: "app_db" } ]})



# Manually test the database.
Follow the steps below to manually test the newly created mongo database

## Create a collection and add a record to it. Run these commands from the terminal CLI
```
mongo -u appUser -p passwordForAppUser admin
> use app_db
> db.createCollection('number')
> db.number.insertOne({num:1})
> db.number.find()
{ "_id" : ObjectId("5cc84e276e9abf31a65a5f1f"), "num" : 1 }
```
# Overview
![Objective - what success looks like](/img/overview.png)
