# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_17:36:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,132 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Rathnapura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 17:36:25 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-21 17:14:23 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-21 17:14:20 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.018 |  |
| 2026-09-21 17:09:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-09-21 17:08:47 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.029 |  |
| 2026-09-21 17:08:43 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:08:20 | Ellagawa (Kalu Ganga) | 9.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:07:03 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-21 17:06:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:06:23 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:05:46 | Panadugama (Nilwala Ganga) | 5.51 | 🟡 Alert | -0.029 |  |
| 2026-09-21 17:05:35 | Magura (Kalu Ganga) | 5.33 | 🟡 Alert | -0.054 |  |
| 2026-09-21 17:05:05 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-09-21 17:04:56 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-21 17:04:23 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 17:04:21 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.040 |  |
| 2026-09-21 17:04:03 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:04:00 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-09-21 17:03:44 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-09-21 17:03:44 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:03:37 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-21 17:03:29 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 17:03:07 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.099 |  |
| 2026-09-21 17:03:01 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-21 17:02:58 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.022 |  |
| 2026-09-21 17:02:49 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-09-21 17:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-21 17:02:31 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-21 17:02:17 | Hanwella (Kelani Ganga) | 5.58 | 🟢 Normal | -0.104 |  |
| 2026-09-21 17:02:12 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2026-09-21 17:02:00 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.066 |  |
| 2026-09-21 17:01:47 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:01:31 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-09-21 17:01:29 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:01:27 | Peradeniya (Mahaweli Ganga) | 3.67 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-21 17:01:25 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-09-21 17:01:18 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.032 | 🔺 Rising |
| 2026-09-21 17:07:03 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-21 17:05:05 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-09-21 17:14:20 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.018 |  |
| 2026-09-21 17:05:46 | Panadugama (Nilwala Ganga) | 5.51 | 🟡 Alert | -0.029 |  |
| 2026-09-21 17:05:35 | Magura (Kalu Ganga) | 5.33 | 🟡 Alert | -0.054 |  |
| 2026-09-21 17:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-21 17:01:27 | Peradeniya (Mahaweli Ganga) | 3.67 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-21 17:03:37 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-21 17:04:56 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-21 17:36:25 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-21 17:03:29 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 17:14:23 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-09-21 17:03:01 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-21 17:04:23 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 17:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:01:47 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:08:43 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:08:20 | Ellagawa (Kalu Ganga) | 9.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:06:23 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:06:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:02:12 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:03:44 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:04:03 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:01:18 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:01:29 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-21 17:09:17 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-09-21 17:02:31 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-21 17:01:31 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-09-21 17:01:25 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-09-21 17:02:58 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.022 |  |
| 2026-09-21 17:08:47 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.029 |  |
| 2026-09-21 17:04:00 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.030 |  |
| 2026-09-21 17:02:49 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.030 |  |
| 2026-09-21 17:03:44 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-09-21 17:04:21 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.040 |  |
| 2026-09-21 17:02:00 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.066 |  |
| 2026-09-21 17:03:07 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.099 |  |
| 2026-09-21 17:02:17 | Hanwella (Kelani Ganga) | 5.58 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)