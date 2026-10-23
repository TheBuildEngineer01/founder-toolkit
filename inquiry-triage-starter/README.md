# Inquiry Triage Starter

**It's 11:47 PM. A customer asks "Is this available? How much?" You reply at 9 AM. They've already bought elsewhere.**

This small, free Python script is a starting point for an **automatic first reply**. It:

1. **Sorts** each customer message into `ORDER`, `QUESTION`, `COMPLAINT` or `OTHER`
2. **Pulls out details** such as quantity, city and urgency
3. **Flags hot leads** (orders and urgent messages)
4. **Drafts a polite first reply** from templates you control

It works with English and common Roman Urdu phrases ("kitne ka hai", "chahiye", "kharab").

> Rule-based on purpose: no API keys, no monthly cost, easy to read. When you need smarter sorting, swap `classify()` for an AI model.

---

## Quick start

Requires Python 3.8+. There are no extra packages to install.

```bash
python triage.py "Hi! Is this still available? How much?"
python triage.py --file sample_messages.txt
python triage.py --file sample_messages.txt --json   # for connecting to other tools
```

Example output:

```
[ORDER]  🔥 HOT LEAD  Need 5 units urgent, can you deliver today in Karachi?
   details: {'quantity': 5, 'city': 'Karachi', 'urgent': True}
   reply:   Thanks for your order request! We've received it and will confirm shortly.

[COMPLAINT]  My parcel arrived damaged, I want a refund
   reply:   We're really sorry about this. A team member will personally look into it ...
```

## Make it yours

Edit **`rules.json`**:

- `keywords`: the words that mark an order, question, complaint or urgent message
- `cities`: the places you deliver to
- `replies`: your own first-reply templates
- `ask_for`: details to request automatically when they're missing

## What this is (and isn't)

This is a **starter / demo**, not a finished product. A production setup would also connect to your actual channels (for example, the WhatsApp Business Platform or your website chat) and add a human handover and a follow-up schedule. Each channel has its own messaging rules, so check them before automating replies.

---

## About

Made by **Bilal | The Build Engineer**, an individual software developer in Lahore, Pakistan, building web apps, Flutter mobile apps, SaaS/MVPs, backends and AI automation for local and international clients.

*Turning ideas into smart digital solutions.*

### 📞 Losing customers at night? Book a call with me.
We'll map how your inquiries come in and what a smart first reply should do for your business.

- 📱 WhatsApp: **+92 300 8982661**
- 📧 Email: **mbilalabid800@gmail.com**
- 🌐 @thebuildengineer01 on Instagram, Facebook, YouTube, TikTok, X and Threads

## License

MIT. Free to use, copy and share.
