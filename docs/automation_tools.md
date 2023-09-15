# Automation Tools

## CURL

command line tool and library for transferring data with URLs
(since 1998)

https://curl.se

store token
```commandline
export token=xxxxxxxxxxxxxxxxxxx
```

### GET

GET the **projects** 

Default call from page
```commandline
curl -X GET https://api.todoist.com/rest/v2/projects -H "Authorization: Bearer $token"
```

GET without GET option
```commandline
curl https://api.todoist.com/rest/v2/projects -H "Authorization: Bearer $token"
```

output to file
```commandline
curl -s https://api.todoist.com/rest/v2/projects -H "Authorization: Bearer $token" -o output.json
```

See the details of response
```commandline
curl "https://api.todoist.com/rest/v2/projects" -H "Authorization: Bearer $token" -v
```
Get a project by Id

```commandline
curl "https://api.todoist.com/rest/v2/projects/$id_project" \
  -H "Authorization: Bearer $token"
```

### POST
Create a project
```commandline
curl "https://api.todoist.com/rest/v2/projects" -X POST \
    --data '{ "name": "Shopping List" }' \
    -H "Content-Type: application/json" \    
    -H "Authorization: Bearer $token"
```
create project using file
```commandline
curl "https://api.todoist.com/rest/v2/projects" -X POST \
    --data @data.json \ 
    -H "Content-Type: application/json"  
    -H "Authorization: Bearer $token"
```
### UPDATE
Update project 
```commandline
curl "https://api.todoist.com/rest/v2/projects/$id_project" \
    -X POST \
    --data '{ "name": "Things To Buy" }' \
    -H "Content-Type: application/json" \    
    -H "Authorization: Bearer $token"
```
** Try using PUT and PATCH

### DELETE
Delete a project

```commandline
curl -X DELETE "https://api.todoist.com/rest/v2/projects/$id_project" \
    -H "Authorization: Bearer $token"
```

## Postman

Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration,
so you can create better APIs—faster.

https://www.postman.com/

## Insomnia

Kong Insomnia is a collaborative open source API development platform that makes it easy to build high-quality APIs — without the bloat and clutter of other tools.

https://insomnia.rest


