# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_04:26:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,594 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 04:26:40 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:25:01 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.007 |  |
| 2026-09-01 04:18:24 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.008 |  |
| 2026-09-01 04:14:17 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-09-01 04:11:40 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-01 04:11:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:11:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-01 04:08:49 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-09-01 04:08:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:07:53 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-09-01 04:07:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:07:01 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:06:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:06:22 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:05:53 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.352 |  |
| 2026-09-01 04:05:37 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-09-01 04:05:36 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-09-01 04:04:43 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:03:50 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:03:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:03:43 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.030 |  |
| 2026-09-01 04:03:24 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 04:03:01 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:02:56 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:02:07 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:01:35 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:01:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.011 |  |
| 2026-09-01 04:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.352 |  |
| 2026-09-01 04:00:15 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:53:32 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.007 |  |
| 2026-09-01 03:50:15 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-09-01 03:49:40 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 04:05:37 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-09-01 04:14:17 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.374 | 🔺 Rising |
| 2026-09-01 00:11:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-09-01 04:11:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-01 02:03:15 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 04:03:24 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 04:03:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:00:15 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:49:40 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:01:35 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:11:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:03:50 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:02:07 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:04:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:07:25 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:03:01 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:08:06 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:39 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:01:30 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:07:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:04:06 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:03:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:04:43 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:26:40 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:02:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:06:22 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 04:25:01 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.007 |  |
| 2026-09-01 03:53:32 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.007 |  |
| 2026-09-01 04:18:24 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.008 |  |
| 2026-09-01 04:11:40 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.009 |  |
| 2026-09-01 03:08:52 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-09-01 04:07:53 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-09-01 04:01:17 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.011 |  |
| 2026-09-01 04:08:49 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-09-01 04:03:43 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.030 |  |
| 2026-09-01 04:05:53 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.352 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)