# API Design Pattern

## Description

Design a complete REST API with endpoints, schemas, error handling, and versioning strategy.

## When to use

Creating APIs, integrations, or when contract-first development matters.

## When to avoid

Internal tools where API design is secondary.

## Template

```
Design a RESTful API for [DOMAIN].

Endpoints:
1. `POST /api/v1/resource` - Create with body schema
2. `GET /api/v1/resource/{id}` - Read with response schema  
3. `PUT /api/v1/resource/{id}` - Update with body schema
4. `DELETE /api/v1/resource/{id}` - Delete with response schema

Request Schema:
{
  "field1": type (constraints),
  "field2": type (constraints)
}

Response Schema (200 OK):
{
  "id": type,
  "field1": type,
  "field2": type,
  "created_at": timestamp
}

Error Responses:
- 400: Bad Request - Invalid input
- 404: Not Found - Resource not found
- 500: Server Error - Database error

Versioning strategy: URL (/v1/, /v2/) or Content-Type header
```

## Example

```
Design a RESTful API for user management.

Endpoints:
1. `POST /api/v1/users` - Create user with body schema
2. `GET /api/v1/users/{id}` - Read with response schema  
3. `PUT /api/v1/users/{id}` - Update with body schema
4. `DELETE /api/v1/users/{id}` - Delete with response schema

Request Schema:
{
  "email": string (email format),
  "name": string (max 100 chars),
  "role": string (user, admin, guest)
}

Response Schema (200 OK):
{
  "id": string (UUID),
  "email": string (email format),
  "name": string (max 100 chars),
  "role": string (user, admin, guest),
  "created_at": ISO8601 timestamp
}

Error Responses:
- 400: Bad Request - Invalid email format
- 404: Not Found - User not found
- 500: Server Error - Database error

Versioning: URL path versioning (/v1/, /v2/)
```

## Tags

api, rest, endpoints, schema, versioning
