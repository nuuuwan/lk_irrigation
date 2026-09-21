# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_02:04:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 02:04:46 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.082 |  |
| 2026-09-22 02:04:43 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-09-22 02:04:00 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:03:52 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-09-22 02:03:41 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 02:03:24 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-22 02:03:08 | Hanwella (Kelani Ganga) | 5.12 | 🟢 Normal | -0.154 |  |
| 2026-09-22 02:02:55 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-22 02:02:01 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.070 |  |
| 2026-09-22 02:01:54 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:38 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:33 | Ellagawa (Kalu Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:26 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:00:08 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-22 01:43:39 | Hanwella (Kelani Ganga) | 5.17 | 🟢 Normal | -0.154 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 01:12:38 | Baddegama (Gin Ganga) | 4.15 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-22 00:18:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.13 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 02:02:55 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-22 01:02:29 | Panadugama (Nilwala Ganga) | 5.29 | 🟡 Alert | -0.020 |  |
| 2026-09-22 01:01:08 | Magura (Kalu Ganga) | 5.05 | 🟡 Alert | -0.060 |  |
| 2026-09-22 01:01:10 | Peradeniya (Mahaweli Ganga) | 4.06 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-22 02:03:24 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-22 01:20:54 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-22 02:03:41 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 01:06:50 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 01:22:14 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-22 01:27:51 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:38 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:54 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-22 01:23:49 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:33 | Ellagawa (Kalu Ganga) | 9.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:02:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:04:00 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 01:01:05 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-22 02:01:26 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 00:06:29 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-22 02:03:52 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-09-22 00:08:09 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-22 01:04:48 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.011 |  |
| 2026-09-22 01:08:39 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.018 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-22 01:32:44 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-22 02:00:08 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.021 |  |
| 2026-09-22 02:04:43 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-09-22 01:02:08 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-09-22 02:02:01 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.070 |  |
| 2026-09-22 01:00:46 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.073 |  |
| 2026-09-22 02:04:46 | Rathnapura (Kalu Ganga) | 5.02 | 🟢 Normal | -0.082 |  |
| 2026-09-22 01:02:04 | Glencourse (Kelani Ganga) | 12.67 | 🟢 Normal | -0.117 |  |
| 2026-09-22 02:03:08 | Hanwella (Kelani Ganga) | 5.12 | 🟢 Normal | -0.154 |  |
| 2026-09-22 01:03:17 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.163 |  |

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)