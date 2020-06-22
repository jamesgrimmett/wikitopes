# wikitopes
A web scraper to collect isotope decay data from Wikipedia


Usage
-----

```python
>>> import wikitopes
>>> df = wikitopes.get(elements = ['zinc','plutonium'])
>>> df
   nuclide   Z    N  ... daughter_isotope spin-parity branching_ratio
0     54Zn  30   24  ...             52Ni          0+    1.000000e+00
1     55Zn  30   25  ...             53Ni       5/2−#    1.000000e+00
2     55Zn  30   25  ...             55Cu       5/2−#    1.000000e+00
3     56Zn  30   26  ...             56Cu          0+    1.000000e+00
4     57Zn  30   27  ...             56Ni       7/2−#    6.500000e-01
..     ...  ..  ...  ...              ...         ...             ...
44   244Pu  94  150  ...        (various)          0+    1.230000e-03
45   244Pu  94  150  ...            244Cm          0+    7.300000e-11
46   245Pu  94  151  ...            245Am      (9/2−)    1.000000e+00
47   246Pu  94  152  ...           246mAm          0+    1.000000e+00
48   247Pu  94  153  ...            247Am       1/2+#    1.000000e+00

[79 rows x 9 columns]
```

You can leave the decay mode/branching ratio unprocessed in raw form

```python
>>> import wikitopes
>>> df = wikitopes.get(elements = ['zinc','plutonium'], raw_decay_mode = True)      
>>> df                                                                      
   nuclide   Z    N  ...        decay_mode daughter_isotope spin-parity
0     54Zn  30   24  ...                2p             52Ni          0+
1     55Zn  30   25  ...                2p             53Ni       5/2−#
2     55Zn  30   25  ...                β+             55Cu       5/2−#
3     56Zn  30   26  ...                β+             56Cu          0+
4     57Zn  30   27  ...       β+, p (65%)             56Ni       7/2−#
..     ...  ..  ...  ...               ...              ...         ...
44   244Pu  94  150  ...        SF (.123%)        (various)          0+
45   244Pu  94  150  ...  β−β− (7.3×10−9%)            244Cm          0+
46   245Pu  94  151  ...                β−            245Am      (9/2−)
47   246Pu  94  152  ...                β−           246mAm          0+
48   247Pu  94  153  ...                β−            247Am       1/2+#

[79 rows x 8 columns]
```

Requirements
------------

Python 3.6+ with numpy, pandas, requests, bs4


