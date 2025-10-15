# How the Mock API Helps TSEs - Demonstration

## 🎯 The TSE Investigation Value

The mock API server provides **CONCRETE EVIDENCE** that TSEs can use to solve the customer's problem. Here's what happens:

### 1. Health Check Response
```bash
curl http://localhost:8080/v1/health
```

**Response:**
```json
{
  "status": "operational",
  "timestamp": "2025-10-15T01:22:06.207276",
  "version": "1.0.0"
}
```

**TSE Insight:** ✅ Service is operational - NOT a connectivity issue

### 2. Account Details Response
```bash
curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account
```

**Response:**
```json
{
  "org_id": "3294",
  "plan_type": "trial_legacy",
  "status": "active",
  "billing_model": "separate_tcc_billing",
  "docker_pro_plan": "legacy_subscription",
  "tcc_included": false
}
```

**TSE Insights:** 
- ✅ Legacy trial plan (limited quota)
- ✅ Separate TCC billing (not included in Docker Pro)
- ✅ This explains the quota limitations

### 3. Usage Status Response (THE SMOKING GUN!)
```bash
curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/usage
```

**Response:**
```json
{
  "free_tier_minutes": 50,
  "current_month_usage": 52,
  "quota_exceeded": true,
  "quota_reset": "never",
  "last_successful_ci": "2025-01-08T14:22:00Z",
  "quota_exhausted_date": "2025-01-09T00:00:00Z"
}
```

**TSE Insights:** 🎯 **ROOT CAUSE IDENTIFIED!**
- ❌ Quota exceeded: 52/50 minutes used
- ❌ No quota reset (one-time trial)
- ❌ Last successful CI was before quota exhaustion
- ✅ Timeline matches customer's "48 hours ago" report

## 🔍 Investigation Process for TSEs

### Before Mock API:
- ❌ TSE reads static files
- ❌ No hands-on testing
- ❌ Theoretical investigation
- ❌ Hard to build confidence

### With Mock API:
- ✅ TSE runs real diagnostic commands
- ✅ Sees actual API responses
- ✅ Gets concrete evidence
- ✅ Builds confidence in solution
- ✅ Practices real troubleshooting skills

## 💡 The "Aha!" Moment

When TSEs see `"quota_exceeded": true` and `"current_month_usage": 52`, they have:

1. **Concrete evidence** of the root cause
2. **Timeline confirmation** (matches customer's 48-hour report)
3. **Plan type understanding** (legacy trial limitations)
4. **Confidence** in their diagnosis
5. **Real experience** with TCC API troubleshooting

## 🎯 Why This Helps TSEs

**Real-world skills:** TSEs practice actual diagnostic commands they'd use with real customers

**Evidence-based investigation:** Instead of guessing, they see concrete data

**Confidence building:** Hands-on experience builds troubleshooting confidence

**Professional preparation:** Simulates real TSE investigation workflows

**Problem-solving practice:** Teaches systematic diagnostic approach

This transforms the lab from "reading about troubleshooting" to "actually doing troubleshooting" - exactly what TSEs need!
