# Constants module for cemo.
REGION = {
    1: 'NSW',
    2: 'QLD',
    3: 'SA',
    4: 'TAS',
    5: 'VIC'
}

TECH_TYPE = {
    1: 'biomass',
    2: 'ccgt',
    3: 'ccgt_ccs',
    4: 'coal_sc',
    5: 'coal_sc_ccs',
    6: 'brown_coal_sc',
    7: 'brown_coal_sc_ccs',
    8: 'ocgt',
    9: 'solar_pv_dat',
    10: 'solar_pv_ffp',
    11: 'solar_pv_sat',
    12: 'wind',
    13: 'cst_6h',
    14: 'phes_6h',
    15: 'battery_2h',
    16: 'recip_engine',
    17: 'wind_h',
    18: 'hydro',
    19: 'gas_thermal',
    20: 'pumps'
}

ZONE = {
    1: 'NQ',
    2: 'CQ',
    3: 'SWQ',
    4: 'SEQ',
    5: 'SWNSW',
    6: 'CAN',
    7: 'NCEN',
    8: 'NNS',
    9: 'LV',
    10: 'MEL',
    11: 'CVIC',
    12: 'NVIC',
    13: 'NSA',
    14: 'ADE',
    15: 'SESA',
    16: 'TAS'
}

DEFAULT_FUEL_PRICE = {
    1: 0.5,
    2: 9.68,
    3: 9.68,
    4: 3,
    5: 3,
    6: 3,
    7: 3,
    8: 9.68,
    16: 9.68,
    19: 9.68
}

DEFAULT_HEAT_RATE = {
    1: 12.66,
    2: 6.93,
    3: 6.93,
    4: 8.66,
    5: 8.66,
    6: 12.4,
    7: 12.4,
    8: 10.15,
    16: 7.6,
    19: 10.7
}

DEFAULT_FUEL_EMIT_RATE = {
    1: 57.13,
    2: 420.0,
    3: 420.0,
    4: 850.0,
    5: 850.0,
    6: 1100.0,
    7: 1100,
    8: 602.0,
    16: 602.0,
    19: 705.0
}

DEFAULT_HYDRO_MWH_MAX = {
    1: 195000,
    3: 0,
    4: 0,
    5: 3294000,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    12: 4753000,
    14: 0,
    16: 11287000
}

DEFAULT_RETIREMENT_COST = {
    2: 10487.98,
    3: 10487.98,
    4: 52439.9,
    5: 52439.9,
    6: 83903.4,
    7: 83903.4,
    8: 5243.99,
    11: 20975.96,
    12: 10487.98,
    16: 52439.9,
    19: 52439.9  # Sould this be 10 like for gas?
}

DEFAULT_TECH_LIFETIME = {
    1: 60.0,
    2: 40.0,
    4: 60.0,
    8: 40.0,
    11: 30.0,
    12: 30.0,
    13: 30.0,
    14: 30.0,
    15: 30.0,

}
# First number in the sum is AEMO ISP build limits
# Second number in the sum is existing tech as per capacity by 2020
# TODO Check that wind existing is by 2020
# TODO impose a limit of 0 to PHES and CSP for regions that do not allow it
# TODO Make sure that wind is not double counted in Riverina and Murray river
DEFAULT_BUILD_LIMIT = {
    1: {
        11: 9250 + 1001,
        12: 8350 + 235
    },
    2: {
        11: 6000 + 170,
        12: 2105
    },
    3: {
        11: 4000 + 135,
        12: 2090 + 453
    },
    4: {
        11: 0 + 52.5,
        12: 0
    },
    5: {
        11: 8000 + 29.9,
        12: 5475 + 199
    },
    6: {
        11: 1000 + 0,
        12: 1735 + 914
    },
    7: {
        11: 6750 + 150,
        12: 2265 + 431
    },
    8: {
        11: 5000 + 57,
        12: 2760 + 270
    },
    9: {
        11: 0,
        12: 105 + 445
    },
    10: {
        11: 30,
        12: 1725 + 1220
    },
    11: {
        11: 3000 + 822,
        12: 1185 + 2069
    },
    12: {
        11: 0 + 453,
        12: 0
    },
    13: {
        11: 11950 + 330,
        12: 2770 + 1462
    },
    14: {
        11: 0,
        12: 1820 + 35
    },
    15: {
        11: 0,
        12: 1355 + 484
    },
    16: {
        11: 0,
        12: 3480 + 592
    }
}

DEFAULT_CAP_FACTOR = {
    1: 0.5,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 1,
    8: 1,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 1,
    15: 1,
    16: 1,
    17: 1,
    18: 1,
    19: 1
}

DEFAULT_GEN_RAMP_PENALTY = {
    4: 5,
    6: 100,
    19: 25
}

DISPLAY_ORDER = [6, 7, 4, 5, 1, 16, 19, 2, 3, 8, 15, 18, 14, 12, 13, 9, 10, 11]

GEN_TECH = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 18, 19, 20]
RE_GEN_TECH = [1, 9, 10, 11, 12, 18]
GEN_TRACE = [9, 10, 11, 12]
FUEL_TECH = [1, 2, 3, 4, 5, 6, 7, 8, 16, 19]
HYB_TECH = [13]
STOR_TECH = [14, 15]

# IDEA These three may be exposed to users?
RETIRE_TECH = [2, 3, 4, 5, 6, 7, 8, 16, 19]
NOBUILD_TECH = [3, 4, 5, 6, 7, 9, 10, 16, 18, 19]
SYNC_TECH = [1, 2, 3, 4, 5, 6, 7, 8, 13, 15, 16, 18, 19]
