from taipy.gui import Gui, notify
import pandas as pd
import os

DOWNLOAD_PATH = "data/download.csv"
upload_file = None
FIXED_ROW_COUNT = 7  # Number of rows to display in the table
REPLACEMENT_VALUE = '-'  # Value to replace NaN with

page_1 = """
<|navbar|>
<|container|
#Entire Process

<center>
<|navbar|lov={[("page1", "This Page"), ("https://taipy.io", "Reference"), ("https://docs.taipy.io/en/latest/getting_started/", "Video")]}|>
</center>
-----------------------------------------------------------------------------------------------

<|{logo_entire_process2}|image|height=700px|width=100%|>

<|layout|columns= 1 1 |
<|
<|card|
###Safety and Storage Conditions
Ammonia is highly toxic and requires careful handling. The storage facility design follows safety regulations and guidelines, with a focus on low-temperature storage. 
The chosen capacity is 25,500 tons of ammonia stored at -33.4°C to ensure safety and efficiency.
|>
|>


<|
<|card
###Cooling of Vaporized Ammonia: For effective cooling

ammonia is used as the refrigerant in a Carnot cycle to condense vaporized ammonia at a rate of 25.5 tons/day.
|>
|>
|>

#### Thermodynamic Equation Selection
##### **Selected Model: SRKM**


#### **Why SRKM Was Chosen**
The SRKM (Sengupta-Raj-Carrier-Kumar) model was selected due to its high accuracy in predicting the behavior of the ammonia-water system. It aligns closely with experimental solubility data and handles the complex interactions between polar and non-polar substances effectively.

- **Strengths of SRKM**:
  - **Precision**: Matches experimental solubility data closely.
  - **Complex Interaction Modeling**: Capable of handling the mixture's intricate interactions.
  - **Performance**: Proven reliability in various thermodynamic scenarios.

> **Note:** The SRKM model was chosen for its accuracy.

-------------------------------------------------------------------------------
<|Thermodynamic Equation Selection|expandable|expanded=False|partial={partial_A}|>


---

### **Evaluation Methods**

#### **1. Pro/II Thermodynamic Equation Application**
We evaluated various thermodynamic equations using Pro/II simulation software. This assessment involved:

- **Applicability**: Determining how each equation performs in modeling the system.
- **Performance Metrics**: Comparing the outcomes of each model with expected results.

**Key Insights:**

- **NRTL/UNIQUAC**: Effective for general non-ideal systems.
- **SRKM**: Provided the best fit for our specific system.

#### **2. Equilibrium Data Analysis**
Analyzed phase equilibrium data (xy diagrams) to validate the thermodynamic models:

- **Method**: Compared model predictions with phase equilibrium data for ammonia-water systems.
- **Outcome**: Identified models that accurately predicted system behavior.

**Results:**

- **SRKM**: Accurately reflects phase equilibrium data.
- **UNIWAALS**: Showed significant deviations from experimental observations.

#### **3. Absorption Tower Solubility Experiments**
Conducted experiments using absorption towers to test solubility predictions:

- **Setup**: Implemented a 10-stage absorption tower for empirical testing.
- **Validation**: Compared experimental solubility data with predictions from various models.

**Findings:**

- **SRKM**: Delivered accurate solubility predictions.
- **Other Models**: Showed varying degrees of deviation from experimental data.

---

### **Visual Aids**

<|layout|columns= 1 1 1 |
<|
<|{cat}|image|height=300px|width=300px|>

- **Peng Robinson EOS**
- **Dew point 50.1**
|>
<|
<|{cat}|image|height=300px|width=300px|>

- **Vapor Pressure mode**- 
- **Dew point 54.3 C**
- **Good predictions at low pressures Binary Plot**
|>
<|
<|{cat}|image|height=300px|width=300px|>

- **NRTL Ideal**
|>
|>

---

#### **Thermodynamic Models Overview**
- **Diagram**: Visual overview of different thermodynamic equations and their applicability.
- **Details**: Explanation of why each model is suitable or unsuitable.

#### **Phase Equilibrium Data**
- **Graphs**: xy diagrams comparing model predictions with actual data.
- **Analysis**: Evaluation of model performance based on equilibrium data.

#### **Absorption Tower Experiment**
- **Diagram**: Illustration of the absorption tower experimental setup.
- **Summary**: Key results and implications of the solubility experiments.
  - **Test**: Text test check

---

### **Interactive Demo**

Explore our interactive demo to visualize the models and their practical applications:

[**Interactive Demo - Explore Thermodynamic Models**](https://taipy.io)

[**이미지 열기**](/static/cat.png)

[**page3 open**](#page_3)

---

### **Additional Resources**

- **Technical Papers**: Access detailed studies on SRKM and other thermodynamic models.
- **FAQs**: Answers to common questions about thermodynamic modeling.
- **Contact Us**: For more detailed inquiries or support, reach out to our team.

|>
"""

