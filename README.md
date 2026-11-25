# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_00:03:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,722 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 00:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.89 | 🟢 Normal | 254.618 | 🔺 Rising |
| 2026-11-26 00:02:51 | Glencourse (Kelani Ganga) | 12.29 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-26 00:02:48 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.061 |  |
| 2026-11-26 00:02:48 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:02:17 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.150 |  |
| 2026-11-26 00:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.00 | 🟢 Normal | 254.618 | 🔺 Rising |
| 2026-11-26 00:02:16 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-26 00:02:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:01:43 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:01:28 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:01:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-26 00:01:18 | Moragaswewa (Deduru Oya) | 1.95 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-11-26 00:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 22:02:20 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-11-25 22:00:14 | Peradeniya (Mahaweli Ganga) | 5.26 | 🟡 Alert | -0.241 |  |
| 2026-11-26 00:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.89 | 🟢 Normal | 254.618 | 🔺 Rising |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-25 23:01:15 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-26 00:01:18 | Moragaswewa (Deduru Oya) | 1.95 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-11-26 00:01:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-25 23:03:58 | Holombuwa (Kelani Ganga) | 2.47 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-25 23:02:44 | Giriulla (Maha Oya) | 2.82 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-26 00:02:51 | Glencourse (Kelani Ganga) | 12.29 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-26 00:02:16 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-25 23:00:45 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-25 23:05:43 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-25 22:02:12 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 00:01:28 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:02:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:02:48 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-26 00:01:43 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-11-25 23:07:42 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-25 23:01:19 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-25 23:04:37 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-25 23:06:35 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-25 23:00:21 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-25 23:05:18 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.019 |  |
| 2026-11-26 00:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-25 23:02:16 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 23:01:24 | Horowpothana (Yan Oya) | 2.72 | 🟢 Normal | -0.023 |  |
| 2026-11-25 23:10:02 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-11-25 23:07:30 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.028 |  |
| 2026-11-25 23:12:57 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.044 |  |
| 2026-11-25 23:03:34 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | -0.045 |  |
| 2026-11-26 00:02:48 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.061 |  |
| 2026-11-25 23:06:42 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.064 |  |
| 2026-11-25 23:00:45 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.110 |  |
| 2026-11-26 00:02:17 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)