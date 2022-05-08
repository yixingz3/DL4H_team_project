# DL4H Team Project Spring 2022

### Team 64
- Zerui Tian (zeruit2@illinois.edu)
- Yixing Zheng (yixingz3@illinois.edu)

### Paper ID 79
- Disease Inference with Symptom Extraction and Bidirectional Recurrent Neural Network

### Draft Submission
- Our implementation of the TF-IDF + Bi-LSTM model
- trained and evaluated with the IMDb data set as we haven't been able to obtained the original data set
  - We have contacted the original authors of the paper to request the original data set, but haven't received any responses yet
- Please refer to our [draft report](https://github.com/yixingz3/DL4H_team_project/blob/main/CS598DL4H_project_template_2022Spring_team64.pdf) for more detials 

### Final Submission
- [final report](To be completed)

### IMDB dataset
- To be completed - add instruction on how to mount this data to the script and utilize it with Colab

### Repo structure
- [mergeData.py](https://github.com/yixingz3/DL4H_team_project/blob/main/mergeData.py)
    - Failed attempt to extract symptoms from MIMIC-III data set
- [TF-IDF+Bi-LSTM.ipynb](https://github.com/yixingz3/DL4H_team_project/blob/main/TF-IDF%2BBi-LSTM.ipynb)
    - Our implementation of the proposed model
- Glove+Bi-LSTM.ipynb
    - Our implementation of the baseline models - Glove + Bi-LSTM
- WordVec+Bi-LSTM.ipynb
    - Our implementation of the baseline models WordVec + Bi-LSTM
- Embedding.ipynb
    - Our implementation of the baseline models - Embedding

### ML Code Completeness Checklist
- Specification of dependencies
    - Need to move the dataset into Google Drive
    - Environment is setup with Google Colab - no need any other specific dependency
    - TODO - add more instructions
- Data download/uss instruction
    - The dataset can be accessed and downloaded in this [google drive with @illinois credentials](https://drive.google.com/drive/folders/1_p4CNHAMX1lt7tltUyxu0U6N3rptSqK8?usp=sharing)
- Training Code
    - Included in the model specific .ipynb file
- Evaluation code
    - Included in the model specific .ipynb file
- Pre-trained models
    - Not included
    - TODO - check if we have it
- README file including table of results accompanied by precise commands to run/produce those results
    - The result of each model is included in the model specific .ipynb file
    - To execute the script, open file with Google Colab and execute the code blocks sequentially from the top to the bottom
- Table of Results
    - TODO