page_2="""
<|navbar|>
<|container|
<|
## Ammonia Liquefaction Process ##
|>

<|
<center>
<|{logo_1}|image|class_name=image-style|height=255px|width=100%|on_action={lambda s: s.assign("show_pane1", True)}|>
<|{logo_2}|image|class_name=image-style|height=255px|width=100%|on_action={lambda s: s.assign("show_dialogam2", True)}|>
</center>
<center>
<|{logo_3}|image|class_name=image-style|height=255px|width=100%|on_action={lambda s: s.assign("show_dialogam3", True)}|>
<|{logo_4}|image|class_name=image-style|height=255px|width=100%|on_action={lambda s: s.assign("show_dialogam4", True)}|>
</center>

<style>
.image-style {
    width: 595px; 
}
</style>

<|{show_pane1}|pane|width=70%|partial={partial_B}|>
<|{show_dialogam2}|dialog|width=60%|height=80%|partial={partial_C}|on_action={close_dialogam2}|>
<|{show_dialogam3}|dialog|width=60%|height=80%|partial={partial_D}|on_action={close_dialogam3}|>
<|{show_dialogam4}|dialog|width=60%|height=80%|partial={partial_E}|on_action={close_dialogam4}|>

<|Input vs Conversion|expandable|expanded=False|
## Data Visualization
<|{dataset1}|chart|mode=line|x=Input|y=conversion|>
|>
|>
|>

"""


page_3 = """
<|navbar|>
<|container|

<|layout|columns= 3 2 |
<|
<video width="700" height="500" controls>
  <source src="static/amvideo.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
|>


<|
#### **Phase Equilibrium Data**
- **Graphs**: xy diagrams comparing model predictions with actual data.
- **Analysis**: Evaluation of model performance based on equilibrium data.

<|Thermodynamic Equation Selection|expandable|expanded=True|
### **Additional Resources**
<center>
<|{cat}|image|height=200px|width=180px|>
</center>
|>


|>
|>



#### **Thermodynamic Models Overview**
- **Diagram**: Visual overview of different thermodynamic equations and their applicability.
- **Details**: Explanation of why each model is suitable or unsuitable.

#### **Phase Equilibrium Data**
- **Graphs**: xy diagrams comparing model predictions with actual data.
- **Analysis**: Evaluation of model performance based on equilibrium data.

#### **Absorption Tower Experiment**
- **Diagram**: Illustration of the absorption tower experimental setup.
- **Summary**: Key results and implications of the solubility experiments.



|>

"""


page_4 = """
<|navbar|>
<|container|

#Distillation Process
<|
<|{logo_distillation_column}|image|height=600px|width=100%|>
|>

<|
<center>
<|S8_1|button|class_name=button-style|on_action={lambda s: s.assign("show_dialogs8_1", True)}|>
<|S18_1|button|class_name=button-style|on_action={lambda s: s.assign("show_dialogs18_1", True)}|>
<|S17_1|button|class_name=button-style|on_action={lambda s: s.assign("show_dialogs17_1", True)}|>
<|S35|button|class_name=button-style|on_action={lambda s: s.assign("show_dialogs35", True)}|>
<|S36|button|class_name=button-style|on_action={lambda s: s.assign("show_dialogs36", True)}|>
</center>
|>

<style>
.button-style {
    margin-left: 25px;
    margin-right: 25px;
    font-size: 15px;
    width: 65px;
}
</style>


<|{show_dialogs8_1}|dialog|width=60%|height=80%|partial={partial_S8_1}|on_action={close_dialogs8_1}|>
<|{show_dialogs18_1}|dialog|width=60%|height=80%|partial={partial_S18_1}|on_action={close_dialogs18_1}|>
<|{show_dialogs17_1}|dialog|width=60%|height=80%|partial={partial_S17_1}|on_action={close_dialogs17_1}|>
<|{show_dialogs35}|dialog|width=60%|height=80%|partial={partial_S35}|on_action={close_dialogs35}|>
<|{show_dialogs36}|dialog|width=60%|height=80%|partial={partial_S36}|on_action={close_dialogs36}|>


<|layout|columns= 6 5 |
<|
## Table
<|{datasetdistill1}|table|page_size=15|height=500px|width=99%|>
|>
<|
## Data Visualization
<|{datasetdistill}|chart|mode=lines|x=R(reflux)|y=total trays|height=550px|width=99%|>
|>
|>


|>
"""

