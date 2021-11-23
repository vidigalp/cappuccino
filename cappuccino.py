# https://kb.novaordis.com/index.php/G1

import os
import pandas as pd
import numpy as np
import click
from Cappuccino.auxiliary import get_gc_parser

pd.set_option('display.max_columns', None)

@click.command()
@click.argument('data_directory', required=False)
@click.argument('log_file', type=click.File('rb'), required=False)
def main(data_directory, log_file):

    df = pd.DataFrame()

    if data_directory:
        df_list = []
        for root, subdirectories, files in os.walk(data_directory):
            for file in files:
                if any(x in file for x in ('.log',)):
                    parser = get_gc_parser(input_file=f"{root}/{file}")
                    parser.run()
                    df_list.append(parser.to_df())

        if df_list:
            df = pd.concat(df_list, axis=0)
            df = df.drop_duplicates()



    if log_file:
        parser = get_gc_parser(input_file=file)
        parser.run()
        df = parser.to_df()

    if not df.empty:
        df = df[['pause_type', 'real_time_seconds_float']].dropna()
        print(df.groupby(["pause_type"])['real_time_seconds_float'].describe())

    if not log_file and not data_directory:
        print('Please include a log file or Directory containing log files')

if __name__ == '__main__':
    main()
