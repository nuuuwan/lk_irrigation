# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_19:05:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,970 measurements** from **39** stations.
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
| 2026-09-03 19:05:52 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:05:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:05:35 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:04:36 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-03 19:04:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-09-03 19:04:18 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:04:08 | Thanamalwila (Kirindi Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:04:05 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-03 19:03:44 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.010 |  |
| 2026-09-03 19:03:39 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:13 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:55 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-03 19:02:45 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-03 19:02:33 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-03 19:02:32 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:31 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:27 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-03 19:02:24 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:13 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:01:57 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:01:49 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 19:01:15 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-03 19:00:54 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:59:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-03 18:20:45 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 18:02:38 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 10.703 | 🔺 Rising |
| 2026-09-03 19:02:27 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-03 19:02:33 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-03 19:01:15 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-03 18:01:25 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-03 18:04:53 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-03 19:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-03 19:02:55 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-03 18:59:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-03 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-03 19:04:36 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-03 19:01:49 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 19:02:31 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:24 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:05:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:39 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:00:54 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:02:40 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:32 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:10:01 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:05:35 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:01:57 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:04:05 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:05:52 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:13 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:01:11 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:02:13 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:03:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:04:18 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 19:04:08 | Thanamalwila (Kirindi Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-03 18:03:43 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-03 19:03:44 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.010 |  |
| 2026-09-03 19:02:45 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-03 18:04:16 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-09-03 18:01:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-09-03 18:02:27 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |
| 2026-09-03 19:04:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)