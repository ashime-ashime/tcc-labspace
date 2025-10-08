# Interactive LabSpace with guided experience
FROM ubuntu:22.04

# Install basic tools for interactive experience
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    tree \
    less \
    && rm -rf /var/lib/apt/lists/*

# Copy lab content
COPY labspace-exercises/ /app/labspace-exercises/
COPY labspace.yaml /app/
COPY README.md /app/

# Create interactive lab starter script
RUN echo '#!/bin/bash\n\
\n\
show_menu() {\n\
    echo "🎉 Welcome to Testcontainers Cloud Lab for TSEs!"\n\
    echo "================================================="\n\
    echo ""\n\
    echo "📚 Available Exercises:"\n\
    echo "  1. TCC Basics (45 min) - Learn TCC fundamentals"\n\
    echo "  2. TCC Optimization (30 min) - Maximize free tier usage"\n\
    echo "  3. TCC Troubleshooting (45 min) - Handle real TSE scenarios"\n\
    echo "  4. Explore Lab Structure"\n\
    echo "  5. Exit"\n\
    echo ""\n\
    echo -n "Choose an option (1-5): "\n\
}\n\
\n\
start_exercise() {\n\
    local exercise=$1\n\
    local title=$2\n\
    \n\
    echo ""\n\
    echo "🚀 Starting: $title"\n\
    echo "================================"\n\
    cd /app/labspace-exercises/$exercise\n\
    \n\
    echo "📖 Reading exercise guide..."\n\
    echo ""\n\
    cat README.md\n\
    \n\
    echo ""\n\
    echo "🎯 Exercise started! Follow the steps above."\n\
    echo "💡 Use these commands to navigate:"\n\
    echo "   - ls -la                    # List files"\n\
    echo "   - tree                      # Show directory structure"\n\
    echo "   - cat README.md             # Re-read instructions"\n\
    echo "   - cd python                 # Go to Python examples"\n\
    echo "   - cd java                   # Go to Java examples"\n\
    echo "   - exit                      # Return to main menu"\n\
    echo ""\n\
    echo "Ready to start? Press Enter to continue..."\n\
    read\n\
}\n\
\n\
explore_structure() {\n\
    echo ""\n\
    echo "📁 Lab Structure:"\n\
    echo "================="\n\
    cd /app\n\
    tree labspace-exercises/\n\
    echo ""\n\
    echo "💡 Each exercise contains:"\n\
    echo "   - README.md: Step-by-step instructions"\n\
    echo "   - python/: Python code examples"\n\
    echo "   - java/: Java code examples"\n\
    echo ""\n\
}\n\
\n\
# Main menu loop\n\
while true; do\n\
    show_menu\n\
    read choice\n\
    \n\
    case $choice in\n\
        1)\n\
            start_exercise "tcc-basics" "TCC Basics"\n\
            ;;\n\
        2)\n\
            start_exercise "tcc-optimization" "TCC Optimization"\n\
            ;;\n\
        3)\n\
            start_exercise "tcc-troubleshooting" "TCC Troubleshooting"\n\
            ;;\n\
        4)\n\
            explore_structure\n\
            ;;\n\
        5)\n\
            echo "👋 Thanks for using the TCC Lab! Happy learning!"\n\
            exit 0\n\
            ;;\n\
        *)\n\
            echo "❌ Invalid option. Please choose 1-5."\n\
            echo ""\n\
            ;;\n\
    esac\n\
done' > /app/start-lab.sh && chmod +x /app/start-lab.sh

# Set working directory
WORKDIR /app

# Expose port for lab interface
EXPOSE 8080

# Default command - start interactive lab experience
CMD ["/app/start-lab.sh"]
