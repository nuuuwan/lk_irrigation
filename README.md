# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_02:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,909 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 02:02:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-11-07 02:02:48 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 02:02:40 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.033 |  |
| 2026-11-07 02:02:22 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-11-07 02:02:13 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-07 02:02:11 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-07 02:02:08 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-07 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.098 |  |
| 2026-11-07 02:02:01 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-11-07 02:01:56 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.162 |  |
| 2026-11-07 02:01:52 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-11-07 02:01:44 | Glencourse (Kelani Ganga) | 12.78 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-11-07 02:01:36 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -324.000 |  |
| 2026-11-07 02:01:35 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -324.000 |  |
| 2026-11-07 02:00:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 02:00:25 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:50:11 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-11-07 01:42:16 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:35:17 | Giriulla (Maha Oya) | 3.29 | 🟢 Normal | -0.110 |  |
| 2026-11-07 01:23:08 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.031 |  |
| 2026-11-07 01:18:54 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.056 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 01:06:26 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.171 | 🔺 Rising |
| 2026-11-07 02:00:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-07 01:09:00 | Holombuwa (Kelani Ganga) | 3.32 | 🟡 Alert | -0.562 |  |
| 2026-11-07 02:02:22 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.459 | 🔺 Rising |
| 2026-11-07 02:01:44 | Glencourse (Kelani Ganga) | 12.78 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-07 02:02:13 | Badalgama (Maha Oya) | 3.68 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-11-07 01:10:04 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-07 02:02:08 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 01:05:44 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 01:04:06 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 01:04:16 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 00:03:36 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 02:02:48 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 01:09:20 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 02:00:25 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:33 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:24 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:42:16 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:36 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:00:17 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:03:58 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:11:30 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.009 |  |
| 2026-11-07 01:50:11 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-11-07 01:02:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2026-11-07 02:02:11 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-07 02:01:52 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-11-07 02:02:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-11-07 02:02:01 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-11-07 02:02:40 | Rathnapura (Kalu Ganga) | 3.32 | 🟢 Normal | -0.033 |  |
| 2026-11-07 01:02:44 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-11-07 01:04:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-07 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.098 |  |
| 2026-11-07 01:35:17 | Giriulla (Maha Oya) | 3.29 | 🟢 Normal | -0.110 |  |
| 2026-11-07 02:01:56 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.162 |  |
| 2026-11-07 02:01:36 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)