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

### Code and Data
- Model implementation
    - [DL4H_project.ipynb](https://github.com/yixingz3/DL4H_team_project/blob/main/DL4H_project.ipynb)
          - Our implementation of the proposed and baseline models
- Data set
    - [IMDB dataset](https://github.com/yixingz3/DL4H_team_project/blob/main/aclImdb_v1.tar.gz)
- Data processing
    - [mergeData.py](https://github.com/yixingz3/DL4H_team_project/blob/main/mergeData.py)
          - Failed attempt to extract symptoms from MIMIC-III data set

### ML Code Completeness Checklist
- Data download/uss instruction
    - The data set can be accessed and downloaded from the repo [IMDB dataset](https://github.com/yixingz3/DL4H_team_project/blob/main/aclImdb_v1.tar.gz)
- Specification of dependencies
    - Need to move the extracted dataset from above into your Google Drive under directory "/content/drive/MyDrive/aclImdb"
    - Environment is setup with Google Colab
          - no need any other specific dependency
          - just run through code blocks in sequential order
- Training Code
    - Included in the [model implementation](https://github.com/yixingz3/DL4H_team_project/blob/main/DL4H_project.ipynb) file
- Evaluation code
    - Included in the [model implementation](https://github.com/yixingz3/DL4H_team_project/blob/main/DL4H_project.ipynb) file
- Pre-trained models
    - Not included
- README file including table of results accompanied by precise commands to run/produce those results
    - The result of each model is also included in the [model implementation](https://github.com/yixingz3/DL4H_team_project/blob/main/DL4H_project.ipynb) file
    - To execute the script, open file with Google Colab and execute the code blocks sequentially from the top to the bottom
- Table of Results

| Model            | Loss   | Train Acc | Test Acc | Runtime  |
|------------------|--------|-----------|----------|----------|
| TF-IDF + Bi-LSTM | 0.0738 | 0.9108    | 0.8345   | ~10 Mins |
| Glove + Bi-LSTM  | 0.1836 | 0.6814    | 0.6776   | ~10 Mins |
| WordVec+ Bi-LSTM | 0.1528 | 0.7929    | 0.8042   | ~10 Mins |
| Embedding        | 0.1429 | 0.8331    | 0.7682   | ~10 Mins |



