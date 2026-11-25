# Lab 2: Component Diagrams and Architectural Modeling

**Course:** Software Engineering (UE24CS341A)  
**Institution:** PES University, Bengaluru  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  

---

## 1. Objective
- Model software systems using UML Component diagrams to represent physical and logical architecture.
- Define modular components, provided interfaces (`lollipop`), required interfaces (`socket`), ports, and dependencies.
- Illustrate multi-tier separation of concerns across Client, API Gateway, Microservices, and Persistence layers.

---

## 2. System Architecture: Distributed Sports Event Management System
The system is partitioned into high-cohesion, loosely-coupled microservices:

1. **Client Tier:** Next.js Web Portal (Admin Dashboard & Fan Web App), Mobile Ingress Scanner App.
2. **API Gateway Tier:** Reverse proxy handling TLS termination, JWT validation, rate limiting, and request routing.
3. **Core Services:**
   - `Ticketing & Inventory Service`: Atomic seat reservation, lock management via Redis.
   - `Ingress & Turnstile Controller Service`: High-throughput QR code verification with offline-capable edge caching.
   - `Crowd Analytics & Telemetry Engine`: Real-time density calculation, IoT turnstile telemetry aggregation.
   - `Notification Service`: Kafka-driven email/SMS push worker.
4. **Data Tier:**
   - PostgreSQL: Relational ACID storage for matches, bookings, transactions.
   - Redis: In-memory seat-lock cache and active session store.

---

## 3. Component Diagram

### Mermaid Representation
```mermaid
flowchart TD
    subgraph ClientLayer ["Client Applications"]
        WebApp["Web App (Next.js / React)"]
        ScannerApp["Turnstile Scanner (Android / PWA)"]
    end

    subgraph GatewayLayer ["API Gateway & Security"]
        Gateway["API Gateway / Envoy Proxy"]
        AuthModule["OAuth2 / JWT Authenticator"]
    end

    subgraph ServiceLayer ["Microservices Layer"]
        TicketService["Ticketing & Booking Component"]
        IngressService["Ingress & Gate Control Component"]
        AnalyticsService["Crowd Telemetry Component"]
        NotificationWorker["Notification Worker"]
    end

    subgraph StorageLayer ["Persistence & Messaging Layer"]
        PostgresDB[(PostgreSQL Primary DB)]
        RedisCache[(Redis Distributed Lock Cache)]
        EventBus[[Kafka Message Broker]]
    end

    WebApp -->|HTTPS / REST| Gateway
    ScannerApp -->|gRPC / WebSockets| Gateway
    Gateway --> AuthModule
    Gateway --> TicketService
    Gateway --> IngressService
    Gateway --> AnalyticsService

    TicketService --> PostgresDB
    TicketService --> RedisCache
    TicketService -->|Publish Booking Event| EventBus

    IngressService --> PostgresDB
    IngressService --> RedisCache
    IngressService -->|Publish Gate Entry Event| EventBus

    EventBus --> AnalyticsService
    EventBus --> NotificationWorker
```

### PlantUML Source
See [`diagrams/component_diagram.puml`](diagrams/component_diagram.puml).

---

## 4. Key Deliverables
- [`component_specifications.md`](component_specifications.md): Component interface contracts and port definitions.
- [`diagrams/component_diagram.puml`](diagrams/component_diagram.puml): PlantUML component diagram.
- [`diagrams/component_diagram.mmd`](diagrams/component_diagram.mmd): Mermaid component diagram.