page_5 = """
<|navbar|>
<|container|


<|
#Table
<|{datasetmoney1}|table|page_size=15|height=500px|width=99%|class_name=table-container|>
|>

<style>
/* Highlight the 3 row */
.table-container tr:nth-child(2) {
    background-color: #ADD8E6 !important; 
}
</style>

<|layout|columns= 1 1 |
<|
## Chart1
<|{datasetmoney1}|chart|mode=line|x=운전압력(최상단 압력,kPa)|y=가격 총합|>
|>

<|
## Chart2
<|{datasetmoney}|chart|mode=line|x=운전압력(최상단 압력,kPa)|y=가격 총합|color=red|>
|>
|>


<|layout|columns=1 6|
<|
## Custom Parameters
**운전압력 및 흡수탑 단수**\n\n<|{combined_value}|selector|lov={combined_lov}|dropdown|on_change=combined_onchange|>
<br/><br/>
<center>
<|button|label=GO|on_action=button_action|>
<|button|label=Reset|on_action=reset_action|>
</center>
|>
<|
<center>
    <h2>Dataset</h2><|{DOWNLOAD_PATH}|file_download|on_action=download|>
    <|{datasetmoney}|table|page_size={FIXED_ROW_COUNT}|height=500px|width=95%|>
</center>
|>
|>
|>

<style>
.chart-container svg path:nth-of-type(6) {
    stroke: #FF4500; /* Orange color */
    stroke-width: 3px;
}
</style>
"""
page_6 = """
<|navbar|>

# Entire Process

## Safety and Storage Conditions
### Cooling of Vaporized Ammonia: For effective cooling
#### Thermodynamic Equation Selection
##### **Selected Model: SRKM**
---
<u>밑줄 텍스트</u>
---
<b>굵은 글씨</b>
굵은 글씨
----

<i>기울임 글씨</i>
---




"""

A = """
###The simulation software used is AVEVA Pro/II.
WILSON: Recommended for single liquid phases with mild non-idealities.

NRTL/UNIQUAC: Applicable to all non-ideal systems.

SRKS/SRKM/PRM/UNIWAALS: Applicable to all non-ideal systems.

HOCV: Suitable for systems containing dimers.

HEXAMER:  Suitable for systems containing hexamers
"""
B = """
##E5 process
###Heat Exchanger
_______________________
<|{dataset2}|table|page_size=15|height=500px|width=99%|>
"""
C = """
##C2 process
###Compressor
_______________________
<|{dataset3}|table|page_size=15|height=500px|width=99%|>
"""
D = """
##V3 process
###Valve
_______________________
<|{dataset4}|table|page_size=15|height=500px|width=99%|>
"""
E = """
##E4 process
###Heat Exchanger
_______________________
<|{dataset5}|table|page_size=15|height=500px|width=99%|>
"""

S8_1 = """
##S8_1 
_______________________
<|{datasets8_1}|table|page_size=15|height=500px|width=99%|>

"""
S18_1 = """
##S18_1 
_______________________
<|{datasets18_1}|table|page_size=15|height=500px|width=99%|>

"""
S17_1 = """
##S17_1 
_______________________
<|{datasets17_1}|table|page_size=15|height=500px|width=99%|>

"""
S35 = """
##S35 
_______________________
<|{datasets35}|table|page_size=15|height=500px|width=99%|>

"""
S36 = """
##S36 
_______________________
<|{datasets36}|table|page_size=15|height=500px|width=99%|>

"""



pages = {
    "Intro": page_1,
    "NH3_Storage": page_2,
    "NH3_Decomposition": page_3,
    "Distillation": page_4,
    "Economice_Analysis": page_5,
    "Test": page_6
}

show_pane1 = False
show_pane2 = False
show_dialogam2 = False  
show_dialogam3 = False  
show_dialogam4 = False
show_dialogs8_1 = False
show_dialogs18_1 = False
show_dialogs17_1 = False
show_dialogs35 = False
show_dialogs36 = False

amvideo = "static/amvideo.mp4"
cat = "static/cat.png"
logo_distillation_column = "static/distillation_column.png"
logo_entire_process2 = "static/entire_process2.png"
logo_1 = "static/am1.png"
logo_2 = "static/am2.png"
logo_3 = "static/am3.png"
logo_4 = "static/am4.png"

# data visualization
def get_data(path: str):
    return pd.read_csv(path)

dataset1 = get_data("data/conversion.csv")
dataset2 = get_data("data/E5.csv")
dataset3 = get_data("data/C2.csv")
dataset4 = get_data("data/V3.csv")
dataset5 = get_data("data/E4.csv")

datasets8_1 = get_data("data/S8_1.csv")
datasets18_1 = get_data("data/S18_1.csv")
datasets17_1 = get_data("data/S17_1.csv")
datasets35 = get_data("data/S35.csv")
datasets36 = get_data("data/S36.csv")

