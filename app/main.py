# Fast API implementation

## Search Indexing Endpoints

### Create Index

**API:** POST /search-index

**Description:** Create a search index for product data

**Request Body:** 
```json
{
    "index_name": "example_index",
    "fields_to_index": ["name", "description", "price"]
}
```

**Response Body:** 
```json
{
    "status": "success",
    "message": "Index successfully created"
}
```

### Update Index

**API:** PUT /search-index/{index_name}

**Description:** Update a search index for product data

**Request Body:** 
```json
{
    "fields_to_index": ["name", "description", "price", "category"]
}
```

**Response Body:** 
```json
{
    "status": "success",
    "message": "Index successfully updated"
}
```

### Delete Index

**API:** DELETE /search-index/{index_name}

**Description:** Delete a search index

**Response Body:** 
```json
{
    "status": "success",
    "message": "Index successfully deleted"
}
```

### Add Data to Index

**API:** POST /search-index/{index_name}/data

**Description:** Add product data to the search index

**Request Body:** 
```json
{
    "products": [
        {
            "name": "Product 1",
            "description": "This is a product description",
            "price": 100.00
        },
        {
            "name": "Product 2",
            "description": "This is another product description",
            "price": 200.00
        }
    ]
}
```

**Response Body:** 
```json
{
    "status": "success",
    "message": "Data successfully added to index"
}
```

### Remove Data from Index

**API:** DELETE /search-index/{index_name}/data

**Description:** Remove product data from the search index

**Request Body:** 
```json
{
    "products": [
        {
            "name": "Product 1"
        },
        {
            "name": "Product 2"
        }
    ]
}
```

**Response Body:** 
```json
{
    "status": "success",
    "message": "Data successfully removed from index"
}
```

### Search Index

**API:** GET /search-index/{index_name}/search

**Description:** Search the search index for products

**Parameters:**

- `query`: the search query

**Request Body:** 
```
query=Product
```

**Response Body:** 
```json
{
    "status": "success",
    "results": [
        {
            "name": "Product 1",
            "description": "This is a product description",
            "price": 100.00
        },
        {
            "name": "Product 2",
            "description": "This is another product description",
            "price": 200.00
        }
    ]
}
```