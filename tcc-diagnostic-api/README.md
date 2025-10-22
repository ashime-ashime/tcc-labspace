# TCC Diagnostic API

## Overview

This mock API simulates Testcontainers Cloud API endpoints for realistic diagnostic investigations. It provides the same responses you would get from the real TCC API, using customer-specific data.

## Starting the API

```bash
cd /workspace/tcc-diagnostic-api
./start-api.sh
```

The API will run on `http://localhost:8080`.

## Available Endpoints

### Health Check (No Authentication)

```bash
curl http://localhost:8080/v1/health
```

**Response:**
```json
{
  "status": "operational",
  "timestamp": "2025-10-22T...",
  "version": "1.0.0"
}
```

### Account Information (Authentication Required)

```bash
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/account
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

### Usage Statistics (Authentication Required)

```bash
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/usage
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

## Authentication

### Valid Tokens

The following tokens are pre-configured for testing:

- `tcc-lab-token-12345` - Customer service account token
- `tcc-lab-org-12345` - Organization token

### Invalid Token Response

```bash
curl -H "Authorization: Bearer invalid-token" \
     http://localhost:8080/v1/account
```

Returns: `401 Unauthorized`

## Use Cases

### 1. Verify TCC Service Status

Check if TCC is operational:
```bash
curl http://localhost:8080/v1/health
```

If this fails, TCC service might be down.

### 2. Check Account Configuration

Understand the customer's plan and setup:
```bash
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/account
```

Look for plan type, billing model, and status.

### 3. Investigate Usage Patterns

Check current usage and limitations:
```bash
curl -H "Authorization: Bearer tcc-lab-token-12345" \
     http://localhost:8080/v1/usage
```

Compare usage against limits to identify constraints.

## When to Use This API

**Good for:**
- ✅ Verifying service health
- ✅ Checking account status and plan details
- ✅ Investigating usage patterns
- ✅ Understanding billing models
- ✅ Confirming authentication works

**Not needed if:**
- ❌ You find the answer in static files (logs, configs)
- ❌ The issue is obvious from customer data
- ❌ You prefer file-based investigation

## Tips

- Start with static files (logs, configs) first
- Use the API when you need dynamic account information
- Compare API responses with static customer data
- The API shows real-time state that complements file evidence

---

**This is an optional diagnostic tool - use it if you find it helpful!**

