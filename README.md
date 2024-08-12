```
uvicorn main:app --reload
```

```
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name": "Item 1", "description": "This is item 1."}'
```

```
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name": "Updated Item", "description": "This is an updated item."}'
```

```
curl -X GET "http://127.0.0.1:8000/items/"
```

```
curl -X DELETE "http://127.0.0.1:8000/items/1"

```