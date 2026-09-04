# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_15:06:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **251,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 15:06:49 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-04 15:06:23 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 15:05:59 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:05:43 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:05:04 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-04 15:04:51 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-09-04 15:04:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:04:27 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 15:04:18 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.038 |  |
| 2026-09-04 15:04:10 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.046 |  |
| 2026-09-04 15:03:59 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-09-04 15:03:46 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-09-04 15:03:35 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-04 15:03:22 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-09-04 15:03:17 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:03:06 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.040 |  |
| 2026-09-04 15:03:00 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:57 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:40 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:12 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-04 15:02:11 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:09 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-04 15:02:01 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:01:29 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-04 15:01:22 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.074 |  |
| 2026-09-04 15:01:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:01:09 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:00:43 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.130 |  |
| 2026-09-04 15:00:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 15:06:49 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-04 15:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-04 15:03:35 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-04 15:04:27 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 15:06:23 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-04 15:02:57 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:00:08 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-04 14:01:36 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:01:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:40 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:01:29 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:03:00 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 14:08:30 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:04:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:05:43 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:01 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-04 14:11:58 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:11 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:02:09 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:01:09 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:03:17 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-04 14:07:06 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:05:59 | Thanamalwila (Kirindi Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-04 15:04:51 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-09-04 15:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-04 14:01:20 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-04 15:02:12 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | -0.010 |  |
| 2026-09-04 15:03:46 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-09-04 15:03:59 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-09-04 15:05:04 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-04 14:05:53 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-09-04 13:58:07 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-09-04 15:04:18 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.038 |  |
| 2026-09-04 15:03:06 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | -0.040 |  |
| 2026-09-04 15:03:22 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-09-04 15:04:10 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.046 |  |
| 2026-09-04 14:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.049 |  |
| 2026-09-04 15:01:22 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.074 |  |
| 2026-09-04 15:00:43 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)