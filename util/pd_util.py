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
