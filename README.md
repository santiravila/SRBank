---
marp: true
---

# Topic: Bank Financial Service System

## Entities

### Customer
#### Attributes
- **id** (PK)
- **full name**
- **email**
- **registered_at**

---

### Account
#### Attributes
- **id** (PK)
- **customer_id** (FK)
- **balance** (lock)
- **type** (enum)
- **passwordhash** (encrypt)
- **created_at**

> **Business Logic & Security:**
> - Create a trigger in the `Transaction` table so that if an entry is `INSERTED`, the `balance` is automatically `UPDATED` in the `Account` table.
> - Make customer transactions only accessible through a view so only transactions of a *GIVEN* customer ID are shown without proper privileges.

---

### Transaction
#### Attributes
- **id** (PK)
- **account_id** (FK)
- **wire_event_id** (FK)
- **amount**
- **type**
- **timestamp**

---

### Wire_event
#### Attributes
- **id** (PK)
- **amount**