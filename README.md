# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_18:23:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 18:23:49 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.007 |  |
| 2026-11-01 18:14:39 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:07:36 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-01 18:06:14 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-11-01 18:05:54 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-01 18:05:40 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-01 18:05:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-01 18:04:59 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:04:32 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:03:56 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 18:03:29 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-01 18:03:26 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 18:02:39 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:02:36 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 18:02:34 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-01 18:02:29 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-01 18:02:28 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.112 |  |
| 2026-11-01 18:02:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:02:26 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-01 18:02:20 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:02:14 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 18:02:02 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-11-01 18:02:01 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-01 18:02:01 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-01 18:01:56 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:51 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 18:01:44 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:32 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-01 18:01:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-11-01 18:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 18:01:20 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:00 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.022 |  |
| 2026-11-01 18:00:52 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 18:00:30 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:00:17 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.136 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 18:23:49 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.007 |  |
| 2026-11-01 18:05:54 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-01 18:05:40 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-01 18:02:01 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-01 18:02:26 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-01 18:02:34 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-01 18:02:01 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-01 18:07:36 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-01 18:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 18:00:52 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 18:03:56 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 18:01:51 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 18:02:36 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 18:02:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:00:30 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:11 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:14:39 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:02:39 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:44 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:56 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:04:59 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:20 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:03:29 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-01 18:02:20 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-01 18:05:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-01 18:02:02 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-11-01 18:02:29 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-01 18:03:26 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-11-01 18:01:32 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-01 18:06:14 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-11-01 18:01:00 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.022 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:02:14 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-11-01 18:01:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-11-01 18:02:28 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.112 |  |
| 2026-11-01 18:00:17 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)