# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_17:26:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 17:26:20 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:20:10 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.165 |  |
| 2026-11-07 17:17:22 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:15:03 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-07 17:10:31 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | -0.009 |  |
| 2026-11-07 17:09:20 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.028 |  |
| 2026-11-07 17:08:41 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-11-07 17:08:05 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:06:37 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:06:07 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.128 |  |
| 2026-11-07 17:06:03 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.032 |  |
| 2026-11-07 17:06:00 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.036 |  |
| 2026-11-07 17:05:36 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.091 |  |
| 2026-11-07 17:05:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-07 17:05:06 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-07 17:04:28 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:04:27 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -2.250 |  |
| 2026-11-07 17:04:21 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:04:11 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -2.250 |  |
| 2026-11-07 17:03:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:03:36 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-11-07 17:03:26 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:03:25 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:03:25 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 17:03:23 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.040 |  |
| 2026-11-07 17:03:16 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-07 17:02:47 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:38 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.060 |  |
| 2026-11-07 17:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.020 |  |
| 2026-11-07 17:02:26 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-11-07 17:02:11 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-11-07 17:02:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:02:04 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 17:02:04 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:03 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.079 |  |
| 2026-11-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-07 17:01:19 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:01:14 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 17:01:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.165 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 17:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.020 |  |
| 2026-11-07 17:02:38 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.060 |  |
| 2026-11-07 17:15:03 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-07 17:08:41 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-11-07 17:02:11 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-11-07 17:05:06 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-07 17:03:16 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-07 17:01:49 | Pitabeddara (Nilwala Ganga) | 1.56 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-07 17:02:04 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 17:05:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-07 17:03:25 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 17:03:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:04:21 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:08:05 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:26:20 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:47 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:17:22 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:02:04 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:04:28 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:03:25 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:01:14 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:03:26 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 17:10:31 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | -0.009 |  |
| 2026-11-07 17:06:37 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:01:19 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:02:07 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-07 17:03:36 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-11-07 17:09:20 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.028 |  |
| 2026-11-07 17:02:26 | Putupaula (Kalu Ganga) | 1.53 | 🟢 Normal | -0.031 |  |
| 2026-11-07 17:06:03 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.032 |  |
| 2026-11-07 17:06:00 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.036 |  |
| 2026-11-07 17:03:23 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.040 |  |
| 2026-11-07 17:02:03 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.079 |  |
| 2026-11-07 17:05:36 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.091 |  |
| 2026-11-07 17:06:07 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.128 |  |
| 2026-11-07 17:01:05 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.165 |  |
| 2026-11-07 17:20:10 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.165 |  |
| 2026-11-07 17:04:27 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -2.250 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)