# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_16:21:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,567 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 16:21:20 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-11-06 16:16:27 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:16:04 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:13:57 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-06 16:11:20 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:10:26 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:10:21 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.028 |  |
| 2026-11-06 16:09:36 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:08:58 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.054 |  |
| 2026-11-06 16:08:20 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.732 | 🔺 Rising |
| 2026-11-06 16:07:11 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-06 16:06:47 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 16:06:40 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.019 |  |
| 2026-11-06 16:06:24 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-06 16:06:07 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:05:32 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:05:01 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.090 |  |
| 2026-11-06 16:05:00 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-11-06 16:04:42 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.031 |  |
| 2026-11-06 16:04:40 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:04:40 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | -0.067 |  |
| 2026-11-06 16:04:19 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:04:09 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-06 16:03:38 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-06 16:03:36 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-11-06 16:03:24 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:03:24 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 16:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.051 |  |
| 2026-11-06 16:03:10 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 16:03:10 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:02:49 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-11-06 16:02:38 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-06 16:02:27 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-06 16:02:19 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-11-06 16:01:45 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:01:08 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-06 16:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:00:56 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.140 |  |
| 2026-11-06 16:00:11 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 16:08:20 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.732 | 🔺 Rising |
| 2026-11-06 16:01:08 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-06 16:04:09 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-06 16:07:11 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-06 16:00:11 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-06 15:04:06 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 16:03:10 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 16:13:57 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-06 16:00:56 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 16:03:24 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 16:06:47 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 16:04:19 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:03:10 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:05:32 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:04:40 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:16:04 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:06:07 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:01:45 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:11:20 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:16:27 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:10:26 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:06:24 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-06 16:03:38 | Thanamalwila (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-06 16:05:00 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-11-06 16:03:36 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-11-06 16:06:40 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.019 |  |
| 2026-11-06 16:02:27 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-06 16:02:38 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-06 16:10:21 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.028 |  |
| 2026-11-06 16:02:19 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-11-06 16:04:42 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.031 |  |
| 2026-11-06 16:02:49 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-11-06 16:21:20 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-11-06 16:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.051 |  |
| 2026-11-06 16:08:58 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.054 |  |
| 2026-11-06 16:04:40 | Moragaswewa (Deduru Oya) | 2.58 | 🟢 Normal | -0.067 |  |
| 2026-11-06 16:05:01 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.090 |  |
| 2026-11-06 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)