# M-Schema: a semi-structure representation of database schema
## Introduction
MSchema is a semi-structured schema representation of database structure, which could be used in various scenarios such as Text-to-SQL.
This repository contains the code for connecting to the database and constructing M-Schema.
We support a variety of relational databases, such as MySQL, PostgreSQL, Oracle, etc.

```text
【DB_ID】card_games
【Schema】
# Table: rulings
[
(id:INTEGER, unique id identifying this ruling, Primary Key, Examples: [1, 2, 3]),
(date:DATE, date, Examples: [2007-07-15]),
(text:TEXT, description about this ruling),
(uuid:TEXT, Examples: [6d268c95-c176-5766-9a46-c14f739aba1c])
]
# Table: cards
[
(id:INTEGER, Primary Key, Examples: [41138, 1349, 23810]),
(artist:TEXT, The name of the artist that illustrated the card art., Examples: [Pete Venters, Volkan Baǵa, Justin Sweet]),
(availability:TEXT, A list of the card's available printing types., Examples: [mtgo,paper, paper, arena]),
(borderColor:TEXT, The color of the card border., Examples: [black, white, borderless]),
(edhrecRank:INTEGER, The card rank on EDHRec, Examples: [15650, 12702, 11081]),
(faceConvertedManaCost:REAL, The converted mana cost or mana value for the face for either half or part of the card., Examples: [4.0, 5.0, 6.0]),
(faceName:TEXT, The name on the face of the card., Examples: [Dusk, Dawn, Commit]),
(uuid:TEXT, The universal unique identifier (v5) generated by MTGJSON. Each entry is unique., Examples: [00010d56-fe38-5e35-8aed-518019aa36a5])
]
【Foreign keys】
legalities.uuid=cards.uuid
```

## Requirements
+ python >= 3.9
```shell
pip install -r requirements.txt
```

## Quick Start
You can just connect to the database using [```sqlalchemy```](https://www.sqlalchemy.org/) and construct M-Schema representation.

1、create a database connection.

Take PostgreSQL as an example:
```python
from sqlalchemy import create_engine
db_name = 'mydatabase'
db_engine = create_engine(f"postgresql+psycopg2://scott:tiger@localhost:5432/{db_name}")
```

2、construct M-Schema representation.
```python
from schema_engine import SchemaEngine

schema_engine = SchemaEngine(engine=db_engine, db_name=db_name)
mschema = schema_engine.mschema
mschema_str = mschema.to_mschema()
print(mschema_str)
mschema.save(f'./{db_name}.json')
```

3、Text-to-SQL Generation
```python
dialect = db_engine.dialect.name
question = ''
evidence = ''
prompt = """You are now a {dialect} data analyst, and you are given a database schema as follows:

【Schema】
{db_schema}

【Question】
{question}

【Evidence】
{evidence}

Please read and understand the database schema carefully, and generate an executable SQL based on the user's question and evidence. The generated SQL is protected by ```sql and ```.
""".format(dialect=dialect, question=question, db_schema=mschema, evidence=evidence)

# Replace the function call_llm() with your own function or method to interact with a LLM API.
response = call_llm(prompt)
```


## Citation
If you find our work helpful, feel free to give us a cite.

```bibtext
@article{xiyansql,
      title={XiYan-SQL: A Multi-Generator Ensemble Framework for Text-to-SQL}, 
      author={Yingqi Gao and Yifu Liu and Xiaoxia Li and Xiaorong Shi and Yin Zhu and Yiming Wang and Shiqi Li and Wei Li and Yuntao Hong and Zhiling Luo and Jinyang Gao and Liyu Mou and Yu Li},
      year={2024},
      journal={arXiv preprint arXiv:2411.08599},
      url={https://arxiv.org/abs/2411.08599},
      primaryClass={cs.AI}
}
```
