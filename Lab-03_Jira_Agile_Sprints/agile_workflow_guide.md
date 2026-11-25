# Sprint Backlog & User Story Specifications

## Story SEMS-102: Distributed Seat Reservation Lock

### User Story:
> **As an** Event Attendee,  
> **I want** selected seats to be reserved exclusively for me for 10 minutes during checkout,  
> **So that** another user does not purchase the same seats while I am entering payment details.

### Complexity: 8 Story Points (Fibonacci)
- Involves distributed lock orchestration using Redis Redlock algorithm.
- Requires automatic expiry TTL and event bus notifications.

### Acceptance Criteria (Gherkin Format):
```gherkin
Feature: Temporary Seat Lock during Checkout

  Scenario: Successful seat lock when seats are unoccupied
    Given seat "A-12" in match "Derby-2026" has status "AVAILABLE"
    When user "Amith" clicks "Select Seat"
    Then the system should assign status "LOCKED" to seat "A-12"
    And a 10-minute countdown timer should start for user "Amith"
    And other users viewing the seating map should see "A-12" marked as "PENDING"

  Scenario: Expiration of lock when checkout is abandoned
    Given user "Amith" holds lock on seat "A-12" with 1 second remaining
    When the 10-minute timer expires without payment confirmation
    Then the Redis lock should be automatically evicted
    And seat "A-12" status should revert to "AVAILABLE"
    And a WebSocket update should broadcast the release to all active clients
```

---

## Story SEMS-104: High-Velocity Turnstile QR Validation

### User Story:
> **As a** Turnstile Gate Operator,  
> **I want** the scanner to validate ticket credentials in under 50 milliseconds,  
> **So that** crowd throughput exceeds 30 spectators per minute per turnstile without queue build-up.

### Acceptance Criteria:
```gherkin
Feature: High-Speed Gate Validation

  Scenario: Valid attendee scans pass at correct gate
    Given ticket with JWT payload "TK-98213" has status "CONFIRMED"
    And ticket match date matches today's date
    And ticket stand matches "Gate West 2"
    When the scanner reads the QR code
    Then the response latency must be less than 50 milliseconds
    And the gate relay should receive an "UNLOCK_SINGLE" signal
    And ticket status should update to "CHECKED_IN"
```
