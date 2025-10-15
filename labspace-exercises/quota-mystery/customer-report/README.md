# Customer Report - Diagnostic Tools

## 🔧 Mock TCC API Server

To make the TSE investigation more realistic and interactive, this directory includes a mock Testcontainers Cloud API server that simulates real API responses.

### Mock Server Status

**The mock TCC API server starts automatically and silently in the background.** It provides realistic API responses based on the customer's actual data on `http://localhost:8080`. No spoiler information is shown during startup to preserve the mystery for TSEs.

### Pre-configured Test Tokens

The mock server includes valid tokens for testing:

- **`tcc-lab-token-12345`** - Customer service account token
- **`tcc-lab-org-12345`** - Organization token

### Diagnostic Commands to Test

TSEs can execute these diagnostic commands during the investigation (available through the interactive game):

```bash
# 1. Check TCC service health
curl http://localhost:8080/v1/health

# 2. Check account details (requires authentication)
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/account

# 3. Check usage and quota status (requires authentication)
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/usage
```

### Expected Responses

#### Health Check (200 OK)
```json
{
  "status": "operational",
  "timestamp": "2025-10-14T21:07:06.207276",
  "version": "1.0.0"
}
```

#### Account Details (200 OK)
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

#### Usage Status (200 OK)
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

#### Invalid Token (401 Unauthorized)
```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 401</p>
        <p>Message: Unauthorized - Invalid or missing token.</p>
        <p>Error code explanation: 401 - No permission -- see authorization schemes.</p>
    </body>
</html>
```

## 🎯 Investigation Value

This mock API allows TSEs to:

1. **Test diagnostic commands** in a realistic environment during the interactive game
2. **Experience real API responses** without needing actual TCC credentials
3. **Understand authentication flows** and error handling
4. **Verify quota status** and billing model differences
5. **Practice troubleshooting** with live API interactions
6. **Discover clues progressively** without spoiler information

## 🔍 Investigation Process

**TSEs must discover these insights through the interactive investigation:**
- **Service is operational** (health check passes)
- **Authentication works** (valid tokens get 200 responses)
- **Quota is exceeded** (52/50 minutes used)
- **Billing model is separate** (tcc_included: false)
- **Plan type is legacy** (trial_legacy)

**The mystery is preserved until TSEs run the diagnostic tools themselves!**
