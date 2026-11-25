# Use Case Specifications: Sports Event Crowd Management System

## Use Case UC-02: Book Event Tickets

| Field | Detail |
|---|---|
| **Use Case ID** | UC-02 |
| **Use Case Name** | Book Event Tickets |
| **Primary Actor** | Registered Spectator |
| **Secondary Actor** | Payment Gateway Service |
| **Stakeholders & Interests** | Spectator (wants verified seat with instant ticket), Organizer (maximizes attendance & timely payment settlement) |
| **Preconditions** | User must be authenticated; selected match must have available seat inventory. |
| **Postconditions** | Seat inventory is decremented; payment ledger updated; digital QR ticket pass generated and sent via email/SMS. |

### Main Success Scenario (Basic Flow):
1. Spectator selects an upcoming tournament match and views the stadium seating layout.
2. Spectator chooses the desired seating stand (VIP, General, Pavilion) and quantity of seats.
3. System temporarily locks selected seats for 10 minutes and computes total price with booking fees.
4. Spectator confirms booking details and proceeds to payment.
5. System invokes Payment Gateway Subsystem (`<<include>> UC-03: Process Payment`).
6. Payment Gateway returns transaction success authorization code.
7. System transitions seat status from `RESERVED` to `CONFIRMED`.
8. System invokes `<<include>> UC-04: Issue Digital QR Pass` and displays booking confirmation screen.

### Extensions (Alternative Flows):
- **3a. Seats Become Unavailable During Selection:**
  - System notifies spectator that selected seats have just been reserved.
  - Returns to Step 1 with updated real-time seating map.
- **5a. Payment Fails or Times Out:**
  - System cancels temporary seat reservation lock.
  - Displays error reason (insufficient funds, gateway timeout) with option to retry within 2 minutes.

---

## Use Case UC-05: Scan Ticket at Turnstile Gate

| Field | Detail |
|---|---|
| **Use Case ID** | UC-05 |
| **Use Case Name** | Scan Ticket at Turnstile Gate |
| **Primary Actor** | Turnstile Security Staff / Automated Turnstile Barcode Reader |
| **Preconditions** | Turnstile IoT reader is online and connected to local edge server / master database. |
| **Postconditions** | Turnstile unlocks for single passenger entry; ticket status changed to `CHECKED_IN`; ingress timestamp logged. |

### Main Success Scenario:
1. Spectator presents digital or printed QR pass to turnstile scanner.
2. Scanner decodes cryptographic JWT token from QR code.
3. System invokes `<<include>> UC-06: Validate Ticket Credential` against local ingress cache.
4. System verifies ticket validity: correct date, gate match, and not previously used.
5. System sends turnstile unlock signal (green indicator).
6. Spectator passes through turnstile optical beams; gate locks.
7. System marks ticket as `CHECKED_IN` and logs entry gate ID and timestamp.

### Extensions:
- **4a. Duplicate Entry Detected (Anti-Passback Rule):**
  - System identifies ticket as already used at `Gate 3` at `18:42:10`.
  - Gate remains locked, red alarm sounds, event security notified.
- **4b. Network Partition / Local Edge Fallback:**
  - Ingress gateway falls back to local SQLite edge replica; verifies offline HMAC signature; queues sync event.
