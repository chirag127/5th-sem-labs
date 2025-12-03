---
name: Bug Report
about: Report a bug in the Academic Data Science Automation Toolkit
title: "Bug: [Brief Description of Bug]"
labels: "bug"
assignees: "chirag127"

body:
  - type: markdown
    attributes:
      value: | 
        ### 🐛 Bug Report
        Please provide a clear and concise description of the bug you are experiencing. Ensure you have reviewed the [CONTRIBUTING.md](https://github.com/chirag127/Academic-Data-Science-Automation-Toolkit-Python/blob/main/.github/CONTRIBUTING.md) guidelines before submitting.

        **Important:** For security-related issues, please refer to our [SECURITY.md](https://github.com/chirag127/Academic-Data-Science-Automation-Toolkit-Python/blob/main/.github/SECURITY.md) policy.

  - type: markdown
    attributes:
      value: | 
        --- 

        ## 1. Environment Details
        This section helps us understand the context in which the bug occurred.

  - type: input
    id: version
    attributes:
      label: Toolkit Version
      description: "The specific version of the toolkit you are using (e.g., 1.2.0 or the commit hash if from main)."
      placeholder: "e.g., 1.2.0 / abc1234"
    validations:
      required: true

  - type: input
    id: python-version
    attributes:
      label: Python Version
      description: "The Python version installed on your system."
      placeholder: "e.g., 3.11.4"
    validations:
      required: true

  - type: textarea
    id: os
    attributes:
      label: Operating System & Version
      description: "Specify your OS and its version (e.g., Ubuntu 22.04, macOS Ventura 13.5, Windows 11).
      placeholder: "e.g., macOS Ventura 13.5 (Apple M1 Pro)"
    validations:
      required: true

  - type: textarea
    id: dependencies
    attributes:
      label: Key Dependencies (if applicable)
      description: "List any specific versions of major libraries you are using, especially if they deviate from the standard toolkit dependencies."
      placeholder: "e.g., pandas==2.0.3, numpy==1.25.1"
    validations:
      required: false

  - type: markdown
    attributes:
      value: | 
        --- 

        ## 2. Bug Description
        Provide a detailed explanation of the bug.

  - type: textarea
    id: description
    attributes:
      label: Describe the bug
      description: "What is the unexpected behavior? What did you expect to happen?"
      placeholder: "A clear and concise description of the bug."
    validations:
      required: true

  - type: textarea
    id: steps_to_reproduce
    attributes:
      label: Steps to Reproduce
      description: "Provide step-by-step instructions to reproduce the bug. Be as detailed as possible."
      placeholder: "1. Run command `python toolkit.py process --data input.csv`\n2. Observe error message..."
    validations:
      required: true

  - type: textarea
    id: expected_behavior
    attributes:
      label: Expected Behavior
      description: "What did you expect to happen?"
      placeholder: "The command should complete successfully and output results to output.txt."
    validations:
      required: true

  - type: textarea
    id: actual_behavior
    attributes:
      label: Actual Behavior
      description: "What actually happened? Include any error messages or logs."
      placeholder: "The command failed with a `KeyError: 'column_name'`.
Traceback:
python
...error traceback...
"
    validations:
      required: true

  - type: markdown
    attributes:
      value: | 
        --- 

        ## 3. Additional Information
        Any other context about the problem.

  - type: textarea
    id: additional_context
    attributes:
      label: Additional Context
      description: "Screenshots, logs, relevant configurations, or any other context about the problem. You can attach screenshots by dragging and dropping them."
      placeholder: "e.g., This bug only occurs when processing large datasets..."
    validations:
      required: false

  - type: markdown
    attributes:
      value: | 
        --- 

        Thank you for helping improve the **Academic Data Science Automation Toolkit**!
