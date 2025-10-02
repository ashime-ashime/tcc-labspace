# Deployment Guide

This guide explains how to deploy the Docker Testcontainers Lab to GitHub and make it available for TSEs.

## Prerequisites

- GitHub account with appropriate permissions
- Git installed locally
- Access to the lab repository

## Deployment Steps

### Step 1: Prepare the Repository

1. **Initialize Git Repository:**
   ```bash
   cd "Docker Testcontainer Lab test"
   git init
   git add .
   git commit -m "Initial commit: Docker Testcontainers Lab"
   ```

2. **Create .gitignore:**
   ```bash
   cat > .gitignore << EOF
   # IDE files
   .idea/
   .vscode/
   *.swp
   *.swo
   
   # OS files
   .DS_Store
   Thumbs.db
   
   # Language-specific
   # Java
   target/
   *.class
   *.jar
   
   # Node.js
   node_modules/
   npm-debug.log*
   yarn-debug.log*
   yarn-error.log*
   
   # Python
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   .Python
   venv/
   env/
   
   # Go
   *.exe
   *.exe~
   *.test
   *.out
   
   # Test results
   coverage/
   test-results/
   
   # Environment files
   .env
   .env.local
   .env.*.local
   EOF
   ```

### Step 2: Create GitHub Repository

1. **Create New Repository on GitHub:**
   - Go to GitHub and create a new repository
   - Name it `docker-testcontainers-lab`
   - Make it public or private based on your organization's needs
   - Don't initialize with README (we already have one)