datasetdistill = get_data("data/distill_data.csv")
datasetdistill1 = get_data("data/distill_data1.csv")
datasetmoney1 = get_data("data/money1.csv")
datasetmoney = get_data("data/money.csv")

datasetmoney1["가격 총합"] = datasetmoney1["가격 총합"].apply(lambda x: f"{x:.5e}")




# 데이터셋을 파일로 저장 (옵션)
datasetmoney.to_csv("data/money_with_highlight.csv", index=False)


# Extract unique combined values for dropdown
combined_values = datasetmoney[['운전압력(최상단 압력,kPa)', '흡수탑 단수']].drop_duplicates()
combined_lov = [{"label": f"{row['운전압력(최상단 압력,kPa)']}, {row['흡수탑 단수']}", "value": f"{row['운전압력(최상단 압력,kPa)']},{row['흡수탑 단수']}"} for idx, row in combined_values.iterrows()]

pressure = None
tray_number = None
combined_value = None  # Initialize combined_value


#page5 
def get_data(path: str):
    dataset = pd.read_csv(path)
    return dataset

def combined_onchange(state, var_name, value):
    if value:
        # Extract the pressure and tray number from the dictionary
        pressure, tray_number = value['value'].split(',')
        state.pressure = float(pressure)
        state.tray_number = float(tray_number)
    else:
        state.pressure = None
        state.tray_number = None


def filter_by_parameters(dataset, pressure, tray_number):
    mask = (dataset['운전압력(최상단 압력,kPa)'] == pressure) & (dataset['흡수탑 단수'] == tray_number)
    return dataset.loc[mask]

def adjust_row_count(dataframe):
    """ Adjust the row count to ensure a fixed number of rows in the table, replacing NaN values. """
    num_rows = len(dataframe)
    if num_rows < FIXED_ROW_COUNT:
        # Add empty rows
        empty_rows = pd.DataFrame(index=range(FIXED_ROW_COUNT - num_rows))
        for col in dataframe.columns:
            empty_rows[col] = REPLACEMENT_VALUE
        dataframe = pd.concat([dataframe, empty_rows], ignore_index=True)
    
    # Replace NaN values in the dataframe with REPLACEMENT_VALUE
    dataframe.fillna(REPLACEMENT_VALUE, inplace=True)
    
    return dataframe

def button_action(state):
    if state.pressure is not None and state.tray_number is not None:
        state.datasetmoney = filter_by_parameters(datasetmoney, state.pressure, state.tray_number)
        state.datasetmoney = adjust_row_count(state.datasetmoney)
        notify(state, "info", f"Filtered dataset for pressure: {state.pressure} and tray number: {state.tray_number}")

def reset_action(state):
    state.datasetmoney = datasetmoney.copy()  # Reset to initial dataset
    state.datasetmoney = adjust_row_count(state.datasetmoney)
    state.pressure = None
    state.tray_number = None
    notify(state, "info", "Reset to initial dataset")

def download(state):
    state.datasetmoney.to_csv(DOWNLOAD_PATH)

#page5 

def close_dialogam2(state):
    state.assign("show_dialogam2", False)

def close_dialogam3(state):
    state.assign("show_dialogam3", False)

def close_dialogam4(state):
    state.assign("show_dialogam4", False)

def close_dialogs8_1(state):
    state.assign("show_dialogs8_1", False)

def close_dialogs18_1(state):
    state.assign("show_dialogs18_1", False)

def close_dialogs17_1(state):
    state.assign("show_dialogs17_1", False)

def close_dialogs35(state):
    state.assign("show_dialogs35", False)

def close_dialogs36(state):
    state.assign("show_dialogs36", False)

gui = Gui(pages=pages)
partial_A = gui.add_partial(A)
partial_B = gui.add_partial(B)
partial_C = gui.add_partial(C)
partial_D = gui.add_partial(D)
partial_E = gui.add_partial(E)
partial_S8_1 = gui.add_partial(S8_1)
partial_S18_1 = gui.add_partial(S18_1)
partial_S17_1 = gui.add_partial(S17_1)
partial_S36 = gui.add_partial(S36)
partial_S35 = gui.add_partial(S35)

stylekit = {
  "color_primary": "#FF462B",  
  "color_secondary": "#C0FFE",  # 기존 보조 색상
}


if __name__ == '__main__':
    # the options in the gui.run() are optional, try without them
    gui.run(title='About Process',
    		host='0.0.0.0',
    		port=os.environ.get('PORT', '5007'),
    		dark_mode=False,
            stylekit=stylekit,
            )
else:
    app = gui.run(title='About Process',
                  dark_mode=False,
                  run_server=False,
                  stylekit=stylekit,
                  )

#저장시간 2024/8/4 14:00
