# 04 — Build Log

**Client:** `<client name>`
**Stage:** Implementation
**Date range:** `<start>` → `<end>`
**Input:** [03-roadmap.md](03-roadmap.md)

Goal: record each control as it's built — what it was before, what changed, why, and the evidence. Write each entry so a client engineer understands it without you in the room. This doubles as audit evidence.

> Use one entry per control. Copy the block. Group by area (AI / CI / platform / cloud) if helpful.

---

## Entry template (copy per control)

### `<control name>` (`<control ID>`)
- **Before:** `<the state that was a problem>`
- **Change:** `<what you implemented>`
- **Why:** `<the risk this closes, in plain terms>`
- **Evidence:** `<diff / config / manifest / test / scan output — where it lives>`
- **Status:** `<built — pending validation | built + validated>`

---

## Built this engagement

*(fill in — examples of the kinds of entries that go here)*

### `<e.g. Tenant isolation>` (`<AC-3, AC-4>`)
- **Before:** `<...>`
- **Change:** `<...>`
- **Why:** `<...>`
- **Evidence:** `<...>`
- **Status:** built — pending validation

### `<e.g. CI security gates>` (`<SA-11, SI-2, IA-5>`)
- **Before:** `<...>`
- **Change:** `<...>`
- **Why:** `<...>`
- **Evidence:** `<...>`
- **Status:** built — pending validation

`<add entries for each control in the roadmap>`

---

## Deliberately not "done" yet

List what's built but not yet *proven*. These carry into validation and only count as done once tested.

- [ ] `<control>` — built, not yet validated against `<the specific test>`
- [ ] `<control>` — built, not yet validated against `<the specific test>`

That's the handoff to the next stage.

→ Next: **[05-validation-checklist.md](05-validation-checklist.md)**.
