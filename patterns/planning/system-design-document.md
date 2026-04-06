# System Design Document Pattern

## Description

Create a comprehensive system design document covering requirements, architecture, APIs, and deployment.

## When to use

Starting a new service, major architectural decisions, or when stakeholders need detailed technical documentation.

## When to avoid

Simple CRUD applications where architecture is straightforward and well-understood.

## Template

```
You are tasked with creating a comprehensive and detailed system design document.

## Phase 1: Requirements Gathering

Outline the problem the service aims to solve:
- **Functional requirements**: What must the system do?
- **Non-functional requirements**: Performance, scalability, security
- **Constraints**: Budget, timeline, compliance
- **Integration points**: External systems and APIs

## Phase 2: Architecture Evaluation

Compare architectural options:
- Monolith vs Microservices vs Serverless
- Synchronous vs Asynchronous communication
- SQL vs NoSQL vs Hybrid data storage

For each option, discuss trade-offs:
| Option | Scalability | Maintainability | Performance | Cost |
|--------|-------------|-----------------|-------------|------|
| [Option A] | [Rating] | [Rating] | [Rating] | [Rating] |
| [Option B] | [Rating] | [Rating] | [Rating] | [Rating] |

## Phase 3: High-Level Architecture

Define major components:
- **Component A**: [Responsibility]
- **Component B**: [Responsibility]
- **Component C**: [Responsibility]

Data flow: [How data moves between components]

## Phase 4: Detailed Design

### Technology Stack
- **Language**: [e.g., Python, Go, TypeScript]
- **Framework**: [e.g., FastAPI, Express]
- **Database**: [e.g., PostgreSQL, MongoDB]
- **Cache**: [e.g., Redis]
- **Message Queue**: [e.g., RabbitMQ, Kafka]
- **Deployment**: [e.g., Kubernetes, AWS ECS]

### Data Design
- **Entity A**: [Fields, relationships]
- **Entity B**: [Fields, relationships]
- **Indexes**: [For query optimization]
- **Sharding strategy**: [If applicable]

### API Design
RESTful endpoints:
- `POST /api/v1/resource` - Create
- `GET /api/v1/resource/{id}` - Read
- `PUT /api/v1/resource/{id}` - Update
- `DELETE /api/v1/resource/{id}` - Delete

Include:
- Request/response schemas
- Authentication requirements
- Rate limiting
- Error response format

## Phase 5: Operational Considerations

### Scalability
- Horizontal scaling strategy
- Caching layers
- Load balancing
- CDN usage

### Fault Tolerance
- Circuit breakers
- Retry strategies
- Fallback mechanisms
- Data replication

### Security
- Authentication (OAuth, JWT, etc.)
- Authorization (RBAC, ABAC)
- Data encryption
- Input validation
- API rate limiting

### Monitoring
- Metrics to track
- Alerting thresholds
- Log aggregation
- Distributed tracing

## Output Format

Provide as professional Markdown document:

```markdown
# System Design: [Service Name]

## 1. Introduction
## 2. Requirements
## 3. Architecture
## 4. Data Design
## 5. API Design
## 6. Scalability & Fault Tolerance
## 7. Security
## 8. Deployment
## 9. Conclusion
```

Include diagrams as ASCII art or detailed textual descriptions.
```

## Example

```
You are tasked with creating a comprehensive system design document.

## Phase 1: Requirements Gathering

Build a URL shortening service like bit.ly:
- Create short URLs from long ones
- Redirect to original URL
- Track click analytics
- Support custom aliases
- 10M requests/day, <100ms latency

## Phase 2: Architecture Evaluation

Compare storage options:
| Option | Scalability | Complexity | Cost |
|--------|-------------|------------|------|
| PostgreSQL | Good | Low | Medium |
| DynamoDB | Excellent | Medium | High |
| Redis | Excellent | Low | Medium |

Choose: PostgreSQL with Redis cache layer

## Phase 3: High-Level Architecture

- **API Gateway**: Rate limiting, auth
- **URL Service**: Create, retrieve, redirect
- **Analytics Service**: Track clicks
- **Cache Layer**: Hot URL caching

## Phase 4: Detailed Design

### Technology Stack
- Python/FastAPI
- PostgreSQL (sharded by hash)
- Redis (caching)
- Kafka (analytics events)

### Data Design
- URLs table: id, short_code, long_url, created_at, user_id
- Analytics table: url_id, timestamp, ip, user_agent, referrer

### API Design
- `POST /api/v1/shorten` - Create short URL
- `GET /{short_code}` - Redirect
- `GET /api/v1/stats/{short_code}` - Get analytics

## Phase 5: Operational
- Horizontal scaling with Kubernetes
- Circuit breakers for DB failures
- Prometheus + Grafana monitoring
```

## Notes

- Justify all choices with reasoning
- Keep comprehensive but concise
- Include failure scenarios
- Address security from start

## Tags

system-design, architecture, documentation, api-design, planning
