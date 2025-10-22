#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Simple welcome message - no interactive menu
echo -e "${CYAN}🚀 Testcontainers Cloud (TCC) Lab for TSEs${NC}"
echo -e "${CYAN}==========================================${NC}"
echo ""
echo -e "${GREEN}✅ Pre-configured Environment Ready!${NC}"
echo -e "${GREEN}✅ TCC account: tcc-lab-org-12345${NC}"
echo -e "${GREEN}✅ Service account token: Configured${NC}"
echo -e "${GREEN}✅ Testcontainers Desktop: Simulated${NC}"
echo ""
echo -e "${YELLOW}📚 Available Break-and-Fix Exercise:${NC}"
echo ""
echo -e "${PURPLE}1. The Quota Mystery${NC}"
echo -e "   🎯 TCC Billing & Quota Investigation"
echo -e "   📁 Location: labspace-exercises/quota-mystery/"
echo -e "   ⏱️  Duration: 45 minutes"
echo ""
echo -e "${YELLOW}🎮 Interactive Investigation Game:${NC}"
echo -e "${BLUE}• Start Mystery Game:${NC} cd labspace-exercises/quota-mystery && ./start-investigation.sh"
echo -e "${BLUE}• Investigation Engine:${NC} python3 .investigation-engine.py"
echo ""
echo -e "${YELLOW}📋 Traditional Mode:${NC}"
echo -e "${BLUE}• Read Exercise:${NC} cat README.md"
echo -e "${BLUE}• Investigation Guide:${NC} cat tse-investigation/README.md"
echo ""
echo -e "${YELLOW}💡 Investigation Tips:${NC}"
echo -e "• Use 'cat' to view customer reports and logs"
echo -e "• Use 'cd' to navigate to exercise directories"
echo -e "• Use 'ls -la' to see all investigation materials"
echo -e "• Use 'grep' to search for specific information"
echo ""
echo -e "${CYAN}==========================================${NC}"
echo -e "${GREEN}Ready to investigate! Happy troubleshooting!${NC}"
echo -e "${CYAN}==========================================${NC}"
echo ""
echo -e "${YELLOW}🎯 To start investigating, run:${NC}"
echo -e "${BLUE}  cd labspace-exercises/quota-mystery${NC}"
echo -e "${BLUE}  cat README.md${NC}"
echo ""
