# Mermaid Magic

An IPython magic extension for rendering Mermaid diagrams in notebooks, including Databricks, Jupyter, VS Code and Cursor

<a href="https://github.com/vbalasu/mermaid-magic/releases/download/assets/mermaid-in-notebooks.html" download class="button-link">Download Databricks Notebook</a>


## Installation

```bash
pip install mermaid-magic
```

## Usage

1. Load the extension in your Jupyter notebook:

```python
%load_ext mermaid_magic
```

2. Use the `%%mermaid` cell magic to create diagrams:

```python
%%mermaid
graph TD;
    A[Start] --> B{Is it working?};
    B -- Yes --> C[Great!];
    B -- No --> D[Fix it];
    D --> B;
```

![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/01.mmd.png)

## Features

- Renders Mermaid diagrams directly in Jupyter notebooks
- Automatically loads the Mermaid.js library when needed
- Supports all Mermaid diagram types (flowcharts, sequence diagrams, etc.)

Create mermaid diagrams in:
- Jupyter Lab and Jupyter notebooks (classic)
- Databricks Notebooks
- Notebooks (.ipynb) in VS Code
- Notebooks (.ipynb) in Cursor

# Using Mermaid Diagrams in Databricks
This notebook demonstrates how to create Mermaid diagrams in Databricks notebooks. Also works in Jupyter, VS Code, Cursor and other notebook environments


```python
%pip install -qqq mermaid-magic
```

    Note: you may need to restart the kernel to use updated packages.



```python
%load_ext mermaid_magic
```

## Basic Flowchart Example


```python
%%mermaid
graph TD
    A[Start] --> B{Is it working?}
    B -->|Yes| C[Great!]
    B -->|No| D[Debug]
    D --> B
```


![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/02.mmd.png)





## Data Pipeline Example
Let's create a more complex diagram showing a typical data pipeline in Databricks


```python
%%mermaid
graph TD
    A[Data Ingestion] --> B[Data Processing]
    B --> C{Quality Check}
    C -->|Pass| D[Feature Engineering]
    C -->|Fail| E[Error Handling]
    D --> F[Model Training]
    F --> G[Model Evaluation]
    G -->|Metrics Meet Threshold| H[Model Deployment]
    G -->|Metrics Below Threshold| F
    E --> A
```



![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/03.mmd.png)





## Sequence Diagram Example
Sequence diagrams are useful for showing the interaction between different components


```python
%%mermaid
sequenceDiagram
    participant User
    participant Databricks
    participant DataLake
    participant ML
    
    User->>Databricks: Execute notebook
    Databricks->>DataLake: Query data
    DataLake-->>Databricks: Return dataset
    Databricks->>ML: Train model
    ML-->>Databricks: Return model
    Databricks-->>User: Display results
```



![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/04.mmd.png)




## Class Diagram
Class diagrams can be useful for showing the structure of your code


```python
%%mermaid
classDiagram
    class DataProcessor {
        +DataFrame data
        +process_data()
        +validate_schema()
    }
    
    class FeatureEngineering {
        +create_features()
        +scale_features()
    }
    
    class ModelTrainer {
        +train()
        +evaluate()
        +save_model()
    }
    
    DataProcessor --> FeatureEngineering
    FeatureEngineering --> ModelTrainer
```



![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/05.mmd.png)




## Entity Relationship Diagram
ER diagrams are useful for database schema visualization


```python
%%mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|--|{ DELIVERY-ADDRESS : uses
```



![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/06.mmd.png)





## Gantt Chart
Gantt charts are useful for project planning and scheduling


```python
%%mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Planning
    Requirements gathering :a1, 2023-01-01, 10d
    Design phase           :a2, after a1, 15d
    section Development
    Coding                 :a3, after a2, 25d
    Testing                :a4, after a3, 10d
    section Deployment
    Deployment preparation :a5, after a4, 5d
    Go-live                :milestone, after a5, 0d
```



![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/07.mmd.png)





## State Diagram
State diagrams are useful for showing the different states of a process or system


```python
%%mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: New data
    Processing --> Completed: Successful
    Processing --> Failed: Error
    Completed --> [*]
    Failed --> Idle: Retry
```



![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/08.mmd.png)




## Pie Chart


```python
%%mermaid
pie title Programming Languages
    "Python" : 40
    "SQL" : 30
    "Scala" : 20
    "R" : 10
```



![](https://raw.githubusercontent.com/vbalasu/mermaid-magic/main/media/09.mmd.png)




## Conclusion
These examples show various ways to create Mermaid diagrams in Databricks. You can use these techniques to:

- Visualize data processes
- Document workflows
- Create architecture diagrams
- Plan project timelines

For more information on Mermaid syntax, visit [the Mermaid documentation](https://mermaid-js.github.io/mermaid/#/).
