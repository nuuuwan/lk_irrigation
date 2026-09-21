# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_00:18:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,389 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 00:18:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.13 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 00:16:48 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.090 |  |
| 2026-09-22 00:12:44 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:08:40 | Ellagawa (Kalu Ganga) | 9.04 | 🟢 Normal | -0.029 |  |
| 2026-09-22 00:08:26 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-09-22 00:08:09 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.610 | 🔺 Rising |
| 2026-09-22 00:08:09 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-22 00:07:47 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2026-09-22 00:07:14 | Hanwella (Kelani Ganga) | 5.20 | 🟢 Normal | -0.037 |  |
| 2026-09-22 00:06:32 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-22 00:06:29 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-22 00:06:27 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-22 00:05:36 | Glencourse (Kelani Ganga) | 12.78 | 🟢 Normal | -0.085 |  |
| 2026-09-22 00:05:19 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-22 00:04:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:03:47 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-09-22 00:03:46 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-09-22 00:03:12 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.061 |  |
| 2026-09-22 00:02:53 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.061 |  |
| 2026-09-22 00:02:45 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:41 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:39 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.022 |  |
| 2026-09-22 00:02:35 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 00:02:24 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:15 | Nawalapitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | 0.610 | 🔺 Rising |
| 2026-09-22 00:02:15 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-22 00:02:06 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:01:59 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.057 |  |
| 2026-09-22 00:01:40 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 00:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:01:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:01:12 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | -0.040 |  |
| 2026-09-22 00:01:07 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 00:00:13 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 00:06:32 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-22 00:18:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.13 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 00:07:47 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | 0.052 | 🔺 Rising |
| 2026-09-22 00:02:39 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.022 |  |
| 2026-09-22 00:01:12 | Magura (Kalu Ganga) | 5.11 | 🟡 Alert | -0.040 |  |
| 2026-09-22 00:08:09 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.610 | 🔺 Rising |
| 2026-09-22 00:03:46 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-09-22 00:06:27 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-22 00:02:35 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 00:01:40 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 00:05:19 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-22 00:02:15 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-22 00:01:07 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 22:06:13 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-22 00:01:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:04:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:24 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:45 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:12:44 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:41 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:06 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 23:06:47 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-09-22 00:06:29 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-22 00:08:09 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-22 00:00:13 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.016 |  |
| 2026-09-22 00:08:26 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-22 00:08:40 | Ellagawa (Kalu Ganga) | 9.04 | 🟢 Normal | -0.029 |  |
| 2026-09-22 00:07:14 | Hanwella (Kelani Ganga) | 5.20 | 🟢 Normal | -0.037 |  |
| 2026-09-22 00:03:47 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.051 |  |
| 2026-09-22 00:01:59 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.057 |  |
| 2026-09-22 00:03:12 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.061 |  |
| 2026-09-22 00:02:53 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.061 |  |
| 2026-09-22 00:05:36 | Glencourse (Kelani Ganga) | 12.78 | 🟢 Normal | -0.085 |  |
| 2026-09-22 00:16:48 | Rathnapura (Kalu Ganga) | 5.18 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)