# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_08:20:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,337 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 08:20:50 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-11-05 08:20:42 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-05 08:17:25 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.097 |  |
| 2026-11-05 08:15:45 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.005 |  |
| 2026-11-05 08:13:02 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.005 |  |
| 2026-11-05 08:12:51 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-11-05 08:12:15 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.055 |  |
| 2026-11-05 08:11:10 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-05 08:10:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:07:10 | Moragaswewa (Deduru Oya) | 3.67 | 🟢 Normal | -0.029 |  |
| 2026-11-05 08:07:04 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.088 |  |
| 2026-11-05 08:05:57 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.084 |  |
| 2026-11-05 08:05:50 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:05:37 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 08:05:04 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-11-05 08:04:40 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:04:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:04:32 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 08:04:22 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-05 08:04:08 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.020 |  |
| 2026-11-05 08:03:49 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.052 |  |
| 2026-11-05 08:03:46 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | -0.022 |  |
| 2026-11-05 08:03:36 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:02:55 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-11-05 08:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-05 08:02:19 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-05 08:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:02:16 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-05 08:02:09 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:02:01 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-11-05 08:01:57 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.087 |  |
| 2026-11-05 08:01:52 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.309 |  |
| 2026-11-05 08:01:44 | Thanamalwila (Kirindi Oya) | 2.24 | 🟢 Normal | -0.061 |  |
| 2026-11-05 08:01:42 | Giriulla (Maha Oya) | 2.39 | 🟢 Normal | -0.070 |  |
| 2026-11-05 08:01:39 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.032 |  |
| 2026-11-05 08:01:21 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-11-05 08:01:01 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:00:16 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 08:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-05 08:01:21 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-11-05 08:20:42 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-05 08:04:22 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-05 08:11:10 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-05 08:04:32 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 08:05:37 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 08:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:04:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:03:36 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:05:50 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:04:40 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:02:09 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:10:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:00:16 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:01:01 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:13:02 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.005 |  |
| 2026-11-05 08:15:45 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.005 |  |
| 2026-11-05 08:12:51 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-11-05 08:02:19 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-11-05 08:02:01 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-11-05 08:05:04 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-11-05 08:04:08 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.020 |  |
| 2026-11-05 08:02:16 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-05 08:03:46 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | -0.022 |  |
| 2026-11-05 08:07:10 | Moragaswewa (Deduru Oya) | 3.67 | 🟢 Normal | -0.029 |  |
| 2026-11-05 08:20:50 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-11-05 08:01:39 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.032 |  |
| 2026-11-05 08:02:55 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-11-05 08:03:49 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.052 |  |
| 2026-11-05 08:12:15 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.055 |  |
| 2026-11-05 07:04:11 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.058 |  |
| 2026-11-05 08:01:44 | Thanamalwila (Kirindi Oya) | 2.24 | 🟢 Normal | -0.061 |  |
| 2026-11-05 08:01:42 | Giriulla (Maha Oya) | 2.39 | 🟢 Normal | -0.070 |  |
| 2026-11-05 08:05:57 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.084 |  |
| 2026-11-05 08:01:57 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.087 |  |
| 2026-11-05 08:07:04 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.088 |  |
| 2026-11-05 08:17:25 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.097 |  |
| 2026-11-05 08:01:52 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.309 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)