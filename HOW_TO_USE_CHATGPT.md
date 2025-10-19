# How to Use All Tools in ChatGPT - No Copy-Paste Needed!

## The New Way (RECOMMENDED) - Automatic Data Flow

Thanks to automatic caching, you **no longer need to copy-paste data** between tools!

### Simple 2-Step Workflow:

**Step 1: Analyze Stakeholders**
```
Analyze these stakeholders:
Context: [Your negotiation context]

Stakeholders:
1. Actor A - Power: 0.8, Urgency: 0.9, Legitimacy: 0.85, Position: 0.6
2. Actor B - Power: 0.7, Urgency: 0.8, Legitimacy: 0.9, Position: -0.7
3. Actor C - Power: 0.5, Urgency: 0.6, Legitimacy: 0.7, Position: 0.5
```

ChatGPT will return the analysis with all stakeholders and their priority levels.

**Step 2: Develop Influence Tactics (FOR EACH STAKEHOLDER)**
```
Now develop influence tactics for [Stakeholder Name] using the latest analysis.
```

That's it! The system automatically retrieves the analysis you just ran.

---

## Complete Example: Riverland Crisis

### Step 1: Run Stakeholder Analysis
```
Analyze these 5 stakeholders involved in the Riverland humanitarian crisis:

Context: Complex multi-party humanitarian response requiring coordination between government, armed groups, NGOs, donors, and media.

Stakeholders:
1. Riverland Government - Power: 0.9, Urgency: 0.8, Legitimacy: 0.95, Position: 0.6
2. GRN (Armed Group) - Power: 0.7, Urgency: 0.9, Legitimacy: 0.3, Position: -0.8
3. Local NGOs - Power: 0.5, Urgency: 0.8, Legitimacy: 0.7, Position: 0.7
4. Donors - Power: 0.6, Urgency: 0.7, Legitimacy: 0.8, Position: 0.8
5. Media - Power: 0.4, Urgency: 0.6, Legitimacy: 0.6, Position: 0.5
```

**Response:** Analysis with all 5 stakeholders, their salience scores, and priority levels (First/Second/Third).

### Step 2a: Develop Tactics for Riverland Government
```
Now develop influence tactics for Riverland Government using the latest analysis.
```

**Response:** Specific tactics for Riverland Government, including coalition opportunities (Donors + Local NGOs identified as allies).

### Step 2b: Develop Tactics for GRN (Armed Group)
```
Now develop influence tactics for GRN using the latest analysis.
```

**Response:** Different tactics for GRN, recognizing them as adversarial (position: -0.8).

### Step 2c: Develop Tactics for Other Actors
Repeat for Donors, Media, Local NGOs - just change the name!

---

## Complete Tool Set Available

| # | Tool | Purpose | Input |
|---|------|---------|-------|
| **1** | Island of Agreement | Understand common ground | Situation + two parties |
| **2** | Icebergs | Dig into interests | Positions, reasoning, motives |
| **3** | Stakeholders | Prioritize actors | List of stakeholders with ratings |
| **4** | Leverage Influence (OLD) | Tactics (manual) | Name + full analysis data |
| **5** | **Leverage Influence Latest** | **Tactics (automatic!)** | **Just the stakeholder name** ⭐ |
| **6** | Guide | Reference | No input needed |

---

## Why This Works Better

**Before (Old Way):**
```
Tool 3: Analyze Stakeholders
↓ Get response
↓ Copy entire JSON
↓ Tool 4: Leverage Influence
↓ Paste JSON + target name
↓ Get tactics
```

**Now (New Way):**
```
Tool 3: Analyze Stakeholders
↓ Get response
↓ Tool 5: Leverage Influence Latest
↓ Just say target name
↓ Get tactics (automatically uses analysis)
```

---

## Setting Up in ChatGPT

1. Go to your Custom GPT → **Actions**
2. Replace your schema with: `OPENAI_COMPLETE_SCHEMA.json`
3. Server URL: `https://humanitarian-mcp-904769523449.us-central1.run.app`
4. You'll now have 6 tools available (including the new auto one!)

---

## Multiple Analyses in Session

The system keeps the **latest stakeholder analysis for 30 minutes**.

If you run a new stakeholder analysis, it replaces the old one.

- Run analysis for Riverland crisis
- Develop tactics for 5 stakeholders
- Then run analysis for different crisis
- Develop tactics for new stakeholders
- The system automatically switches to the new analysis

---

## Error Messages & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Stakeholder 'X' not found" | Name doesn't match exactly | Use exact name from analysis |
| "No cached analysis available" | You haven't run Tool 3 yet | Run stakeholder analysis first |
| "Cached analysis expired" | More than 30 min passed | Run stakeholder analysis again |

---

## Recommended Workflow for Complex Negotiations

```
1. Island of Agreement
   → Understand where you agree

2. Icebergs (optional)
   → Understand motivations

3. Stakeholders
   → Prioritize who matters most

4. Leverage Influence Latest (repeat for each key stakeholder)
   → Get specific tactics

5. Guide (reference)
   → Review best practices
```

---

## Pro Tips

- **Develop tactics for ALL stakeholders**, not just friendly ones
  - GRN (adversarial) tactics are just as important
  - Media (neutral) tactics help shape narrative

- **Update analysis after negotiation events**
  - Stakeholder positions change
  - Re-run analysis with new data
  - Develop new tactics accordingly

- **Use before/after analysis**
  - Run analysis before negotiation → develop tactics
  - Run analysis after → see what changed
  - Adjust strategy based on position changes

---

## Available Endpoints

All endpoints on: `https://humanitarian-mcp-904769523449.us-central1.run.app`

```
POST  /api/v1/island-of-agreement
POST  /api/v1/analyze-icebergs
POST  /api/v1/analyze-stakeholders        ← Feeds into Tools 4 & 5
POST  /api/v1/leverage-influence           ← Manual: requires full analysis data
POST  /api/v1/leverage-influence-latest    ← Automatic: uses cached data ⭐ NEW!
GET   /api/v1/guide
```

---

## Support

Deployment status: ✅ Always online on Google Cloud Run

Health check: `https://humanitarian-mcp-904769523449.us-central1.run.app/health`

All tools tested and working! 🎉
