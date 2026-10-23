# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_14:11:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,842 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 14:11:58 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-10-23 14:11:41 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:11:06 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-23 14:10:18 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | -0.018 |  |
| 2026-10-23 14:08:30 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-10-23 14:08:13 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:07:44 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-10-23 14:07:25 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:06:38 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.010 |  |
| 2026-10-23 14:06:22 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-10-23 14:04:52 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:04:48 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.030 |  |
| 2026-10-23 14:04:45 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-10-23 14:04:11 | Moragaswewa (Deduru Oya) | 4.66 | 🟢 Normal | -0.039 |  |
| 2026-10-23 14:04:04 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.028 |  |
| 2026-10-23 14:03:33 | Ellagawa (Kalu Ganga) | 7.51 | 🟢 Normal | -0.049 |  |
| 2026-10-23 14:03:06 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 14:03:03 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-23 14:03:01 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-23 14:02:59 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 14:02:57 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-23 14:02:56 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-10-23 14:02:55 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.030 |  |
| 2026-10-23 14:02:54 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-23 14:02:37 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.157 |  |
| 2026-10-23 14:02:22 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-23 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.051 |  |
| 2026-10-23 14:02:16 | Thanthirimale (Malwathu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:02:12 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:01:45 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.041 |  |
| 2026-10-23 14:01:38 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:01:33 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-23 14:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 14:01:09 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.046 |  |
| 2026-10-23 14:01:08 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-10-23 14:00:28 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 14:01:33 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-23 14:03:01 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-23 14:02:54 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-23 14:11:06 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-23 14:03:06 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 14:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 14:02:59 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 14:08:13 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-23 13:06:22 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:04:52 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:01:38 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:02:16 | Thanthirimale (Malwathu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:11:41 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:07:25 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:02:12 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-23 14:11:58 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-10-23 14:06:38 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.010 |  |
| 2026-10-23 14:03:03 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-23 14:02:57 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-23 14:04:45 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.011 |  |
| 2026-10-23 14:00:28 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.015 |  |
| 2026-10-23 14:07:44 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-10-23 14:10:18 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | -0.018 |  |
| 2026-10-23 14:02:22 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-23 14:01:08 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-10-23 13:20:16 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.023 |  |
| 2026-10-23 14:04:04 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.028 |  |
| 2026-10-23 14:04:48 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.030 |  |
| 2026-10-23 14:02:55 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.030 |  |
| 2026-10-23 14:08:30 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-10-23 14:04:11 | Moragaswewa (Deduru Oya) | 4.66 | 🟢 Normal | -0.039 |  |
| 2026-10-23 14:01:45 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.041 |  |
| 2026-10-23 14:01:09 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.046 |  |
| 2026-10-23 14:03:33 | Ellagawa (Kalu Ganga) | 7.51 | 🟢 Normal | -0.049 |  |
| 2026-10-23 14:02:56 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.050 |  |
| 2026-10-23 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.051 |  |
| 2026-10-23 14:06:22 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-10-23 13:06:11 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.063 |  |
| 2026-10-23 14:02:37 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)