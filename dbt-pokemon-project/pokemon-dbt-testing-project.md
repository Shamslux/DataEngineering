![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![duckdb](https://img.shields.io/badge/Duckdb-000000?style=for-the-badge&logo=Duckdb&logoColor=yellow)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Installing dbt

## Step-by-Step Guide

1. Install Python on your machine.
2. Install VSCode.
3. Install the VSCode extension called "Power User for dbt Core." See the image below:

![power_user_dbt_vscode](https://github.com/user-attachments/assets/f4a9db01-da5b-40af-b899-afce91772c9b)

4. Create a local folder in your terminal using: `mkdir dbt_local`. 
5. Inside this new directory, use the command: `python -m venv dbt_venv`
6. Now, `dbt_venv` will have some folders, including one called `bin`. Inside `bin`, there are several files, such as `activate`.
7. We need to activate the virtual environment. Based on what was described in step 6, use the command: `source dbt_venv/bin/activate`. This will activate the environment, and you’ll see `(dbt_venv)` appear in the terminal command line.

> **Hint**: There might be an issue during the virtual environment creation. I encountered this myself, and `activate` did not exist. If this happens, carefully repeat the steps, deleting the previous directories using the command: `rm -rf dbt_local`.

## Integration with VSCode Extension Installed

1. Notice that the blue bar in VSCode (at the bottom) will indicate that dbt Core is not installed.
2. Click on this message, and a dialog box will appear at the top. See the image below:

![extension_tutorial_1](https://github.com/user-attachments/assets/13955c45-6063-4add-b821-444f5b4be85a)

3. Select "Setup Extension."
4. Now choose the Python interpreter, as shown in the image below:

![extension_tutorial_2](https://github.com/user-attachments/assets/29535db5-624a-46b7-8015-b2eee3b79130)

5. In the new box that opens, select the path to `dbt_venv` (inside the `bin` folder, choose the `python3` file). After this, the blue bar will look like this:

![extension_tutorial_3](https://github.com/user-attachments/assets/acf20a35-b365-4f25-a421-4df42cc078b2)

# Project Overview

<div align="left">
  <img src="https://github.com/user-attachments/assets/e87be0da-b897-420e-ad9a-65fc24d53bcf" alt="Badge" width="500">
</div>

This is a personal project I created to practice using dbt. In my company, we recently started using the tool, and I picked up some tips from coworkers 
and by watching free courses online. Since I always like to create a basic project to get hands-on with tools I work with, I decided to create a little 
project called PokéMart.



