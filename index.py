from pandas import read_csv as rc; from plotly.figure_factory import create_distplot as cd
cd([rc("data.csv")["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False).show()
