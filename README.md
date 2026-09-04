# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_12:12:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,602 measurements** from **39** stations.
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
| 2026-09-04 12:12:59 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | -0.027 |  |
| 2026-09-04 12:10:58 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:10:24 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:08:38 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.037 |  |
| 2026-09-04 12:07:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-09-04 12:07:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-04 12:06:34 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-09-04 12:06:25 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:06:03 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-04 12:05:26 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-09-04 12:05:22 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:05:19 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:58 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.038 |  |
| 2026-09-04 12:04:50 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-09-04 12:04:38 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:30 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:24 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:13 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:50 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.070 |  |
| 2026-09-04 12:03:44 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:43 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:34 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:34 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 12:03:10 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:50 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:38 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:37 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:36 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:34 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-09-04 12:02:25 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-04 12:02:21 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:01:48 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:01:39 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-04 12:01:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:01:01 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:00:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-09-04 12:00:26 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:00:20 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 12:07:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-04 12:03:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-04 12:01:39 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-04 12:06:03 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-04 12:06:25 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:01:48 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:00:26 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:05:22 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:01:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:10 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:38 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:09:28 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:30 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 11:02:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:13 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:38 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:10:58 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:34 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:04:24 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:36 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:37 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:05:19 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:00:20 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:02:21 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:43 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:34 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:03:44 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 12:07:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-09-04 12:02:25 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-04 12:04:50 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-09-04 12:05:26 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-09-04 12:06:34 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-09-04 12:12:59 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | -0.027 |  |
| 2026-09-04 12:02:34 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-09-04 12:00:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-09-04 12:08:38 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.037 |  |
| 2026-09-04 12:04:58 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.038 |  |
| 2026-09-04 12:03:50 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)