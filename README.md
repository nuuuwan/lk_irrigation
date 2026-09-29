# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_11:25:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,103 measurements** from **39** stations.
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
| 2026-09-29 11:25:03 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-09-29 11:16:49 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.009 |  |
| 2026-09-29 11:15:22 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-09-29 11:10:52 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.054 |  |
| 2026-09-29 11:10:38 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:09:12 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:08:55 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:08:47 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 11:08:31 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:05:59 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:05:45 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.212 |  |
| 2026-09-29 11:05:41 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:05:38 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.047 |  |
| 2026-09-29 11:04:41 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:04:21 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:03:50 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -0.028 |  |
| 2026-09-29 11:03:45 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:03:34 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | -0.031 |  |
| 2026-09-29 11:03:22 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:03:18 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:03:13 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-29 11:03:10 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:02:56 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:02:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:02:20 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:02:17 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.141 |  |
| 2026-09-29 11:02:15 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-09-29 11:02:10 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-29 11:02:05 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:01:57 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:01:47 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:01:15 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.096 |  |
| 2026-09-29 11:00:36 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:00:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:32 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:22 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:15 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-09-29 11:00:10 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:07 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 11:02:10 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-29 11:03:13 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-29 11:08:47 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 11:01:57 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:10:38 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:02:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:08:31 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:04:41 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:04:21 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:02:56 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:03:18 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:02:05 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:32 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:05:41 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:10 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:03:22 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:02:20 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:03:50 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:09:12 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:00:22 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:01:47 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-29 11:16:49 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.009 |  |
| 2026-09-29 11:03:10 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:03:45 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:00:36 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:05:59 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-29 11:00:15 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-09-29 11:02:15 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-09-29 11:00:07 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-09-29 11:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | -0.028 |  |
| 2026-09-29 11:15:22 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-09-29 11:03:34 | Baddegama (Gin Ganga) | 3.16 | 🟢 Normal | -0.031 |  |
| 2026-09-29 11:25:03 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.038 |  |
| 2026-09-29 11:05:38 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.047 |  |
| 2026-09-29 11:10:52 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.054 |  |
| 2026-09-29 11:01:15 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.096 |  |
| 2026-09-29 11:02:17 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.141 |  |
| 2026-09-29 11:05:45 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)