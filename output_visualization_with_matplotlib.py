# Output:
Dataset
  Month  Sales  Profit
0   Jan    100      20
1   Feb    120      25
2   Mar    150      30
3   Apr    180      40
4   May    170      35
5   Jun    200      50

First 5 Rows
  Month  Sales  Profit
0   Jan    100      20
1   Feb    120      25
2   Mar    150      30
3   Apr    180      40
4   May    170      35

Dataset Information
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Month   6 non-null      object
 1   Sales   6 non-null      int64 
 2   Profit  6 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 192.0+ bytes

Summary Statistics
            Sales     Profit
count    6.000000   6.000000
mean   153.333333  33.333333
std     37.771241  10.801234
min    100.000000  20.000000
25%    127.500000  26.250000
50%    160.000000  32.500000
75%    177.500000  38.750000
max    200.000000  50.000000

Insights
1. Sales show an increasing trend from January to June.
2. June recorded the highest sales value.
3. Higher sales generally result in higher profit.
4. The histogram shows the distribution of sales values.
5. The scatter plot indicates a positive relationship between sales and profit.


