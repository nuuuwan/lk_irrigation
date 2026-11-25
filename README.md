# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_06:12:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 06:12:36 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.066 |  |
| 2026-11-25 06:12:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.133 |  |
| 2026-11-25 06:10:54 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:09:09 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.037 |  |
| 2026-11-25 06:07:04 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-25 06:05:51 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:05:48 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-11-25 06:05:20 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:05:08 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-25 06:05:01 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-25 06:05:00 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | -396.000 |  |
| 2026-11-25 06:04:59 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | -396.000 |  |
| 2026-11-25 06:04:36 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.036 |  |
| 2026-11-25 06:03:54 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 06:03:49 | Glencourse (Kelani Ganga) | 11.54 | 🟢 Normal | -0.280 |  |
| 2026-11-25 06:03:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:03:33 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-25 06:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-11-25 06:03:20 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:02:54 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-25 06:02:47 | Dunamale (Aththanagalu Oya) | 3.74 | 🟡 Alert | -0.043 |  |
| 2026-11-25 06:02:26 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.211 |  |
| 2026-11-25 06:02:19 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.204 |  |
| 2026-11-25 06:02:09 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.109 |  |
| 2026-11-25 06:02:06 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-25 06:02:01 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.051 |  |
| 2026-11-25 06:01:54 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:01:38 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | -0.536 |  |
| 2026-11-25 06:01:21 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-25 06:01:18 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.027 |  |
| 2026-11-25 06:01:05 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | -0.203 |  |
| 2026-11-25 05:46:33 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.054 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 06:02:47 | Dunamale (Aththanagalu Oya) | 3.74 | 🟡 Alert | -0.043 |  |
| 2026-11-25 06:01:05 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | -0.203 |  |
| 2026-11-25 05:14:58 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-11-25 06:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-11-25 06:01:21 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-25 06:05:01 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-25 05:46:33 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-25 04:36:39 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-25 06:07:04 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-25 06:02:06 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-25 06:03:54 | Katharagama (Menik Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 05:00:47 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:02:54 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:03:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:10:54 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:01:54 | Badalgama (Maha Oya) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:03:20 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:05:51 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-25 06:05:08 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-25 05:02:54 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-11-25 06:03:33 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 06:01:18 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.027 |  |
| 2026-11-25 06:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-11-25 06:04:36 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.036 |  |
| 2026-11-25 06:09:09 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.037 |  |
| 2026-11-25 06:05:48 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-11-25 06:02:01 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.051 |  |
| 2026-11-25 06:12:36 | Rathnapura (Kalu Ganga) | 3.93 | 🟢 Normal | -0.066 |  |
| 2026-11-25 06:02:09 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.109 |  |
| 2026-11-25 06:12:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.133 |  |
| 2026-11-25 05:04:07 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | -0.135 |  |
| 2026-11-25 06:02:19 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.204 |  |
| 2026-11-25 06:02:26 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.211 |  |
| 2026-11-25 06:03:49 | Glencourse (Kelani Ganga) | 11.54 | 🟢 Normal | -0.280 |  |
| 2026-11-25 06:01:38 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | -0.536 |  |
| 2026-11-25 06:05:00 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | -396.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)