2. **Add Remote and Push:**
   ```bash
   git remote add origin https://github.com/YOUR_ORG/docker-testcontainers-lab.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Set Up Repository Structure

1. **Create Branch for Each Language:**
   ```bash
   # Create feature branches for different language tracks
   git checkout -b java-examples
   git push -u origin java-examples
   
   git checkout -b go-examples
   git push -u origin go-examples
   
   git checkout -b nodejs-examples
   git push -u origin nodejs-examples
   
   git checkout -b python-examples
   git push -u origin python-examples
   ```

2. **Set Up Branch Protection Rules:**
   - Go to repository settings
   - Enable branch protection for `main` branch
   - Require pull request reviews
   - Require status checks

### Step 4: Configure GitHub Actions (Optional)

Create CI/CD pipeline for automated testing:

1. **Create GitHub Actions Workflow:**
   ```bash
   mkdir -p .github/workflows
   ```

2. **Java CI Workflow:**
   ```yaml
   # .github/workflows/java-ci.yml
   name: Java CI
   
   on:
     push:
       branches: [ main, java-examples ]
       paths: [ 'exercises/java/**' ]
     pull_request:
       branches: [ main, java-examples ]
       paths: [ 'exercises/java/**' ]
   
   jobs:
     test:
       runs-on: ubuntu-latest
       
       services:
         docker:
           image: docker:20.10.16-dind
           options: --privileged
       
       steps:
       - uses: actions/checkout@v3
       
       - name: Set up JDK 11
         uses: actions/setup-java@v3
         with:
           java-version: '11'
           distribution: 'temurin'
       
       - name: Cache Maven dependencies
         uses: actions/cache@v3
         with:
           path: ~/.m2
           key: ${{ runner.os }}-m2-${{ hashFiles('**/pom.xml') }}
       
       - name: Run tests
         run: |
           cd exercises/java
           mvn clean test
   ```

3. **Multi-language CI Workflow:**
   ```yaml
   # .github/workflows/test-all.yml
   name: Test All Languages
   
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]
   
   jobs:
     java:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v3
       - name: Set up JDK 11
         uses: actions/setup-java@v3
         with:
           java-version: '11'
           distribution: 'temurin'
       - name: Run Java tests
         run: |
           cd exercises/java
           mvn clean test
   
     go:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v3
       - name: Set up Go
         uses: actions/setup-go@v3
         with:
           go-version: '1.19'
       - name: Run Go tests
         run: |
           cd exercises/go
           go test -v
   
     nodejs:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v3
       - name: Set up Node.js
         uses: actions/setup-node@v3
         with:
           node-version: '18'
           cache: 'npm'
           cache-dependency-path: exercises/nodejs/package-lock.json
       - name: Run Node.js tests
         run: |
           cd exercises/nodejs
           npm ci
           npm test
   
     python:
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v3
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.9'
       - name: Install dependencies
         run: |
           cd exercises/python
           pip install -r requirements.txt
       - name: Run Python tests
         run: |
           cd exercises/python
           pytest -v
   ```

### Step 5: Set Up Documentation

1. **Enable GitHub Pages:**
   - Go to repository settings
   - Navigate to Pages section
   - Enable GitHub Pages from main branch
   - Use `/docs` folder as source

2. **Create Documentation Structure:**
   ```bash
   mkdir docs
   cp README.md docs/index.md
   cp docs/*.md docs/
   ```

3. **Add Jekyll Configuration:**
   ```yaml
   # docs/_config.yml
   title: Docker Testcontainers Lab
   description: Comprehensive hands-on lab for learning Docker Testcontainers
   theme: minima
   plugins:
     - jekyll-feed
   ```

### Step 6: Configure Repository Settings

1. **Repository Description:**
   - Add description: "Comprehensive hands-on lab for learning Docker Testcontainers"
   - Add topics: `testcontainers`, `docker`, `testing`, `integration-testing`, `lab`

2. **Issue Templates:**
   ```bash
   mkdir -p .github/ISSUE_TEMPLATE
   ```

   Create issue template:
   ```markdown
   # .github/ISSUE_TEMPLATE/bug_report.md
   ---
   name: Bug report
   about: Create a report to help us improve
   title: '[BUG] '
   labels: bug
   assignees: ''
   
   ---
   
   **Describe the bug**
   A clear and concise description of what the bug is.
   
   **To Reproduce**
   Steps to reproduce the behavior:
   1. Go to '...'
   2. Click on '....'
   3. Scroll down to '....'
   4. See error
   
   **Expected behavior**
   A clear and concise description of what you expected to happen.
   
   **Screenshots**
   If applicable, add screenshots to help explain your problem.
   
   **Environment:**
   - OS: [e.g. Windows, macOS, Linux]
   - Docker version: [e.g. 20.10.16]
   - Testcontainers version: [e.g. 1.19.3]
   - Language: [e.g. Java, Go, Node.js, Python]
   
   **Additional context**
   Add any other context about the problem here.
   ```

3. **Pull Request Template:**
   ```markdown
   # .github/pull_request_template.md
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Refactoring
   
   ## Testing
   - [ ] Tests pass locally
   - [ ] Added new tests
   - [ ] Updated existing tests
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   ```

### Step 7: Create Release

1. **Create First Release:**
   ```bash
   git tag -a v1.0.0 -m "Initial release of Docker Testcontainers Lab"
   git push origin v1.0.0
   ```

2. **Create Release Notes:**
   - Go to repository releases
   - Create new release with tag v1.0.0
   - Add release notes describing the lab contents

### Step 8: Set Up Collaboration

1. **Add Collaborators:**
   - Go to repository settings
   - Add team members as collaborators
   - Set appropriate permissions

2. **Create Discussion Categories:**
   - Enable GitHub Discussions
   - Create categories: General, Q&A, Bug Reports, Feature Requests

3. **Set Up Project Board:**
   - Create project board for tracking lab improvements
   - Add columns: To Do, In Progress, Review, Done

## Post-Deployment Checklist

- [ ] Repository is accessible to TSEs
- [ ] All documentation is properly formatted
- [ ] CI/CD pipelines are working
- [ ] Issues and pull request templates are configured
- [ ] Branch protection rules are set up
- [ ] Collaborators have appropriate access
- [ ] GitHub Pages is enabled and working
- [ ] First release is created
- [ ] Discussion categories are set up
- [ ] Project board is configured

## Maintenance

### Regular Tasks

1. **Monitor Issues and Discussions:**
   - Respond to questions and bug reports
   - Update documentation based on feedback
   - Track usage and adoption

2. **Update Dependencies:**
   - Regularly update Testcontainers versions
   - Update language-specific dependencies
   - Test compatibility with new versions

3. **Content Updates:**
   - Add new exercises based on feedback
   - Update troubleshooting guides
   - Improve documentation clarity

### Version Management

1. **Semantic Versioning:**
   - Use semantic versioning for releases
   - Document breaking changes
   - Maintain backward compatibility when possible

2. **Release Process:**
   - Create release branches for major updates
   - Test thoroughly before release
   - Document changes in release notes

## Support and Community

### Getting Help

1. **Internal Support:**
   - Create internal Slack channel for lab discussions
   - Set up regular office hours for TSEs
   - Create FAQ based on common questions

2. **External Resources:**
   - Link to Testcontainers community resources
   - Provide links to official documentation
   - Share relevant blog posts and tutorials

### Feedback Collection

1. **Feedback Mechanisms:**
   - Use GitHub issues for bug reports
   - Use GitHub discussions for questions
   - Create feedback surveys periodically

2. **Continuous Improvement:**
   - Analyze feedback to identify improvement areas
   - Prioritize updates based on user needs
   - Iterate on lab content and structure

This deployment guide ensures your Docker Testcontainers Lab is properly set up on GitHub and ready for TSEs to use effectively.
