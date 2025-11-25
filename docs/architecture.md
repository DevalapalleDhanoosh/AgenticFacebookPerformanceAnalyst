# Agentic Workflow Architecture

## 1. Overview
This project uses an agentic architecture to analyze Facebook Ads performance and generate insights.

## 2. Components
- **Data Layer**: Raw + processed data from `/data`
- **Agent Layer**: Prompts and system definitions in `/configs`
- **Processing Layer**: Notebooks performing each assignment step
- **Output Layer**: Reports, visuals, JSON outputs in `/reports`

## 3. Workflow
1. Load data
2. Clean & preprocess
3. Identify performance issues
4. Analyze metrics (CPC, CPM, ROAS)
5. Generate insights + recommendations
6. Export structured outputs
7. Prepare final report

## 4. Tools Used
- Jupyter Notebook
- Pandas, NumPy
- JSON, YAML for configs
