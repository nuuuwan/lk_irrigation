# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_16:23:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 16:23:04 | Panadugama (Nilwala Ganga) | 5.63 | 🟡 Alert | -0.054 |  |
| 2026-11-08 16:22:31 | Ellagawa (Kalu Ganga) | 7.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-08 16:16:32 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:16:10 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:16:07 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:15:21 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:14:00 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-08 16:13:24 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.035 |  |
| 2026-11-08 16:10:04 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-08 16:09:58 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:08:39 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 16:07:27 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-08 16:07:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-08 16:07:03 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.135 |  |
| 2026-11-08 16:06:50 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.109 |  |
| 2026-11-08 16:06:06 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.038 |  |
| 2026-11-08 16:06:04 | Rathnapura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.096 |  |
| 2026-11-08 16:05:11 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | -0.029 |  |
| 2026-11-08 16:05:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-08 16:05:00 | Peradeniya (Mahaweli Ganga) | 3.17 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2026-11-08 16:04:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-08 16:04:32 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-11-08 16:04:32 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:04:29 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-11-08 16:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-11-08 16:04:24 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:04:17 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 16:04:09 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-11-08 16:04:06 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:03:54 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:03:34 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-08 16:03:21 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.069 |  |
| 2026-11-08 16:03:17 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:02:56 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:02:47 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:02:32 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 16:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-08 16:02:11 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:01:44 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.070 |  |
| 2026-11-08 16:01:41 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.021 |  |
| 2026-11-08 16:01:28 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:01:24 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-11-08 16:00:43 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 16:07:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-08 16:10:04 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-11-08 16:01:41 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.021 |  |
| 2026-11-08 16:13:24 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.035 |  |
| 2026-11-08 16:23:04 | Panadugama (Nilwala Ganga) | 5.63 | 🟡 Alert | -0.054 |  |
| 2026-11-08 16:05:00 | Peradeniya (Mahaweli Ganga) | 3.17 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2026-11-08 16:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-08 16:04:29 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-11-08 16:07:27 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-08 16:05:04 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-08 16:03:34 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-08 16:22:31 | Ellagawa (Kalu Ganga) | 7.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-08 16:02:32 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 16:04:17 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 16:04:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-08 16:08:39 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 16:14:00 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-08 16:03:17 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:16:10 | Moragaswewa (Deduru Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:04:24 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:16:32 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:02:47 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-11-08 15:07:50 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:09:58 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:01:28 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-08 16:02:56 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:02:11 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-08 16:01:24 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.011 |  |
| 2026-11-08 16:00:43 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-11-08 16:05:11 | Giriulla (Maha Oya) | 2.47 | 🟢 Normal | -0.029 |  |
| 2026-11-08 16:04:25 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-11-08 16:06:06 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.038 |  |
| 2026-11-08 16:04:09 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-11-08 16:04:32 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-11-08 16:03:21 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.069 |  |
| 2026-11-08 16:01:44 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.070 |  |
| 2026-11-08 16:06:04 | Rathnapura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.096 |  |
| 2026-11-08 16:06:50 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.109 |  |
| 2026-11-08 16:07:03 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)