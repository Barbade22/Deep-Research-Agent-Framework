```markdown
# Organizational Research Scraper

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI powerful web scraping and data extraction tool designed to gather comprehensive information about organizations using search engines, language models, and data refinement techniques.

## Features
- Automated multi-source data collection
- AI-powered data validation and refinement
- Customizable research parameters
- Structured JSON output
- Error handling and progress tracking

## Overview

This project automates the research process by:
- Taking organization names as input
- Generating specific questions about each organization
- Searching the web for relevant information
- Processing and validating search results
- Extracting structured data
- Storing results in JSON format

## Use Cases

This tool can be adapted for various applications:

1. **Competitive Analysis**: Research competitors to understand their structure, offerings, and market positioning
2. **Investment Research**: Gather information about potential investment targets
3. **Recruitment Intelligence**: Research potential employers or partners
4. **Market Research**: Collect data about organizations in specific industries
5. **Academic Research**: Gather structured data about organizations for academic studies
6. **Due Diligence**: Perform preliminary research for mergers and acquisitions
7. **Sales Prospecting**: Research potential clients before outreach

## Potential Modifications

The framework can be easily modified for different use cases:

### For Academic Research
- Modify `questions.py` to focus on academic publications, research grants, and faculty information
- Add citation tracking and academic metrics collection

### For Market Analysis
- Update the schema in `generate_json_schema()` to include market share, growth metrics, and competitor analysis
- Add industry-specific question sets

### For Job Market Research
- Modify questions to focus on hiring trends, salary information, and employee reviews
- Integrate with job posting APIs

### For Product Research
- Adapt the system to gather information about products instead of organizations
- Modify the schema to include product specifications, pricing, and reviews

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/organizational-research-scraper.git
cd organizational-research-scraper
 ```
```

2. Install dependencies:
```bash
pip install requests tavily-python python-dotenv
 ```
```

3. Configuration:
- Get a Tavily API key from Tavily
- Create a .env file and add your API key:
```bash
TAVILY_API_KEY=your_api_key_here
 ```

## Usage
1. Create a text file named org.txt with a list of organizations to research:
```plaintext
Apex Global Solutions
Horizon Business Alliance
Nexus Technology Partners
 ```

2. Run the main script:
```bash
python main.py
 ```

3. Results will be saved to Org_research.json
## Project Structure File Description main.py

Main orchestration script llm.py

Handles language model interactions searchengine.py

Manages web search functionality questions.py

Defines research questions refinery.py

Data refinement and formatting validator.py

Information validation system worker.py

Data extraction workers supervoiser.py

Extraction process supervision
## Configuration
Edit these files for customization:

- questions.py : Modify research questions and fields
- refinery.py : Adjust data formatting rules
- searchengine.py : Configure search parameters
## Dependencies
- Python 3.6+
- Requests - HTTP library
- Tavily - Search API
- Ollama - Local LLM server
- python-dotenv - Environment management
## License
Distributed under the MIT License. See LICENSE for more information.

## Acknowledgments
- Tavily for their powerful search API
- Ollama for local LLM capabilities
- Python community for excellent tooling