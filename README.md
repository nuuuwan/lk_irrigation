# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_04:34:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 04:34:05 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 04:19:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:11:46 | Holombuwa (Kelani Ganga) | 2.24 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-09-22 04:09:24 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-22 04:09:07 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-09-22 04:08:44 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | -0.036 |  |
| 2026-09-22 04:08:15 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 04:08:11 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.027 |  |
| 2026-09-22 04:07:32 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | -0.077 |  |
| 2026-09-22 04:07:14 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:06:26 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:06:03 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-22 04:05:58 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-09-22 04:05:32 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:04:30 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.060 |  |
| 2026-09-22 04:03:58 | Glencourse (Kelani Ganga) | 12.32 | 🟢 Normal | -0.119 |  |
| 2026-09-22 04:03:16 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-09-22 04:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.19 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-22 04:03:14 | Hanwella (Kelani Ganga) | 4.93 | 🟢 Normal | -0.100 |  |
| 2026-09-22 04:02:58 | Ellagawa (Kalu Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:02:49 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.031 |  |
| 2026-09-22 04:02:22 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:02:12 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-09-22 04:01:53 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:01:13 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:01:03 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:00:53 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-09-22 04:00:32 | Peradeniya (Mahaweli Ganga) | 4.32 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 04:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.19 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-22 04:09:24 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-22 04:00:53 | Magura (Kalu Ganga) | 4.90 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-09-22 04:34:05 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-09-22 04:08:44 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | -0.036 |  |
| 2026-09-22 04:11:46 | Holombuwa (Kelani Ganga) | 2.24 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-09-22 04:06:03 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-22 04:08:15 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 04:02:12 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 04:01:03 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:19:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:01:53 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:07:14 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:02:58 | Ellagawa (Kalu Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:02:22 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:05:32 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:06:26 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 03:02:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:01:13 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 04:03:16 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | -0.011 |  |
| 2026-09-22 03:06:19 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-09-22 04:09:07 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-09-22 04:05:58 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-22 04:08:11 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.027 |  |
| 2026-09-22 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-09-22 04:02:49 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.031 |  |
| 2026-09-22 04:04:30 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.060 |  |
| 2026-09-22 04:00:32 | Peradeniya (Mahaweli Ganga) | 4.32 | 🟢 Normal | -0.061 |  |
| 2026-09-22 03:09:15 | Rathnapura (Kalu Ganga) | 4.94 | 🟢 Normal | -0.074 |  |
| 2026-09-22 04:07:32 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | -0.077 |  |
| 2026-09-22 04:03:14 | Hanwella (Kelani Ganga) | 4.93 | 🟢 Normal | -0.100 |  |
| 2026-09-22 04:03:58 | Glencourse (Kelani Ganga) | 12.32 | 🟢 Normal | -0.119 |  |
| 2026-09-22 03:03:01 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -2.769 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)