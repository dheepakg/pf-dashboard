import pandas as pd
import requests

from src.priceTrendCapture import priceCapture

two_funds = {"ppfas": 122639, "uti": 107578}
nav_hist_start_dt = "2023-01-12"
nav_hist_end_date = "2023-01-13"
ptc = priceCapture({"ppfas": 122639}, nav_hist_start_dt, nav_hist_end_date)
ptc1 = priceCapture(two_funds, nav_hist_start_dt, nav_hist_end_date)


def test_cleanNAV(
    st_dt="2023-01-12", end_date="2023-01-13", fund_num="ppfas", schemeCode=122639
):
    """
    Tests cleanNAV method.
    """
    scheme_url = "https://api.mfapi.in/mf/" + str(schemeCode)
    df_scheme_data = requests.get(scheme_url)

    df_scheme = df_scheme_data.json()["data"]

    df_superset = pd.DataFrame.from_records(df_scheme)

    df_superset["date"] = pd.to_datetime(df_superset.date, dayfirst=True)

    df_superset.set_index("date", inplace=True)

    df_superset.rename(columns={"nav": fund_num}, inplace=True)

    df_fund = df_superset.loc[st_dt:end_date]

    assert df_fund.equals(ptc.cleanNAV("ppfas", 122639))


def test_fetchFundNAV():
    """
    Tests the fetchFundNAV method.
    """
    fund_nav = dict()
    fund_nav_from_method = ptc1.fetchFundNAV()
    validation_flag = list()
    for fund_seq, fund_code in two_funds.items():
        scheme_url = "https://api.mfapi.in/mf/" + str(fund_code)
        df_scheme_data = requests.get(scheme_url)

        df_scheme = df_scheme_data.json()["data"]

        df_superset = pd.DataFrame.from_records(df_scheme)

        df_superset["date"] = pd.to_datetime(df_superset.date, dayfirst=True)

        df_superset.set_index("date", inplace=True)

        df_superset.rename(columns={"nav": str(fund_seq)}, inplace=True)

        df_fund = df_superset.loc[nav_hist_start_dt:nav_hist_end_date]

        fund_nav[str(fund_seq)] = df_fund

    list_built_from_method = list(fund_nav_from_method.values())
    list_built_for_testing = list(fund_nav.values())

    assert list_built_from_method[0].equals(
        list_built_for_testing[0]
    ) and list_built_from_method[1].equals(list_built_for_testing[1])


def test_joinFundNAVs():
    """
    Tests joinFundNAVs method.
    """
    df_from_method = ptc1.joinFundNAVs()

    fund_nav = dict()
    for fund_seq, fund_code in two_funds.items():
        scheme_url = "https://api.mfapi.in/mf/" + str(fund_code)
        df_scheme_data = requests.get(scheme_url)

        df_scheme = df_scheme_data.json()["data"]

        df_superset = pd.DataFrame.from_records(df_scheme)

        df_superset["date"] = pd.to_datetime(df_superset.date, dayfirst=True)

        df_superset.set_index("date", inplace=True)

        df_superset.rename(columns={"nav": str(fund_seq)}, inplace=True)

        df_fund = df_superset.loc[nav_hist_start_dt:nav_hist_end_date]

        df_fund.reset_index()
        df_fund['id'] = None

        # Columns are reordered as per sqlite table structure
        column_list = df_fund.columns.values
        col_id_date = [column_list[-1], column_list[0]]
        list_of_funds =list( column_list[1:-1])  # NumPy array is converted into list
        new_column_list = col_id_date + list_of_funds

        df_fund = df_fund[new_column_list]

        fund_nav[fund_seq] = df_fund


    df_built_for_testing = pd.concat(
        list(fund_nav.values()), join="outer", axis=1, sort=False
    ).sort_index()

    print("Testing > ", df_built_for_testing)

    assert df_built_for_testing.equals(df_from_method)
