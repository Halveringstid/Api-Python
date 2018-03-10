# Api-Python

## Run in docker
```bash 
docker build -t hacknarock-api:latest .
docker run -d -p 5000:5000 hacknarock-api:latest
```

## API definition
@GET
/api/messages

Lista:
```json
  "id":"6969692138",
  "lat" : 51.958437,
  "lon" : 19.21934587,
  "message: "Łódź Bałuty to nic dobrego",
  "author":"antek123" //or empty - nie null!
  "created_at":ISO8601 //sprawdź to
```

@POST
body:
/api/messages
```json
  "lat" : 51.958437,
  "lon" : 19.21934587,
  "message: "Łódź Bałuty to nic dobrego",
  "author":"antek123" //or empty - nie null!
```
reponse z utworzonym create_at i id

@GET
/api/messages?lat=51.682473&lon=19.54&radius=15
zwraca listę w promieniu 15 metrów od lat=51.682473 lon=19.54

