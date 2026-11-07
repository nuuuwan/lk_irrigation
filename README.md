# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_16:25:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 16:25:02 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:20:14 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-07 16:16:09 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.071 |  |
| 2026-11-07 16:14:56 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:10:02 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:09:24 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-07 16:08:36 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 16:08:16 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-11-07 16:07:49 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.104 |  |
| 2026-11-07 16:07:37 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-07 16:07:25 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-07 16:06:56 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-11-07 16:06:19 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.029 |  |
| 2026-11-07 16:05:54 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 16:05:32 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.058 |  |
| 2026-11-07 16:05:12 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.125 |  |
| 2026-11-07 16:04:45 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 16:04:33 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:04:23 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-07 16:04:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 16:04:06 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.106 |  |
| 2026-11-07 16:04:02 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | -0.040 |  |
| 2026-11-07 16:03:53 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-07 16:03:38 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:03:30 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:03:10 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-07 16:02:49 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-11-07 16:02:35 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | -0.041 |  |
| 2026-11-07 16:02:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:02:04 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.089 |  |
| 2026-11-07 16:01:37 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-07 16:01:32 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:01:32 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:01:16 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 16:00:44 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 16:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.020 |  |
| 2026-11-07 16:02:35 | Dunamale (Aththanagalu Oya) | 3.64 | 🟡 Alert | -0.041 |  |
| 2026-11-07 16:07:37 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-07 16:01:37 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-07 16:07:25 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-07 16:03:10 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-07 16:04:23 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-07 16:01:16 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 16:04:45 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 16:20:14 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-07 16:05:54 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 16:08:36 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 16:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 16:04:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:04:33 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:10:02 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:14:56 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:01:32 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:25:02 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 16:08:16 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-11-07 16:06:56 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-11-07 16:02:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:00:44 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-11-07 16:01:32 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-11-07 15:05:21 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-11-07 16:03:53 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:03:30 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:02:04 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:03:38 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-07 16:06:19 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.029 |  |
| 2026-11-07 16:02:49 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-11-07 16:09:24 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-07 16:04:02 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | -0.040 |  |
| 2026-11-07 16:05:32 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.058 |  |
| 2026-11-07 16:16:09 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.071 |  |
| 2026-11-07 16:01:40 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.089 |  |
| 2026-11-07 16:07:49 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.104 |  |
| 2026-11-07 16:04:06 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.106 |  |
| 2026-11-07 16:05:12 | Hanwella (Kelani Ganga) | 3.57 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)