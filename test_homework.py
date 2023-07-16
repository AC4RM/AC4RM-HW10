from solution import *
from pathlib import Path
import urllib.request
import sqlite3
import pandas as pd
import sklearn
import re
import numpy as np


def test_python():

    assert register_student('Jane', 'Doe', semester='Summer', year='2023') == 'Jane Doe is registered for Summer 2023'
    assert register_student('John', 'Doe', 'Jack', semester='Summer', year='2023', course='AC4RM') == 'John Jack Doe is registered for Summer 2023 AC4RM'


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')

    invoice_df = pd.read_sql_query(sql_query_1, con)
    product_df = pd.read_sql_query(sql_query_2, con)

    assert invoice_df.shape[0] == 8
    assert "56-934-0748" in invoice_df['number'].values
    assert product_df.shape[0] == 1
    assert 98 in product_df['quantity_in_stock'].values

    Path('data.db').unlink(missing_ok=True)


def test_model():
    model, predictions = train_model()

    assert isinstance(model, sklearn.linear_model._logistic.LogisticRegression)
    assert sum(predictions) == 71


def test_regex():

    assert re.findall(regex_pattern, "His email is john.doe@gmail.com and twitter is @johndoe") == ["@johndoe"]
    assert re.findall(regex_pattern, "Her twitter account is @janedoe and her email address is jane.doe@gmail.com") == ["@janedoe"]

