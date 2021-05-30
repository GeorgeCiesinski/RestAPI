# Flask Rest API

This project is a very simple API made with Flask. This API includes several
endpoints which render a home page, and run various functions of a
mock store.

## Endpoints

The Flask endpoints have specific routes which can be accessed as part of 
the URL. The endpoints are a mix of GET and POST methods that either save
the provided data, or send data back to the client.

- **home** - Renders a simple HTML template into a homepage
- **create_store** - Creates a new store and appends it to the stores list
- **get_store** - Retrieve store matching a specific name
- **get_stores** - Retrieve all stores
- **create_item_in_store** - Creates a new item and appends it to the items
list of a specific store
- **get_items_in_store** - Retrieve all items from a specific store

### create_store

**Request**

```
POST http://127.0.0.1:5000/store

{
    "name": "Another Store"
}
```

**Response**

```
{
    "items": [],
    "name": "Another Store"
}
```

### get_store

**Request**

```
GET http://127.0.0.1:5000/store/My Amazing Store
```

**Response**

```
{
    "items": [
        {
            "name": "Product 1",
            "price": 29.99
        }
    ],
    "name": "My Amazing Store"
}
```

### get_stores

**Request**

```
GET http://127.0.0.1:5000/store
```

**Response**

```
{
    "stores": [
        {
            "items": [
                {
                    "name": "Product 1",
                    "price": 29.99
                }
            ],
            "name": "My Amazing Store"
        }
    ]
}
```

### create_item_in_store

**Request**

```
POST http://127.0.0.1:5000/store/Another Store/item

{
    "name": "Another Item",
    "price": 11.19
}
```

**Response**

```
{
    "name": "Another Item",
    "price": 11.19
}
```

### get_items_in_store

**Request**

```
GET http://127.0.0.1:5000/store/My Amazing Store/item

{
    "name": "Another Item",
    "price": 11.99
}
```

**Response**

```
{
    "items": [
        {
            "name": "Product 1",
            "price": 29.99
        }
    ]
}
```