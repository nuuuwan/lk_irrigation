# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_16:05:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,849 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 16:05:29 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.021 |  |
| 2026-09-03 16:05:28 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:05:24 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.131 |  |
| 2026-09-03 16:05:22 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-03 16:04:31 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:04:28 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-03 16:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 16:03:49 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-03 16:03:32 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 16:03:29 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:28 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:07 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:06 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 16:03:01 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:02:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.062 |  |
| 2026-09-03 16:02:38 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 16:02:35 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-09-03 16:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.042 |  |
| 2026-09-03 16:02:22 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:02:20 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-03 16:02:19 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:01:42 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:01:41 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:01:28 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.052 |  |
| 2026-09-03 16:01:04 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:00:30 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-03 16:00:28 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:56:16 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.100 |  |
| 2026-09-03 15:19:08 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 16:05:22 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-03 15:08:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-03 15:09:38 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-03 15:01:08 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-03 16:02:20 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-03 16:02:38 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 16:03:32 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 16:03:06 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 16:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 16:02:22 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:00:28 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:01:41 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:08:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:02:19 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:01:04 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:28 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:07 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:01 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:30 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:04:31 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:05:28 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:31 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:39 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:00:23 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:01:42 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:29 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:04:28 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-03 16:00:30 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-03 16:03:49 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-09-03 16:02:35 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-09-03 15:04:52 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-09-03 16:05:29 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.021 |  |
| 2026-09-03 15:01:56 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-09-03 16:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.042 |  |
| 2026-09-03 16:01:28 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.052 |  |
| 2026-09-03 16:02:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.062 |  |
| 2026-09-03 15:56:16 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.100 |  |
| 2026-09-03 16:05:24 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.131 |  |
| 2026-09-03 15:04:00 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -2.372 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)