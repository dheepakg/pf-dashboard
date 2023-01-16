import pandas as pd
import requests


class priceCapture:
    def __init__(
        self,
        schemeDetails: dict,
        nav_hist_start_dt="2015-10-01",
        nav_hist_end_date="2023-01-13",
    ) -> None:
        self.schemeDetails = schemeDetails
        self.nav_hist_start_dt = nav_hist_start_dt
        self.nav_hist_end_dt = nav_hist_end_date
        self.fund_nav = dict()

    def cleanNAV(self, fund_num: int, schemeCode: int):
        scheme_url = "https://api.mfapi.in/mf/" + str(schemeCode)

        df_scheme_data = requests.get(scheme_url)

        df_scheme = df_scheme_data.json()["data"]

        df_superset = pd.DataFrame.from_records(df_scheme)

        df_superset["date"] = pd.to_datetime(df_superset.date, dayfirst=True)

        df_superset.set_index("date", inplace=True)

        df_superset.rename(columns={"nav": str(fund_num)}, inplace=True)

        df_fund = df_superset.loc[self.nav_hist_start_dt : self.nav_hist_end_dt]

        return df_fund

    def fetchFundNAV(self) -> dict:

        for fund_seq, fund_code in self.schemeDetails.items():
            self.fund_nav["fund" + str(fund_seq)] = self.cleanNAV(fund_seq, fund_code)

        return self.fund_nav

    def joinFundNAVs(self):

        df_final = pd.concat(
            list(self.fetchFundNAV().values()), join="outer", axis=1, sort=False
        ).sort_index()

        return df_final


# fund_dict = {'fund1':122639, 'fund2':107578 }

# obj = priceCapture(fund_dict)

# print("return >>  ",obj.joinFundNAVs())
