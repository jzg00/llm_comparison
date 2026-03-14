# LLM Code Quality Analysis

### Overview
This project generates responses from various large lanuage models (LLMs) prompted with coding tasks in Python. Their responses are evaluated and analyzed against Python quality standards and other metrics.

#### API / Models used
LLM responses are generated through their repective APIs instead of through the web browser. This is to avoid personalized responses and to make the responses more deterministic.
The current latest iteration of default models from ChatGPT and Claude are used:
+ ChatGPT (Chat Comlpletions API) - gpt-5.3-chat-latest
+ Claude - Sonnet 4.6


#### Metrics
+ **Pylint Score** - Quality score based on errors, potential issues, and compliance to PEP8 style guide

+ **Pylint Violations** - Provides the number of violations for main violation types (Fatal, Error, Warning, Refactor, Convention)

+ **Tests Passed** - Unit testing to check functionality and correctness of logic

+ **Lines of Code (LOC)** - Used as a normalizer (e.g violations per 100 LOC). Also provides context on conciseness vs verbosity of each LLM
