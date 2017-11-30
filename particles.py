
# coding: utf-8

"""particles treat notebooks as data"""


from nbformat import reads, v4 
from pandas import concat, DataFrame, to_datetime 
from pathlib import Path 


def read_notebooks(dir:str='.')->DataFrame:
    """Read a directory of notebooks into a pandas.DataFrame
    >>> df = read_notebooks('.')
    >>> assert len(df) and isinstance(df, DataFrame)"""
    return concat({
        file: DataFrame(reads(file.read_text(), 4)['cells'])
        for file in Path(dir).glob('*.ipynb')
    }).reset_index(-1, drop=True)


def files_to_data(df:DataFrame)->DataFrame:
    """Transform an index of Path's to a dataframe of os_stat.
    >>> df = files_to_data(read_notebooks())
    """
    stats, index = [], df.index.unique()
    for file in index:
        stat = file.stat() 
        stats.append({
            key: to_datetime(
                getattr(stat, key), unit=key.endswith('s') and key.rsplit('_')[-1] or 's'
            ) if 'time' in key else getattr(stat, key)
            for key in dir(stat) if not key.startswith('_') and not callable(getattr(stat, key))})
    # Append the change in time to the dataframe.
    return DataFrame(stats, index).pipe(lambda df: df.join((df.st_mtime - df.st_birthtime).rename('dt')))

