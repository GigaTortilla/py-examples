import logging
from example_logs import init_log
import numpy as np
import pandas as pd


def main(argv=None) -> int:
    init_log(logname="pandas")
    logging.info("Logging started.")
    logging.info("NumPy version: " + np.__version__)
    logging.info("Pandas version: " + pd.__version__)

    # Zwei Series erzeugen und zu einem Dataframe zusammenführen
    my_series_1 = pd.Series(np.random.randn(5))
    my_series_2 = pd.Series(np.random.randn(5))
    my_df_1 = pd.concat([my_series_1, my_series_2], axis=1)
    logging.debug("Dataframe from two Series: " + str(my_df_1))

    # Erzeugen eines Dataframes aus einem Dictionary
    my_dic = {"Name": ['Bernd', 'Silke', 'Claudia'],
              "Alter": [54, 36, 23], "Lieblingszahl": np.random.randn(3)}
    my_df_2 = pd.DataFrame(my_dic)
    logging.debug("Dataframe from dictionary: " + str(my_df_2))

    # CSV-Datei einlesen und Infos darstellen
    dat_csv = pd.read_csv('data/sample_data.csv')
    logging.debug("Dataframe from .csv file: " + str(dat_csv))
    logging.debug("Dataframe information: " + str(dat_csv.info()))
    logging.debug("Descriptive statistics: " + str(dat_csv.describe()))
    logging.debug("Elements per col for \"resp\": " + str(dat_csv['resp'].value_counts()))
    logging.debug("Number of missing values: " + str(dat_csv.isna().sum()))
    logging.debug("Access dataframe areas: " + str(dat_csv.iloc[2:5, 3:6].values))

    # Duplizierte Zeilen finden und entfernen
    logging.debug("Duplicates in the dataframe: " + str(dat_csv.duplicated()))
    dat_csv.drop_duplicates()

    # Fehlende Werte können ersetzt werden
    fill_values = {'place': np.nanmedian(dat_csv['place']),
                   'min': np.mean(dat_csv['min']),
                   'max': np.mean(dat_csv['max']),
                   'type': 'trad',
                   'public': True,
                   'date': '1/1/2017',
                   'fee': '£250.00'}
    dat_csv.fillna(fill_values, inplace=True)
    logging.debug("New dataframe with missing values filled in: "
                  + str(dat_csv))
    
    # Pfundzeichen in 'fee'-Spalte entfernen 
    # und nach float konvertieren. Danach Werte in 'resp' ersetzen
    dat_csv['fee'] = dat_csv['fee'].map(lambda x: str(x)[1:]).astype('float')
    replace_dict = {
        'CT': 'City',
        'AS': 'Ass.'
    }
    dat_csv.replace(to_replace=replace_dict, inplace=True)
    logging.info("Preprocessed data: " + str(dat_csv))
    csv_path = 'data/preprocessed_data.csv'
    dat_csv.to_csv(csv_path)
    logging.info("Saved to " + csv_path)

    logging.shutdown()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
