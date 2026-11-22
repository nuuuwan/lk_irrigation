# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_13:02:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 13:02:39 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-22 13:02:36 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.021 |  |
| 2026-11-22 13:02:25 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.023 |  |
| 2026-11-22 13:02:13 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.033 |  |
| 2026-11-22 13:02:08 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.030 |  |
| 2026-11-22 13:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.093 |  |
| 2026-11-22 13:01:58 | Moragaswewa (Deduru Oya) | 3.55 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-22 13:01:33 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:01:33 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 13:01:22 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-11-22 13:00:55 | Manampitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.050 |  |
| 2026-11-22 13:00:53 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:00:37 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-22 13:00:27 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.170 |  |
| 2026-11-22 13:00:09 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:00:05 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:26:48 | Moragaswewa (Deduru Oya) | 3.47 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-22 12:19:11 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 13:01:58 | Moragaswewa (Deduru Oya) | 3.55 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-22 12:04:21 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-22 12:10:58 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-22 12:03:36 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-22 13:01:33 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 13:00:37 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-22 12:07:28 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:00:09 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:01:33 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:00:27 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:03:10 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:07:47 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:00:53 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 13:00:05 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:02:43 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:14:20 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:01:30 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-22 12:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-11-22 13:02:39 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-22 12:08:34 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2026-11-22 12:19:11 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.017 |  |
| 2026-11-22 12:03:56 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-11-22 12:12:22 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2026-11-22 13:01:22 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-11-22 12:03:08 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-11-22 13:02:36 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.021 |  |
| 2026-11-22 13:02:25 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.023 |  |
| 2026-11-22 12:05:00 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.028 |  |
| 2026-11-22 13:02:08 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.030 |  |
| 2026-11-22 12:03:38 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-11-22 13:02:13 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.033 |  |
| 2026-11-22 12:00:34 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.033 |  |
| 2026-11-22 12:09:08 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.039 |  |
| 2026-11-22 12:06:14 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.048 |  |
| 2026-11-22 13:00:55 | Manampitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.050 |  |
| 2026-11-22 13:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.093 |  |
| 2026-11-22 12:04:42 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.130 |  |
| 2026-11-22 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)