import pandas as pd
import requests


class priceCapture:
    """
    This is to capture historical NAVs between 2 dates.

    Attributes:
    -----------
    schemaDetails : dict
        a dict with unique ID (to identify fund) and the scheme's AMFI number.

    nav_hist_start_dt : str
        Start date from which NAVs to be captured.

    nav_hist_end_dt : str
        End date till which the NAVs to be captured.

    Methods
    ------
    cleanNAV(fund_num, schemeCode)
        Cleans the date and captures the NAV between start & end date.

    fetchFundNAV()
        Fetches NAVs of multiple funds.

    joinFundNAVs()
        Joins multiple the fund scheme's NAVs into single Dataframe.
    """

    def __init__(
        self,
        schemeDetails: dict,
        nav_hist_start_dt: str = "2015-10-01",
        nav_hist_end_date: str = "2023-01-13",
    ) -> None:
        self.schemeDetails = schemeDetails
        self.nav_hist_start_dt = nav_hist_start_dt
        self.nav_hist_end_dt = nav_hist_end_date
        self.fund_nav = dict()

    def cleanNAV(self, fund_name: str, schemeCode: int):
        """
        Cleans the date and captures the NAV between start & end date.

        Reformat date to YYYY-MM-DD and fetches NAV between nav_hist_start_dt & nav_hist_end_dt (Class attributes).
        Returns dataframe.

        Parameters:
        ----------
        fund_num: str
            The fund name to identify fund scheme.

        schemeCode: int
            This is fund's AMFI code.

        """
        scheme_url = "https://api.mfapi.in/mf/" + str(schemeCode)

        df_scheme_data = requests.get(scheme_url)

        df_scheme = df_scheme_data.json()["data"]

        df_superset = pd.DataFrame.from_records(df_scheme)

        df_superset["date"] = pd.to_datetime(df_superset.date, dayfirst=True)

        df_superset.set_index("date", inplace=True)

        df_superset.rename(columns={"nav": fund_name}, inplace=True)

        df_fund_with_date_index  = df_superset.loc[self.nav_hist_start_dt : self.nav_hist_end_dt]

        return df_fund_with_date_index

    def fetchFundNAV(self) -> dict:
        """
        Fetches NAVs of multiple funds.

        Returns dictionary with key as fund<num>:DF.

        Example fund1: Dataframe
        """
        for fund_nm, fund_code in self.schemeDetails.items():
            self.fund_nav[fund_nm] = self.cleanNAV(fund_nm, fund_code)


        return self.fund_nav

    def joinFundNAVs(self):
        """
        Joins multiple the fund scheme's NAVs into single Dataframe.

        All the fund details passed in the config.toml is read and their corresponding NAVs are added as individual columns against date.
        """

        df_final_with_date_index = pd.concat(
            list(self.fetchFundNAV().values()), join="outer", axis=1, sort=False
        ).sort_index()

        df_final = df_final_with_date_index.reset_index()
        df_final['id'] = None  # Column value for auto-increment field in sqlite
        # Columns are reordered as per sqlite table structure
        column_list = df_final.columns.values
        print("Column list >> ",column_list)
        col_id_date = [column_list[-1], column_list[0]]

        list_of_funds =list( column_list[1:-1])  # NumPy array is converted into list
        new_column_list = col_id_date + list_of_funds
        print("New column list >> ",new_column_list)
        df_final = df_final[new_column_list]

        print("NEw column list >> ",df_final.columns.values.tolist())
        return df_final


# price = priceCapture({'ppfas':122639,
#                       'mirae':107578,
#                       'nifty50':120716,
#                       'icici_tax': 100354,
#                       'icici_scap' : 106823,
#                       'prima': 100473,
#                       'absl96' : 107745
#                       },
#                         nav_hist_start_dt='2023-01-02',nav_hist_end_date='2023-01-04')


# print(price.cleanNAV('ppfas',122639))
# df = price.joinFundNAVs()
# print(df)



