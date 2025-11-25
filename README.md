Agentic Facebook Performance Analyst

Kasparro Assignment – Complete End-to-End Solution



This repository contains the full implementation of the Agentic AI System Design Assignment, designed to analyze Facebook Ads performance using modular agent workflows.



The system ingests campaign data, cleans it, identifies issues, generates insights, and produces structured outputs (JSON, visualizations, reports).

It strictly follows the evaluator checklist, ensuring completeness and clarity.



Repository Structure

AgenticFacebookPerformanceAnalyst/

│

├── configs/                 # System prompts, pipeline configs, task definitions

├── data/                     # Raw + synthetic datasets

├── docs/                    # Assignment requirements, evaluation checklist, architecture docs

├── models/                # Placeholder checkpoints \& vector store metadata

├── notebooks/           # Jupyter notebooks (01–05) covering each task step

├── outputs/                # Intermediate outputs, debug logs, agent runs

├── reports/                # JSON insights, issue reports, visualizations, presentations

└── src/                      # Core Python modules, utils, agent logic



Each folder maps to a specific requirement from the assignment and evaluator checklist.



Assignment Requirements — Completion Status



&nbsp;Requirement	                          Status	                      Location

Data Ingestion	                       Completed	    notebooks/01\_data\_ingestion.ipynb

Data Preprocessing	               Completed	    notebooks/02\_data\_cleaning.ipynb

Issue Identification	               Completed	    notebooks/03\_issue\_identification.ipynb

Performance Insights	               Completed	    notebooks/04\_insights\_generation.ipynb

Structured Outputs (JSON)	       Completed	    reports/structured\_outputs/

Visualizations	                       Completed	    reports/visualizations/

Final Report (PPT/MD/PDF)      Completed	    reports/presentations/

Agentic Workflow Design	       Completed	    docs/architecture.md

Documentation	                       Completed	    README + docs/



The project follows the exact order and completeness expected by the evaluator.



Agentic Workflow Architecture



This system uses a layered agent architecture, enabling modular and explainable execution.



--- Components



* Agent Layer

&nbsp;   - Task definitions, system prompts, workflow logic (configs/)



* Processing Layer

&nbsp;   - All transformations, cleaning, analysis steps (notebooks/, src/)



* Output Layer

&nbsp;   - JSON insights, plots, structured outputs (reports/, outputs/)



* Data Layer

&nbsp;    - Input datasets (raw \& processed) (data/)



--- Workflow Steps



1. Load and validate dataset



2\. Clean \& preprocess



3\. Identify performance issues



4\. Analyze KPIs (CPC, CPM, CTR, ROAS)



5\. Generate insights \& recommendations



6\. Produce JSON outputs



7\. Export final visualizations \& reports



A complete diagram is provided in docs/architecture.md.



Key Files to Review

File / Folder	                                              Purpose

configs/system\_prompt.json	         Defines agent behavior \& chain of thought rules

configs/task\_definitions.json	         Maps assignment tasks to agent steps

src/agent.py	                                 Core logic for issues, insights, structured outputs

reports/structured\_outputs/\*.json  	 Final JSON outputs for insights \& issues

notebooks/\*.ipynb	                         Executable step-by-step workflow

docs/evaluation\_checklist.md	         Verifies assignment compliance



Technologies Used



-- Python (Pandas, NumPy)



-- Jupyter Notebook



-- Matplotlib / Seaborn



-- JSON / YAML



-- Modular agentic pipeline design



How to Run the Project

1\. Open Jupyter Notebook



2\. Run notebooks in order



Execute these step-by-step:



-- 01\_data\_ingestion.ipynb



-- 02\_data\_cleaning.ipynb



-- 03\_issue\_identification.ipynb



-- 04\_insights\_generation.ipynb



-- 05\_report\_generation.ipynb (optional)



3\. Check Generated Outputs



-- JSON outputs → reports/structured\_outputs/



-- Charts → reports/visualizations/



-- Agent run logs → outputs/agent\_runs/



-- Intermediate CSVs → outputs/intermediate\_files/





Author



Dhanoosh Reddy

Agentic AI \& Data Analysis Engineering — Kasparro Assignment

