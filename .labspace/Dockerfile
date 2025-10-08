# LabSpace-compatible Dockerfile
FROM nginx:alpine

# Install basic tools for LabSpace
RUN apk add --no-cache \
    python3 \
    py3-pip \
    curl \
    git

# Copy lab content
COPY . /usr/share/nginx/html/

# Create a simple index.html for LabSpace navigation
COPY <<EOF /usr/share/nginx/html/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Testcontainers Cloud Lab for TSEs</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .exercise { background: #f5f5f5; padding: 20px; margin: 20px 0; border-radius: 5px; }
        h1 { color: #333; }
        h2 { color: #666; }
        a { color: #007bff; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>🌐 Testcontainers Cloud (TCC) Lab for TSEs</h1>
    <p>Master Testcontainers Cloud through hands-on exercises and real TSE troubleshooting scenarios.</p>
    
    <div class="exercise">
        <h2>📚 Exercises</h2>
        <ul>
            <li><a href="/labspace-exercises/tcc-setup/README.md">Exercise 1: TCC Architecture and Advanced Configuration</a></li>
            <li><a href="/labspace-exercises/tcc-github-actions/README.md">Exercise 2: Enterprise TCC CI/CD Integration</a></li>
            <li><a href="/labspace-exercises/tcc-troubleshooting/README.md">Exercise 3: Advanced TSE TCC Troubleshooting</a></li>
        </ul>
    </div>
    
    <div class="exercise">
        <h2>📋 Lab Information</h2>
        <ul>
            <li><strong>Difficulty:</strong> Advanced</li>
            <li><strong>Duration:</strong> 3-4 hours</li>
            <li><strong>Target:</strong> Senior TSEs</li>
        </ul>
    </div>
    
    <div class="exercise">
        <h2>🔗 Resources</h2>
        <ul>
            <li><a href="https://testcontainers.com/cloud/">Testcontainers Cloud Documentation</a></li>
            <li><a href="https://testcontainers.com/desktop/">Testcontainers Desktop</a></li>
            <li><a href="https://testcontainers.com/">Testcontainers Main Site</a></li>
        </ul>
    </div>
</body>
</html>
EOF

# Expose port for web interface
EXPOSE 80