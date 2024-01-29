![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatgpt-343434?style=for-the-badge&logo=openai&logoColor=white)

<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/fffa0fdc-4cf8-4845-8e51-9cf7d9bb9900" alt="Badge" width="200">
</div>


# SQL Review Course with ChatGPT

I have a dear friend - who, by the way, helped me get into the Data field - who always reminds me that we should
practice SQL a lot. Currently, I have 2 years of experience in the field, always working with SQL.

However, it's always good to review the basic contents. With that in mind, and with a desire to test ChatGPT's ability
to generate interesting questions to aid human learning, I decided to request some questions from it to practice SQL.

The database I used is a personal database created for study purposes, created by me last year, to practice Business
Intelligence and Data Engineering projects. However, I prefer to review the basics and practice with some tools before
consolidating everything into a large skills demonstration project.

# Mini Project's Structure

This small project is based on the fictional dataset of a game store called "Skeam." They sell games from various
platforms, categories, etc., to users from around the world.

This training will aim to create 100 questions for junior, mid-level, and senior professional levels.

In addition to the folders with scripts and solutions, this document will also record the solutions with images (I will
update as time permits, so there may be a discrepancy between what is in the script and what is updated in this
document).

I will not share the database now, but I will share it when I create a more robust project in the future. Feel free to
adapt the questions used for your personal projects.

Some questions ended up repeating, probably, even though I asked ChatGPT to avoid this. In fact, the idea was to create
500 junior-level questions, but given the limited dataset, everything started to become uncomfortably repetitive, so I
decided it would be better to limit all questions to just 100 per professional hierarchical level.


# 100 Junior Questions Solutions

<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/fa7d8997-be71-40a2-bd8f-899d306a4196" alt="Badge" width="150">
</div>

## 1. List all games from the tb_games table.

```sql
SELECT	nm_title 
FROM	tb_games;
```

![s1_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/42007bcd-2a05-4ce4-a942-190d57962de3)

## 2. Show the names and release years of games from the tb_games table.

```sql
SELECT	nm_title
		, nm_release_year 
FROM	tb_games;
```

![s2_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/0dfa032f-655f-4a2c-9660-b2e9d1846c11)
