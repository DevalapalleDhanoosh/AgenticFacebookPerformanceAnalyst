Agentic Facebook Performance Analyst – Kasparro Assignment

1\. Overview



This repository contains a modular, production-style implementation of the Kasparro Applied AI Engineer Assignment.

The system analyzes Facebook Ads performance using a structured, agentic pipeline and produces:



insights.json (key performance insights)



creatives.json (creative recommendations)



report.md (final combined analyst report)



The solution follows a clean separation of layers—config, data, processing, pipelines, outputs—and fully meets the evaluator checklist.



2\. Project Folder Structure

AgenticFacebookPerformanceAnalyst/

│

├── configs/                      # System prompts \& task configs

│       evaluation\_criteria.json

│       pipeline\_config.yaml

│       prompt\_templates.txt

│       system\_prompt.json

│       task\_definitions.json

│

├── data/                         # Input dataset

│       synthetic\_fb\_ads\_undergarments.csv

│

├── docs/                         # Architecture, requirements \& logs

│       architecture.md

│       assignment\_requirements.md

│       evaluation\_checklist.md

│       project\_log.md

│

├── models/                       # Placeholder model space

│       checkpoints/

│       vector\_store/

│

├── notebooks/                    # Optional development notebooks

│       01\_data\_ingestion.ipynb

│       02\_data\_cleaning.ipynb

│       03\_issue\_identification.ipynb

│       04\_insights\_generation.ipynb

│       05\_report\_generation.ipynb

│

├── outputs/

│   ├── agent\_runs/               # Example agent run traces

│   ├── debug\_logs/               # Logs for debugging

│   ├── intermediate\_files/       # Cleaned + processed CSV files

│   │       cleaned\_data.csv

│   │       raw\_ingested\_data.csv

│   └── final/                    # \*\*\*Required Assignment Outputs\*\*\*

│           insights.json

│           creatives.json

│           report.md

│

├── reports/

│   ├── structured\_outputs/       # Additional JSON outputs

│   ├── visualizations/           # Charts \& KPIs

│       ctr\_trend.png

│       cpm\_trend.png

│       country\_roas.png

│   ├── logs/

│   └── presentations/            # Exported report documents

│       final\_report.md

│

└── src/

&nbsp;   ├── agent.py                  # Agentic workflow utilities

&nbsp;   ├── analysis\_utils.py

&nbsp;   ├── data\_cleaning.py

&nbsp;   ├── data\_loader.py

&nbsp;   └── pipelines/                # \*\*\*Core Pipeline Scripts\*\*\*

&nbsp;           generate\_insights.py

&nbsp;           generate\_creatives.py

&nbsp;           generate\_report.py



3\. Pipeline Architecture



The agentic workflow is implemented as a three-stage pipeline:



Stage 1 — Insights Generation (generate\_insights.py)



Loads dataset



Computes descriptive statistics



Uses an offline LLM-style generator to produce structured insights



Writes outputs/final/insights.json



Stage 2 — Creative Recommendations (generate\_creatives.py)



Reads insights



Produces recommended ad copies, image ideas, video hooks



Saves to outputs/final/creatives.json



Stage 3 — Final Report Generation (generate\_report.py)



Combines insights + creative recommendations



Produces a polished markdown report



Saves to outputs/final/report.md



4\. Setup Instructions

Prerequisites



Python 3.10+



Git installed



No API key required (offline pipeline)



Install dependencies

pip install -r requirements.txt



5\. How to Run the Pipeline

1️⃣ Generate insights

python src/pipelines/generate\_insights.py





Output → outputs/final/insights.json



2️⃣ Generate creative recommendations

python src/pipelines/generate\_creatives.py





Output → outputs/final/creatives.json



3️⃣ Generate final report

python src/pipelines/generate\_report.py





Output → outputs/final/report.md



6\. Assignment Outputs



Your final mandatory files are located at:



outputs/final/insights.json

outputs/final/creatives.json

outputs/final/report.md





These files satisfy the official Kasparro deliverables:



~ insights.json



~ creatives.json



~ report.md



~ clean modular code



~ agentic pipeline architecture



7\. Versioning \& Release (as required)



Create release tag:



v1.0





GitHub → Releases → New Release → Tag v1.0



Include release notes:



Kasparro Agentic Facebook Analyst – v1.0

Contains insights.json, creatives.json, report.md, modular pipeline, and documentation.



8\. Compliance with Evaluation Checklist



This project meets the evaluator requirements:



Requirement	                         Status

Data ingestion	                         ✔ Completed

Cleaning \& preprocessing	         ✔ Completed

Issue identification	                 ✔ Implemented

KPI analysis	                         ✔ Implemented

Agentic pipeline	                         ✔ Modular

Structured outputs	                 ✔ insights.json / creatives.json / report.md

Documentation	                         ✔ README + docs

Reproducibility	                         ✔ Fully runnable

Extra (not required but included)	Visualizations, intermediate files, logs





9\. Author



Dhanoosh Reddy

Applied AI Engineer – Kasparro Assignment

