<div align= "center">
    <h1> 🛠️ToolBench🤖</h1>
</div>

<div align="center">

![Dialogues](https://img.shields.io/badge/Tool\_Num-3451-red?style=flat-square)
![Dialogues](https://img.shields.io/badge/API\_Num-16464-red?style=flat-square)
![Dialogues](https://img.shields.io/badge/Current\_Dataset\_Size-12K-red?style=flat-square)
![Dialogues](https://img.shields.io/badge/Total\_API\_Call-37K-red?style=flat-square)
![Dialogues](https://img.shields.io/badge/Average\_Reasoning\_Traces-4.1-red?style=flat-square)
![Dialogues](https://img.shields.io/badge/Tool\_LLaMA-Released-green?style=flat-square)

</div>

<p align="center">
  <a href="#model">Model</a> •
  <a href="#data">Data Release</a> •
  <a href="https://github.com/OpenBMB/BMTools">Toolkit</a> •
  <a href="https://arxiv.org/abs/2304.08354">Paper</a> •
  <a href="https://github.com/thunlp/ToolLearningPapers">Paper List</a> •
  <a href="#citation">Citation</a> •

</p>

</div>


🔨这个项目旨在构建**开源、大规模、高质量**的指令调整 SFT 数据，以促进构建具有通用工具使用能力的强大LLMs。我们的目标是赋予开源 LLMs 掌握成千上万多样的真实世界API能力。我们通过收集高质量的指令调整数据集来实现这一目标。该数据集使用最新的ChatGPT（gpt-3.5-turbo-16k）自动构建，该版本升级了增强的函数调用功能。我们提供数据集、相应的训练和评估脚本，以及在ToolBench上经过微调的强大模型ToolLLaMA。

✨更多有关 ToolBench 的详细信息以及我们的论文即将发布！

<div align="center">
<img src="https://cdn.discordapp.com/attachments/941582479117127680/1111543600879259749/20230526075532.png" width="400px">
</div>

✨✨特点:
 - API收集: 我们从 RapidAPI 收集了 16464 个API。RapidAPI 是一个托管开发者提供的大规模真实世界API的平台。

 - 指令生成: 我们生成了涉及单工具和多工具场景的指令。

 - 答案标注: 我们设计了一种新颖的深度优先搜索决策树方法（DFSDT），以增强LLMs的规划和推理能力。这显著提高了标注效率，并成功地对那些不能用CoT或ReACT回答的复杂指令进行了标注。我们提供的回答不仅包括最终答案，还包括模型的推理过程、工具执行和工具执行结果。

 - API Retriever: 我们整合了API检索模块，为ToolLLaMA提供了开放域的工具使用能力。

 - 所有数据均由OpenAI API自动生成并由我们筛选，整个数据创建过程易于扩展。


<br>
<div align="center">
<img src="assets/overview.png" width="800px">
</div>
<br>

*请注意，当前发布的数据仍然不是最终版本。我们正在进行数据的后期处理，以提高数据质量并增加真实世界工具的覆盖范围。*

*[老版本](https://github.com/OpenBMB/ToolBench/tree/legacy)*
<!-- 💁‍♂️💁💁‍♀️**We need your help!** Curating large-scale real-world APIs and their corresponding tool-use SFT data is not easy, we sincerely invite you to join us in building and refining ToolBench. We will list all participants as co-authors in the final paper. Please contact and join [us](mailto:yujiaqin16@gmail.com) if you're interested. -->

## 🗒️数据

👐ToolBench仅用于研究和教育目的，不应被视为反映此数据集的创作者、所有者或贡献者的观点或意见。该数据集以 CC BY NC 4.0许可证 进行分发。以下是数据集的统计信息:

| 工具数量 | API数量 | 实例数量 | 真实API调用数量 | 平均Reasoning步数 |
|-----------|----------|---------------|---------------|------------------|
| 3451      | 16464    | 12657         | 37204         | 4.1              |


ToolBench包含单工具和多工具场景。多工具场景可以进一步分为类别内多工具和集合内多工具。我们在数据创建过程中使用DFSDT方法。以下是使用DFSDT方法进行数据创建的说明：

<div align="center">

<img src="assets/answer_anno.png" width="800px">

</div>

### 数据发布

 请使用以下链接下载我们的数据集：[数据](https://drive.google.com/drive/folders/1yBUQ732mPu-KclJnuQELEhtKakdXFc3J)。

 - `G1`，`G2`，`G3` 数据分别代表单工具数据，类别内多工具数据和集合内多工具数据。我们在 G1、G2 和 G3 数据内分别划分出训练集、验证集和测试集，并将训练集合并，作为我们的主要实验的训练数据。`toolllama_G123_dfs_train.json` 文件代表合并后的训练集数据。
 - 与工具环境相关的数据位于 `toolenv` 目录下。
 - 我们从每个测试集中抽样 100 个实例。`test_query_ids` 目录包含每个测试集中测试实例的query id。
 - 用于工具检索的数据也包含在 `retrieval` 目录中。


## 🤖模型

我们发布了7b Lora 版本的[ToolLLaMA](https://huggingface.co/pooruss/ToolLLaMA-7b-lora)，该版本是在发布的数据集上以多任务方式训练的。
## 🚀精调
### 安装
克隆这个仓库并进入ToolBench文件夹。
```bash
git clone git@github.com:OpenBMB/ToolBench.git
cd ToolBench
```
安装包 (python>=3.9)
```bash
pip install -r requirements.txt
```

准备数据和工具环境。下载[数据](https://drive.google.com/drive/folders/1yBUQ732mPu-KclJnuQELEhtKakdXFc3J)并解压到ToolBench目录下:
```bash
tar -zxvf data.tar
```


### 训练Retriever
- 数据预处理:
```bash
export PYTHONPATH=./
python data/preprocess_retriever_data.py \
    --query_file data/instruction/G1_query.json \
    --index_file data/test_query_ids/G1_instruction_test_query_ids.json \
    --dataset_name G1 \
    --output_dir data/retrieval/G1
```
- 使用以下命令训练retriever:
```bash
export PYTHONPATH=./
python toolbench/retrieval/train.py \
    --data_path data/retrieval/G1/ \
    --model_name bert-base-uncased \
    --output_path retrieval_model \
    --num_epochs 5 \
    --train_batch_size 32 \
    --learning_rate 2e-5 \
    --warmup_steps 500 \
    --max_seq_length 256
```

### 训练ToolLLaMA
我们的训练代码基于[FastChat](https://github.com/lm-sys/FastChat)开发.您可以使用以下命令用两张A100（80G）训练ToolLLaMA-7b, 训练数据是我们已经处理好的[数据](https://drive.google.com/drive/folders/1yBUQ732mPu-KclJnuQELEhtKakdXFc3J):
```bash
export PYTHONPATH=./
torchrun --nproc_per_node=2 --master_port=20001 toolbench/train/train_long_seq.py \
    --model_name_or_path huggyllama/llama-7b  \
    --data_path  data/toolllama_G123_dfs_train.json \
    --eval_data_path  data/toolllama_G123_dfs_eval.json \
    --conv_template tool-llama-single-round \
    --bf16 True \
    --output_dir toolllama \
    --num_train_epochs 2 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "epoch" \
    --prediction_loss_only \
    --save_strategy "epoch" \
    --save_total_limit 8 \
    --learning_rate 5e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.04 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
    --tf32 True \
    --model_max_length 8192 \
    --gradient_checkpointing True \
    --lazy_preprocess True \
    --report_to none
```

您也可以用以下命令用您自己的方式去预处理并划分数据:
```bash
export PYTHONPATH=./
python preprocess/preprocess_toolllama_data.py \
    --tool_data_dir data/answer/G1_answer \
    --method DFS_woFilter_w2 \
    --output_file data/answer/toolllama_G1_dfs.json
```


训练lora版本:
```bash
export PYTHONPATH=./
deepspeed --master_port=20001 toolbench/train/train_long_seq_lora.py \
    --model_name_or_path huggyllama/llama-7b  \
    --data_path  data/toolllama_G123_dfs_train.json \
    --eval_data_path  data/toolllama_G123_dfs_eval.json \
    --conv_template tool-llama-single-round \
    --bf16 True \
    --output_dir toolllama_lora \
    --num_train_epochs 5 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 2 \
    --evaluation_strategy "epoch" \
    --prediction_loss_only \
    --save_strategy "epoch" \
    --save_total_limit 8 \
    --learning_rate 5e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.04 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --model_max_length 8192 \
    --gradient_checkpointing True \
    --lazy_preprocess True \    
    --deepspeed ds_configs/stage2.json \
    --report_to none
```


## Inference
首先准备您的rapidapi key:
```bash
export RAPIDAPIKEY="your_rapidapi_key"
```

然后用以下命令做inference:
```bash
export PYTHONPATH=./
python toolbench/inference/qa_pipeline.py \
    --tool_root_dir data/toolenv/tools/ \
    --backbone_model toolllama \
    --model_path /path/to/your/toolllama \
    --max_observation_length 1024 \
    --method DFS_woFilter_w2 \
    --input_query_file data/instruction/inference_query_demo.json \
    --output_answer_file data/answer/toolllama_dfs \
    --rapidapi_key $RAPIDAPIKEY
```

**lora**版本的inference:
```bash
export PYTHONPATH=./
python toolbench/inference/qa_pipeline.py \
    --tool_root_dir data/toolenv/tools/ \
    --backbone_model toolllama \
    --model_path huggyllama/llama-7b \
    --lora \
    --lora_path /path/to/your/toolllama_lora \
    --max_observation_length 1024 \
    --method DFS_woFilter_w2 \
    --input_query_file data/instruction/inference_query_demo.json \
    --output_answer_file data/answer/toolllama_lora_dfs \
    --rapidapi_key $RAPIDAPIKEY
```

lora版本的**开放域**, 用以下命令:
```bash
export PYTHONPATH=./
python toolbench/inference/qa_pipeline_open_domain.py \
    --tool_root_dir data/toolenv/tools/ \
    --corpus_tsv_path data/retrieval/G1/corpus.tsv \
    --retrieval_model_path /path/to/your/retrival_model \
    --retrieved_api_nums 5 \
    --backbone_model toolllama \
    --model_path huggyllama/llama-7b \
    --lora \
    --lora_path /path/to/your/toolllama_lora \
    --max_observation_length 1024 \
    --method DFS_woFilter_w2 \
    --input_query_file data/instruction/inference_query_demo_open_domain.json \
    --output_answer_file data/answer/toolllama_lora_dfs_open_domain \
    --rapidapi_key $RAPIDAPIKEY
```


## ToolEval

通过在ToolBench上对LLaMA进行微调，我们得到了**ToolLLaMA**。考虑到人工评估非常耗时，我们借鉴[AlpacaEval](https://tatsu-lab.github.io/alpaca_eval/)开发了一个高效的机器自动评估**ToolEval**，其中包含两个评估指标：

- **通过率**：计算在有限的OpenAI API调用次数内成功完成指令的比例。

- **偏好**：通过比较给定指令的两个答案（动作序列）来衡量。我们预先定义了一组更好答案的标准，这些标准被组织成ChatGPT的提示。我们向评估器提供测试指令和两个候选答案，并获得其偏好。我们对每个答案对进行多次评估以提高系统的可靠性。然后，我们计算**优胜率**（被评估器选择为更优的百分比）和**标准差**（优胜率的标准误差）。有关详细信息，请参阅我们的论文。

为了验证偏好指标的有效性，我们从三种不同方法（ChatGPT+ReACT、GPT4+ReACT和ChatGPT+DFSDT）中随机抽样获得600个测试指令的答案对。然后，我们邀请人工标注人员对它们进行人工偏好注释（每个答案对4个注释，总共2400个注释）。我们使用ChatGPT开发的自动评估器与人工标注者呈现出显著的**75.8%**相关性。我们还获得了不同人工标注者之间的一致性为**83.54%**，与我们的评估器和人类标注者之间的一致性为**80.21%**。

有关ToolEval的更多细节，请参阅我们的论文。


### Evaluation with ToolEval
要在测试集（如G1-Inst.）上评估模型，可以执行以下命令：
- 通过率:
```bash
python toolbench/tooleval/pass_rate.py --answer_dir data/answer/toolllama_dfs/G1_instruction
```
- 优胜率 (参考模型: ChatGPT-ReACT):
```bash
export OPENAI_KEY=""
export REF_MODEL_DATA="data/answer/chatgpt_cot/G1_instruction"
export REF_MODEL_METHOD="CoT"
export TEST_MODEL_DATA="data/answer/toolllama_dfs/G1_instruction"
export TEST_MODEL_METHOD="DFS"
python ./toolbench/tooleval/convert_to_answer_format.py \
    --method CoT \
    --answer_dir $REF_MODEL_DATA \
    --output ${REF_MODEL_DATA}_converted

python ./toolbench/tooleval/convert_to_answer_format.py \
    --method DFS \
    --answer_dir $TEST_MODEL_DATA \
    --output ${TEST_MODEL_DATA}_converted

python ./toolbench/tooleval/automatic_eval_sample.py \
    --output ${REF_MODEL_DATA}_converted \
    --ref_output ${TEST_MODEL_DATA}_converted \
    --method $REF_MODEL_METHOD \
    --use_existed_output
```

### Model Experiment

在我们的主要实验中，ToolLLaMA展现了处理单一工具和复杂多工具指令的引人注目的能力。
以下是与ChatGPT和Text-Davinci-003相比的主要结果。

**通过率**
| model                  | I1-Inst. | I1-Tool. | I1-Cat. | I2-Inst. | I2-Cat. | I3-Inst. | Average |
|------------------------|----------|----------|---------|----------|---------|----------|---------|
| ChatGPT-ReACT          | 66       | 56       | 62      | 22       | 28      | 30       | 44.0    |
| ChatGPT-DFSDT          | **89**       | **78**       | **84**      | **58**       | **51**      | **57**       | **69.6**    |
| Text-Davinci-003-DFSDT | 61       | 53       | 58      | 38       | 38      | 39       | 47.8    |
| ToolLLaMA              | 75       | 68       | 80      | 56       | 47      | 40       | 61.0    |

**优胜率** (参考模型: ChatGPT-DFSDT)
| model                  | I1-Inst. | I1-Tool. | I1-Cat. | I2-Inst. | I2-Cat. | I3-Inst. | Average |
|------------------------|----------|----------|---------|----------|---------|----------|---------|
| Text-Davinci-003-DFSDT | 38       | 34       | 43      | 25       | 20      | 28       | 31.3    |
| ToolLLaMA              | **50**       | 45       | 45      | **59**       | 48      | 46       | 48.8    |


## TODO
- [ ] ToolLLaMA将达到GPT-4的工具使用能力。
- [ ] 我们将训练一个ToolLLaMa-2。

## Citation
如果您对ToolBench感兴趣，欢迎引用我们的工作。

```bibtex
@misc{qin2023tool,
      title={Tool Learning with Foundation Models}, 
      author={Yujia Qin and Shengding Hu and Yankai Lin and Weize Chen and Ning Ding and Ganqu Cui and Zheni Zeng and Yufei Huang and Chaojun Xiao and Chi Han and Yi Ren Fung and Yusheng Su and Huadong Wang and Cheng Qian and Runchu Tian and Kunlun Zhu and Shihao Liang and Xingyu Shen and Bokai Xu and Zhen Zhang and Yining Ye and Bowen Li and Ziwei Tang and Jing Yi and Yuzhang Zhu and Zhenning Dai and Lan Yan and Xin Cong and Yaxi Lu and Weilin Zhao and Yuxiang Huang and Junxi Yan and Xu Han and Xian Sun and Dahai Li and Jason Phang and Cheng Yang and Tongshuang Wu and Heng Ji and Zhiyuan Liu and Maosong Sun},
      year={2023},
      eprint={2304.08354},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```