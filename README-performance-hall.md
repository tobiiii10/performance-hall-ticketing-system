# Performance Hall Ticketing System

A desktop ticketing system for live music and performance events, built in Java with a Swing GUI. Supports two distinct user roles — administrators who manage the event catalogue, and customers who browse, book and pay.

Built as a second-year coursework project at Loughborough University (Mar – Jun 2025).

---

## What it does

**Administrators can**
- Create and edit events in the catalogue
- Manage ticket stock levels
- View and update inventory in real time as bookings come in

**Customers can**
- Browse the event listings
- Search by event ID and filter by language
- Add tickets to a basket and check out
- Pay by credit card or PayPal
- Receive an itemised receipt on completion

---

## Built with

- **Java** — core application logic
- **Java Swing** — desktop GUI for both the admin and customer views
- **Buffered file I/O** — stock persistence and receipt generation

No external dependencies.

---

## Running it

```bash
javac *.java
java Main
```

> Adjust the entry-point class name if yours differs.

---

## Design decisions

**Role separation over a single interface.** Admin and customer functions run through separate flows rather than one screen with hidden controls. It keeps the stock-modifying operations in one place, which made the write paths far easier to reason about when bookings and stock updates started interacting.

**Object-oriented structure throughout.** Encapsulation keeps stock state private and mutable only through defined methods, so a booking can never leave inventory in an inconsistent state. Inheritance and interfaces let the two payment paths — card and PayPal — share a contract while differing in how each generates its receipt. Enums handle the fixed sets (payment types, event categories) that would otherwise have been error-prone string comparisons.

**Receipts through `toString()` overrides.** Each payment type formats its own receipt, so adding a third payment method means implementing one interface rather than editing a central formatting block.

**File-backed persistence rather than a database.** `BufferedReader` and `BufferedWriter` handle stock reads and writes. A database would have been more robust, but the brief called for a self-contained application and file I/O kept it genuinely runnable anywhere with a JRE.

---

## What I'd do differently

The stock file is read and written on every transaction, which is fine at coursework scale and would not survive concurrent users. A proper implementation would hold state in memory with periodic flushes, or move to an embedded database such as SQLite.

There are no automated tests. Given the payment and stock logic, that is the first thing I would add.
