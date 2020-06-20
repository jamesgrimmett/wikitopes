import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from contextlib import closing

urlbase = 'https://en.wikipedia.org/wiki/Isotopes_of_'

def get_page_content(url):
    try:
        with closing(requests.get(url)) as resp:
            if response_is_html(resp):
                return resp.content
            else:
                print('Check URL. Cannot retrieve HTML from:')
                print('{}'.format(url))
                return None
    except requests.RequestException as error:
        print(error)
        return None

def response_is_html(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def parse_decay_mode(data):
    """
    check format: str + brackets, str, or nan (or ?)
    convert branching ratio if present
    return [mode,BR]
    """

    # Drop trailing notation if present 
    dat = data.split(')')
    dat = dat[0].split('(')

    # Decay mode should have channel, and branching percentage 
    # E.g. "EC (94%)" or just "EC". Assume 100% if percentage is not present.
    if len(dat) < 2:
        dat.append('100')
    elif len(dat) != 2:
        raise Exception('Unknown format in decay mode: {}'.format(dat))
    dat[1] = dat[1].strip(')').strip('%')

    # Covert percentage (string) to float.
    # Some percentages given in scientific notation.
    # Check for presence of '×' i.e. chr(215).
    if chr(215) in dat[1]:
        num = dat[1].split(chr(215))
        base = float(num[0])
        # Negative sign '-' is chr(8722)
        power = float(num[1].split(chr(8722))[1])
        dat[1] = base * 10**-power 
    elif 'rare' in dat[1]:
        dat[1] = 0.0
    else:
        dat[1] = float(dat[1]) 

    # Convert percentage to ratio
    dat[1] = dat[1] * 1.e-2
    
    return dat
    
def set_decay_and_branching(df):
    """
    Parse decay mode and branching data, split into separate columns
    """
    df.loc[:,'decay_mode'] = df.decay_mode.apply(lambda row: parse_decay_mode(row))
    # Split decay mode and branching ratio into separate columns
    df.loc[:,'branching_ratio'] = df.decay_mode.apply(lambda row: row[1]) 
    df.loc[:,'decay_mode'] = df.decay_mode.apply(lambda row: row[0]) 

    return df

def get_isotope_table(html,el,keep_isomers=False):
    """
    All isotope wikipedia pages should have the same layout,
    with isotope table being the second table on the page.
    """
    if keep_isomers:
        raise Exception('Parsing isomer data is not yet implemented')

    tables = html.findAll('table',{'class','wikitable'})
    cols = ['nuclide','Z','N','isotopic_mass',
                'half_life','decay_mode','daughter_isotope',
                    'spin-parity']
    df = pd.read_html(str(tables[1]))[0]

    # Table should have at least 8 columns, as listed above.
    if len(df.columns) < 8:
        print('Columns for {}:'.format(el))
        print(df.columns)
        raise Exception('Table should have at least 8 columns. Wrong table?')
    # Drop the last columns (isotopic/natural abundance) 
    else:
        df.drop(df.columns[8:], axis = 1, inplace = True)
        df.columns = cols    

    if not keep_isomers:
        # Drop rows which contain excited isomers
        df.Z = pd.to_numeric(df.Z, errors = 'coerce')
        df.N = pd.to_numeric(df.N, errors = 'coerce')
        # Check that rows match in Z and N before dropping
        if (df.Z.notna() == df.Z.notna()).all():
            df = df[df.Z.notna()]
        else:
            raise Exception('Unexpected missing data in Z or N column.')

    # remove notation from some nuclides
    df.loc[:,'nuclide'] = df.nuclide.apply(lambda row: row.split('[')[0]) 
    
    return df

def main(elements = 'plutonium'):
    elements = np.array([elements])
    element_dict = {'plutonium': 'Pu'}

    for el in elements:
        url = urlbase + el
        content = get_page_content(url)
        html = BeautifulSoup(content,'html.parser') 
        df = get_isotope_table(html,el)
        df = set_decay_and_branching(df)

    return df


if __name__ == 'main':
    main()
