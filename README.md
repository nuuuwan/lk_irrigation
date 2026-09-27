# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_14:08:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 14:08:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:07:47 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-27 14:07:15 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:07:05 | Baddegama (Gin Ganga) | 4.62 | 🟠 Minor Flood | -0.023 |  |
| 2026-09-27 14:06:37 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:06:32 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.048 |  |
| 2026-09-27 14:06:00 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -0.032 |  |
| 2026-09-27 14:05:47 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-09-27 14:05:38 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.084 |  |
| 2026-09-27 14:05:14 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-09-27 14:04:04 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.019 |  |
| 2026-09-27 14:03:59 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-09-27 14:03:58 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:03:56 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | -0.070 |  |
| 2026-09-27 14:03:27 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:03:23 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:02:45 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.102 |  |
| 2026-09-27 14:02:36 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:02:12 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:02:11 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.049 |  |
| 2026-09-27 14:02:08 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-09-27 14:01:39 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:01:37 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:01:32 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:01:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:01:29 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-27 14:01:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:00:48 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 14:00:48 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-09-27 14:00:16 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:00:13 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 14:00:48 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 14:07:05 | Baddegama (Gin Ganga) | 4.62 | 🟠 Minor Flood | -0.023 |  |
| 2026-09-27 14:06:00 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -0.032 |  |
| 2026-09-27 13:08:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.42 | 🟡 Alert | -0.038 |  |
| 2026-09-27 14:03:59 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-09-27 14:07:47 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-27 14:01:29 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-27 14:00:16 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:01:32 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:01:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:08:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:06:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:00:50 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:01:57 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:00:13 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:06:37 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:01:37 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2026-09-27 13:02:29 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:07:15 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:03:27 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:01:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:02:12 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 14:05:47 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-09-27 14:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-09-27 14:02:08 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-09-27 14:00:48 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-09-27 14:04:04 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.019 |  |
| 2026-09-27 14:03:23 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:01:39 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:02:36 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:03:58 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-09-27 14:05:14 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2026-09-27 13:04:08 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-09-27 12:02:11 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.045 |  |
| 2026-09-27 14:06:32 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.048 |  |
| 2026-09-27 14:02:11 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.049 |  |
| 2026-09-27 14:03:56 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | -0.070 |  |
| 2026-09-27 14:05:38 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.084 |  |
| 2026-09-27 14:02:45 | Rathnapura (Kalu Ganga) | 3.20 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)