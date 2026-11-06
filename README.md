# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_17:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,584 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 17:03:03 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:02:55 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-11-06 17:02:54 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:02:51 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-06 17:02:50 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.062 |  |
| 2026-11-06 17:02:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-11-06 17:02:14 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 17:01:49 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.047 |  |
| 2026-11-06 17:01:45 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.020 |  |
| 2026-11-06 17:01:42 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-11-06 17:01:35 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:01:27 | Moragaswewa (Deduru Oya) | 2.51 | 🟢 Normal | -0.074 |  |
| 2026-11-06 17:01:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-06 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:01:04 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-06 17:00:57 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-06 17:00:14 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-11-06 16:21:20 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 17:02:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-11-06 17:02:55 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-11-06 17:01:42 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-11-06 17:00:57 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-06 17:01:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-06 17:01:04 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-06 16:07:11 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-06 15:04:06 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 16:13:57 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-06 16:00:56 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 16:03:24 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 17:01:35 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:03:10 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:02:54 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:05:32 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:04:40 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:16:04 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:03 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:01:45 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:11:20 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 16:16:27 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:02:14 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 16:05:00 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-11-06 16:03:36 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-11-06 16:06:40 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.019 |  |
| 2026-11-06 17:01:45 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.020 |  |
| 2026-11-06 16:02:27 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-06 17:02:51 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-06 16:10:21 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.028 |  |
| 2026-11-06 16:02:49 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-11-06 17:00:14 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-11-06 16:21:20 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-11-06 17:01:49 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.047 |  |
| 2026-11-06 16:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.051 |  |
| 2026-11-06 16:08:58 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.054 |  |
| 2026-11-06 17:02:50 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.062 |  |
| 2026-11-06 17:01:27 | Moragaswewa (Deduru Oya) | 2.51 | 🟢 Normal | -0.074 |  |
| 2026-11-06 16:05:01 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)