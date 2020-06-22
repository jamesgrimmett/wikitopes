# wikitopes
A web scraper to collect isotope decay data from Wikipedia


Usage
-----

```python
>>> import wikitopes
>>> df = wikitopes.get('plutonium')
>>> df.head()
  nuclide     Z      N  ... daughter_isotope spin-parity branching_ratio
0   228Pu  94.0  134.0  ...             224U          0+           0.999
1   228Pu  94.0  134.0  ...            228Np          0+           0.001
2   229Pu  94.0  135.0  ...             225U       3/2+#           1.000
3   230Pu  94.0  136.0  ...             226U          0+           1.000
4   230Pu  94.0  136.0  ...            230Np          0+           0.000

[5 rows x 9 columns]
```

You can pass a list of elements:

```python
>>> import wikitopes
>>> df = wikitopes.get(['zinc','plutonium'])
>>> df
   nuclide     Z      N  ... daughter_isotope spin-parity branching_ratio
0     54Zn  30.0   24.0  ...             52Ni          0+    1.000000e+00
1     55Zn  30.0   25.0  ...             53Ni       5/2−#    1.000000e+00
2     55Zn  30.0   25.0  ...             55Cu       5/2−#    1.000000e+00
3     56Zn  30.0   26.0  ...             56Cu          0+    1.000000e+00
4     57Zn  30.0   27.0  ...             56Ni       7/2−#    6.500000e-01
..     ...   ...    ...  ...              ...         ...             ...
44   244Pu  94.0  150.0  ...        (various)          0+    1.230000e-03
45   244Pu  94.0  150.0  ...            244Cm          0+    7.300000e-11
46   245Pu  94.0  151.0  ...            245Am      (9/2−)    1.000000e+00
47   246Pu  94.0  152.0  ...           246mAm          0+    1.000000e+00
48   247Pu  94.0  153.0  ...            247Am       1/2+#    1.000000e+00

[79 rows x 9 columns]
```


Requirements
------------

Python 3.6+ with numpy, pandas, requests, bs4


