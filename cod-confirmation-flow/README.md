# COD Order Confirmation Flow (WhatsApp)

A returned COD parcel means you pay shipping out and shipping back, and sell nothing. This guide shows how to confirm every COD order on WhatsApp **before** you dispatch, so fewer parcels come back.

> Free guide from the founder-toolkit. Use it, copy it, share it.

---

## 1. Measure your return rate first (10 minutes)

**Return rate = parcels returned ÷ parcels dispatched × 100**, over the last 30 days.

| Question | Your number |
|---|---|
| COD parcels dispatched (last 30 days) | |
| COD parcels returned | |
| Return rate (%) | |
| Shipping cost per returned parcel (out + back) | |
| Monthly cost of returns (returned × cost) | |

That last number is your budget for fixing this.

## 2. The flow

```
Order placed
   │
   ▼
WhatsApp message within minutes:  "Confirm karein?"  [Confirm] [Cancel]
   │
   ├── Confirm ───────────────▶ Mark CONFIRMED ─▶ Ship
   │
   ├── Cancel ────────────────▶ Mark CANCELLED ─▶ Don't ship
   │
   └── No reply in a few hours ▶ One reminder
                                   ├── Confirm ▶ Ship
                                   └── Still no reply ▶ HOLD (call once, or cancel)
```

## 3. The message (example, edit to your brand)

> Assalam o Alaikum [Name]! Your order from [Store]:
> [Product], [Size], Rs [Amount] COD, delivery to [City].
> Confirm karein? Tap a button below.
> [✓ Confirm]  [Cancel]

Tips:
- [ ] Keep it short. One tap, no typing.
- [ ] Show the amount and city, so a wrong address gets caught.
- [ ] Write it in the language your customers use (Roman Urdu or English).

## 4. Checklist before you switch it on

- [ ] Use the **WhatsApp Business Platform (API)** through a provider, so buttons and automation work.
- [ ] Get the confirmation message approved as a **utility template**.
- [ ] Check Meta's current per-message rates for Pakistan. Template messages are paid per message, and since 1 October 2026 service replies beyond 1,000 a month per number are paid too.
- [ ] Customer gives their number at checkout and expects order updates (that's your opt-in). Don't use this number for marketing without separate consent.
- [ ] Connect it to your store (Shopify, WooCommerce or your own system) so orders get tagged automatically: `COD-CONFIRMED`, `COD-CANCELLED`, `COD-PENDING`.
- [ ] Decide the reminder time (for example 3 hours) and what happens after it (hold, call once, or cancel).
- [ ] Keep a log of every answer against the customer's number, so repeat refusers get flagged.

## 5. Track it for 30 days

| Metric | Before | After 30 days |
|---|---|---|
| Return rate (%) | | |
| Orders cancelled before dispatch | | |
| Orders on hold (no reply) | | |
| Monthly shipping lost to returns | | |

Cancelled-before-dispatch orders are a win: each one is a return you didn't pay for.

---

### 📞 Want this set up for your store? Book a call with me.

**Bilal | The Build Engineer**: AI agents, automation, websites and apps.
WhatsApp: +92 300 8982661 · Email: mbilalabid800@gmail.com
