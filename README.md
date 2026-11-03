# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_11:28:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,651 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 11:28:38 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:19:30 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-11-03 11:12:24 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.086 |  |
| 2026-11-03 11:10:55 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:08:52 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-03 11:08:25 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-11-03 11:06:57 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2026-11-03 11:06:45 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.020 |  |
| 2026-11-03 11:05:33 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.099 |  |
| 2026-11-03 11:05:24 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.078 |  |
| 2026-11-03 11:05:19 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.014 |  |
| 2026-11-03 11:05:06 | Badalgama (Maha Oya) | 3.77 | 🟢 Normal | -0.040 |  |
| 2026-11-03 11:04:47 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-11-03 11:04:03 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.089 |  |
| 2026-11-03 11:03:56 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 11:03:41 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | -0.059 |  |
| 2026-11-03 11:03:35 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.020 |  |
| 2026-11-03 11:03:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 11:03:17 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.019 |  |
| 2026-11-03 11:03:10 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-03 11:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-03 11:03:01 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-03 11:02:57 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-11-03 11:02:39 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-03 11:02:21 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.025 |  |
| 2026-11-03 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:02:13 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 11:01:58 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.329 |  |
| 2026-11-03 11:01:44 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.041 |  |
| 2026-11-03 11:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:01:36 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.094 |  |
| 2026-11-03 11:01:34 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.151 |  |
| 2026-11-03 11:01:25 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.052 |  |
| 2026-11-03 11:01:21 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.084 |  |
| 2026-11-03 11:01:20 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-11-03 11:01:17 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-11-03 11:01:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2026-11-03 11:00:58 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.066 |  |
| 2026-11-03 11:00:37 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 11:06:57 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2026-11-03 11:08:52 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-03 11:03:10 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-03 11:03:19 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 11:02:13 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 11:03:56 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 11:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:28:38 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:10:55 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-11-03 11:03:01 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-03 11:00:37 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-03 11:19:30 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-11-03 11:05:19 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.014 |  |
| 2026-11-03 11:08:25 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.018 |  |
| 2026-11-03 11:03:17 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.019 |  |
| 2026-11-03 11:06:45 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.020 |  |
| 2026-11-03 11:03:35 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.020 |  |
| 2026-11-03 11:02:39 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-11-03 11:01:20 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-11-03 11:02:21 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.025 |  |
| 2026-11-03 11:01:17 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-11-03 11:04:47 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-11-03 11:02:57 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-11-03 11:01:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2026-11-03 11:05:06 | Badalgama (Maha Oya) | 3.77 | 🟢 Normal | -0.040 |  |
| 2026-11-03 11:01:44 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.041 |  |
| 2026-11-03 11:01:25 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.052 |  |
| 2026-11-03 11:03:41 | Weraganthota (Mahaweli Ganga) | -2.11 | 🟢 Normal | -0.059 |  |
| 2026-11-03 11:00:58 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.066 |  |
| 2026-11-03 11:05:24 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.078 |  |
| 2026-11-03 11:01:21 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.084 |  |
| 2026-11-03 11:12:24 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.086 |  |
| 2026-11-03 11:04:03 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.089 |  |
| 2026-11-03 11:01:36 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.094 |  |
| 2026-11-03 11:05:33 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.099 |  |
| 2026-11-03 11:01:34 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.151 |  |
| 2026-11-03 11:01:58 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.329 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)