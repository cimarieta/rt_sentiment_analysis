# coding: utf-8
import codecs
from langdetect import detect
import pandas as pd


def sum_fields(row, fields):
    """ Sum fields `fields` from a row
    """
    value_fields = []
    for col in fields:
        cell_value =row[col]
        if not pd.isnull(cell_value) and unicode(cell_value).isnumeric():
            value_fields.append(cell_value)
    return sum(value_fields)


def get_ratio(value, total):
    """ Return ratio value/total
        (assumes value and total are numeric)
    """
    return u'{0:.2f}'.format(100*float(value)/total)


def read_data_to_df():
    """ Read data into dataframe
    """
    df = pd.DataFrame()
    filenames = ['data/rt-polarity.neg', 'data/rt-polarity.pos']
    for filename in filenames:
        with codecs.open(filename, 'r', 'utf-8') as f:
            lines = f.readlines()
        lines = [u' '.join(line.split()).strip() for line in lines]
        df_aux = pd.DataFrame()
        df_aux['review'] = lines
        positive_label = u'.pos' in filename
        df_aux['label'] = int(positive_label)
        df = pd.concat([df, df_aux])
    return df


def gen_df_lang_label():
    """ Generate df with language and counts
    """
    # load data
    df = read_data_to_df()

    # apply language detection
    df['language'] = df['review'].apply(detect)

    # generate pivot table
    table_lang_label = pd.pivot_table(
        df,
        values=u'review',
        index=[u'language'],
        columns=[u'label'],
        aggfunc=len,
        fill_value=0
    )
    df_lang_label = table_lang_label.reset_index()
    # calculate total and total %
    df_lang_label[u'total'] = df_lang_label.apply(sum_fields, args=[[0,1]], axis=1)
    total = len(df) # total is the number of rows of df
    df_lang_label[u'total %'] = df_lang_label[u'total'].apply(get_ratio, args=[total])
    df_lang_label.columns=[u'língua', 'negativa', 'positiva', 'total', 'total %']
    return df_lang_label
