# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_04:07:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 04:07:11 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-09 04:06:31 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:06:15 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.114 |  |
| 2026-10-09 04:05:08 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-09 04:05:00 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.112 |  |
| 2026-10-09 04:04:36 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.129 |  |
| 2026-10-09 04:04:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:04:11 | Badalgama (Maha Oya) | 4.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-10-09 04:04:10 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | -0.109 |  |
| 2026-10-09 04:04:03 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 04:03:45 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-09 04:03:09 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 04:02:55 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-09 04:02:43 | Moragaswewa (Deduru Oya) | 1.87 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-09 04:02:33 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-09 04:02:30 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-09 04:02:25 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-09 04:01:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-09 04:01:50 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:01:20 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.033 |  |
| 2026-10-09 04:01:11 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.051 |  |
| 2026-10-09 04:01:10 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-09 04:01:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:00:50 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-09 04:00:45 | Glencourse (Kelani Ganga) | 12.52 | 🟢 Normal | -0.084 |  |
| 2026-10-09 03:46:06 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 04:02:43 | Moragaswewa (Deduru Oya) | 1.87 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-09 04:04:11 | Badalgama (Maha Oya) | 4.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-10-09 04:02:30 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-09 04:05:08 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-09 04:02:55 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-09 03:07:51 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-09 04:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-09 03:46:06 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-09 04:04:03 | Baddegama (Gin Ganga) | 2.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-09 04:07:11 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-09 04:01:10 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-09 03:07:40 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-09 04:00:50 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-09 04:03:09 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-09 03:04:30 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:01:20 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:01:50 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:01:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:01:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:04:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:06:31 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-09 04:02:33 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-09 04:02:25 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-09 04:03:45 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-09 03:03:06 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-10-09 03:09:00 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.018 |  |
| 2026-10-09 03:01:52 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-09 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.033 |  |
| 2026-10-09 04:01:11 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.051 |  |
| 2026-10-09 04:00:45 | Glencourse (Kelani Ganga) | 12.52 | 🟢 Normal | -0.084 |  |
| 2026-10-09 03:07:22 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.105 |  |
| 2026-10-09 04:04:10 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | -0.109 |  |
| 2026-10-09 04:05:00 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.112 |  |
| 2026-10-09 04:06:15 | Holombuwa (Kelani Ganga) | 1.92 | 🟢 Normal | -0.114 |  |
| 2026-10-09 04:04:36 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.129 |  |
| 2026-10-09 03:02:33 | Giriulla (Maha Oya) | 4.57 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)