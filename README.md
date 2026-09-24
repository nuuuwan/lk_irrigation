# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_05:35:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Thawalama — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 05:35:47 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-24 05:30:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | -0.034 |  |
| 2026-09-24 05:13:31 | Baddegama (Gin Ganga) | 4.02 | 🟠 Minor Flood | 0.055 | 🔺 Rising |
| 2026-09-24 05:13:00 | Rathnapura (Kalu Ganga) | 4.80 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-24 05:12:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:11:45 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 05:11:36 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.474 | 🔺 Rising |
| 2026-09-24 05:09:53 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:08:47 | Nawalapitiya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-09-24 05:08:07 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.083 |  |
| 2026-09-24 05:07:37 | Hanwella (Kelani Ganga) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 05:07:21 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-24 05:06:19 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 05:06:14 | Urawa (Nilwala Ganga) | 3.14 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 05:06:14 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:06:07 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:05:48 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.118 |  |
| 2026-09-24 05:05:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.135 |  |
| 2026-09-24 05:05:40 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-24 05:04:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:04:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:04:44 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:04:13 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.329 |  |
| 2026-09-24 05:03:40 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-24 05:03:04 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:03:03 | Pitabeddara (Nilwala Ganga) | 4.10 | 🟡 Alert | 0.000 |  |
| 2026-09-24 05:02:47 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:02:25 | Glencourse (Kelani Ganga) | 12.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 05:02:24 | Thawalama (Gin Ganga) | 4.89 | 🟡 Alert | 0.111 | 🔺 Rising |
| 2026-09-24 05:02:18 | Pitabeddara (Nilwala Ganga) | 4.10 | 🟡 Alert | 0.000 |  |
| 2026-09-24 05:02:11 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-24 05:02:07 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 05:01:29 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:01:28 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 05:01:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:00:43 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.118 |  |
| 2026-09-24 05:00:39 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 05:00:29 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.110 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 05:13:31 | Baddegama (Gin Ganga) | 4.02 | 🟠 Minor Flood | 0.055 | 🔺 Rising |
| 2026-09-24 05:30:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | -0.034 |  |
| 2026-09-24 05:11:36 | Panadugama (Nilwala Ganga) | 5.74 | 🟡 Alert | 0.474 | 🔺 Rising |
| 2026-09-24 05:02:24 | Thawalama (Gin Ganga) | 4.89 | 🟡 Alert | 0.111 | 🔺 Rising |
| 2026-09-24 05:00:29 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-09-24 05:02:11 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-24 05:06:14 | Urawa (Nilwala Ganga) | 3.14 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 05:03:03 | Pitabeddara (Nilwala Ganga) | 4.10 | 🟡 Alert | 0.000 |  |
| 2026-09-24 05:13:00 | Rathnapura (Kalu Ganga) | 4.80 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-24 05:08:47 | Nawalapitiya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-09-24 05:35:47 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-24 05:02:25 | Glencourse (Kelani Ganga) | 12.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-24 05:11:45 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 05:06:19 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 05:07:21 | Putupaula (Kalu Ganga) | 2.64 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-24 05:02:07 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 05:01:28 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 05:00:39 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 05:07:37 | Hanwella (Kelani Ganga) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 05:03:04 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:12:15 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:01:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:21:42 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:02:47 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:04:50 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:09:53 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:04:51 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:06:07 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:06:14 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 05:01:29 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-24 05:05:40 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-24 05:03:40 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 05:08:07 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.083 |  |
| 2026-09-24 05:05:48 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.118 |  |
| 2026-09-24 05:05:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.135 |  |
| 2026-09-24 05:04:13 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.329 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)