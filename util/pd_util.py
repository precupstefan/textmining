import pandas as pd


def get_dataframe_row(wordCount: {}, columns: [str]) -> [int]:
    row = []
    for entry in columns:
        if entry in wordCount:
            row.append(wordCount[entry])
        else:
            row.append(0)
    return row


def build_dataframe_without_topics(wordCounts, globalDictionary) -> pd.DataFrame:
    columns = [*globalDictionary]
    dataframe = pd.DataFrame(columns=columns)
    row_index = 1
    for key in wordCounts.keys():
        row = get_dataframe_row(wordCounts[key], columns)
        dataframe.loc[row_index] = row
        row_index += 1
    return dataframe


def add_column_to_dataframe(dataset: pd.DataFrame, columns) -> pd.DataFrame:
    column_dataframe = pd.DataFrame(columns[1:], columns=[columns[0]])
    return pd.concat([dataset, column_dataframe], axis=1)


def add_topics_to_dataset(dataset: pd.DataFrame, topics: {}) -> pd.DataFrame:
    columns = ["topics"]
    for key in topics.keys():
        topics_string = ""
        for topic in topics[key]:
            topics_string += topic + ","
        topics_string = topics_string[:-1]
        columns.append(topics_string)
    return add_column_to_dataframe(dataset, columns)
