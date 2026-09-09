# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_10:07:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,068 measurements** from **39** stations.
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
| 2026-09-09 10:07:27 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:07:09 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-09 10:06:19 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:05:43 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:05:40 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:04:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:04:48 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 10:04:34 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:04:20 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 10:03:47 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:03:47 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:03:20 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.053 |  |
| 2026-09-09 10:03:16 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:03:06 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-09 10:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-09 10:02:57 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.070 |  |
| 2026-09-09 10:02:57 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-09 10:02:52 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:02:43 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-09 10:02:40 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 10:02:38 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:02:30 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:02:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:02:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:02:20 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:01:48 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-09-09 10:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:01:13 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:01:04 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:00:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-09 10:00:42 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:00:22 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.106 |  |
| 2026-09-09 10:00:16 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 10:00:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-09 10:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-09 10:07:09 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-09 10:02:57 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-09 10:03:06 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-09 09:07:33 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-09 10:02:43 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-09 10:04:20 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 09:04:25 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 10:02:40 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 10:04:48 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 10:00:16 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:02:20 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:00:42 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:06:19 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:01:04 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:03:47 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:04:34 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:06:10 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:01:13 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:02:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:05:40 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:02:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:04:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:20 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:11:22 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:05:43 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 10:02:52 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:07:27 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:03:47 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:02:38 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:03:16 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:02:30 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.010 |  |
| 2026-09-09 10:01:48 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.020 |  |
| 2026-09-09 09:04:19 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.048 |  |
| 2026-09-09 10:03:20 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.053 |  |
| 2026-09-09 10:02:57 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.070 |  |
| 2026-09-09 10:00:22 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)