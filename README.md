# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_02:31:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,117 measurements** from **39** stations.
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
| 2026-09-05 02:31:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-09-05 02:16:27 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-05 02:12:31 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:11:08 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-05 02:07:46 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:06:17 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.039 |  |
| 2026-09-05 02:05:53 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.048 |  |
| 2026-09-05 02:05:50 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-09-05 02:04:59 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:03:28 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-05 02:03:09 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:03:08 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:02:37 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-05 02:02:37 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-09-05 02:02:37 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:02:29 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 02:02:11 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-05 02:02:07 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:02:00 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:58 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.051 |  |
| 2026-09-05 02:01:47 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:37 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:29 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-09-05 02:01:15 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:13 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:11 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.052 |  |
| 2026-09-05 02:00:39 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 00:45:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-09-05 02:03:28 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-05 02:11:08 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-05 01:24:11 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-05 02:02:37 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-05 02:02:11 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-05 02:02:29 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-05 02:16:27 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-05 02:02:07 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:00:39 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:00:53 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:02:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:47 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:12:31 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:03:45 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:21:49 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:37 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:36:09 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:03:09 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:15 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 01:31:34 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:02:00 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:02:37 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:07:46 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:04:59 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:02:31 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:07:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:01:13 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-05 00:05:31 | Thanamalwila (Kirindi Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-05 02:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-05 02:01:29 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-09-05 02:02:37 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-09-05 02:05:50 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-09-05 02:31:22 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-09-05 02:06:17 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.039 |  |
| 2026-09-05 02:05:53 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.048 |  |
| 2026-09-05 02:01:58 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.051 |  |
| 2026-09-05 02:01:11 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.052 |  |
| 2026-09-04 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)