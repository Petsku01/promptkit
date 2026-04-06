# API Documentation Pattern

## Description

Generate OpenAPI/Swagger documentation from code or design specs.

## When to use

Creating or updating API documentation, onboarding developers.

## When to avoid

Private/internal APIs where documentation overhead isn't justified.

## Template

```
Generate OpenAPI 3.0 documentation for this API:

Endpoints:
- `METHOD /path` - Description

Include for each:
- Summary
- Description
- Request schema (JSON Schema)
- Response schemas (200, 400, 404, 500)
- Authentication requirements
- Rate limits
- Example requests/responses

Format as YAML.
```

## Example

```
Generate OpenAPI 3.0 documentation for this API:

Endpoints:
- `GET /users` - List users
- `GET /users/{id}` - Get user
- `POST /users` - Create user
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

Include for each:
- Summary
- Description
- Request schema (JSON Schema)
- Response schemas (200, 400, 404, 500)
- Authentication: Bearer token
- Rate limit: 100 req/min
- Example requests/responses

Format as YAML.

Output:
```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      responses:
        200:
          description: List of users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
```
```

## Tags

documentation, api, openapi, swagger, specs
