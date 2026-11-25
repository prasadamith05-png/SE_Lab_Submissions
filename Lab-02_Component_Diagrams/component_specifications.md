# Component Specifications & Interface Definitions

## 1. Ticketing & Booking Component (`TicketComponent`)

### Provided Interfaces:
- `ITicketReservation`:
  - `reserveSeats(matchId: UUID, seatIds: List[UUID], userId: UUID): ReservationToken`
  - `confirmBooking(token: ReservationToken, paymentAuthId: String): BookingReceipt`
  - `releaseReservation(token: ReservationToken): Boolean`
- `ITicketQuery`:
  - `getAvailableSeats(matchId: UUID, standId: String): List[SeatStatus]`
  - `getUserTickets(userId: UUID): List[TicketDetail]`

### Required Interfaces:
- `IPaymentProcessor`: External gateway REST API interface for charging cards.
- `IRedisLock`: Distributed lock manager to prevent race conditions during concurrent seat selection.
- `IEventPublisher`: Publishes `TicketConfirmedEvent` and `TicketCancelledEvent` to Apache Kafka.

---

## 2. Ingress & Turnstile Controller Component (`IngressComponent`)

### Provided Interfaces:
- `ITurnstileAccess`:
  - `verifyTicketQR(qrPayload: String, turnstileId: String): AccessDecision`
  - `reportOpticalPassage(turnstileId: String, timestamp: Long): Void`

### Internal Ports:
- `Port 50051 (gRPC)`: High-velocity binary protocol with sub-30ms latency for physical gate hardware.
- `Port 8080 (REST)`: Security dashboard management and manual overrides.

### Fault Tolerance Strategy:
- When central database connection latency exceeds 150ms, the component activates the Local Edge Cache, validating HMAC ticket signatures offline and batch-syncing checked-in tokens upon network recovery.
