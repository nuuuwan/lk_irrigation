# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_21:25:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,095 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 21:25:56 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-09-23 21:24:47 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:22:40 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-09-23 21:10:27 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:08:19 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-23 21:08:11 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | -0.028 |  |
| 2026-09-23 21:08:05 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:07:01 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-23 21:06:44 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-09-23 21:06:13 | Baddegama (Gin Ganga) | 3.67 | 🟡 Alert | 0.000 |  |
| 2026-09-23 21:06:08 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 21:06:04 | Rathnapura (Kalu Ganga) | 4.23 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-23 21:05:48 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.030 |  |
| 2026-09-23 21:05:36 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-09-23 21:05:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:04:57 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 21:04:41 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-23 21:04:37 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:04:18 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:04:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:04:02 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-23 21:03:52 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-23 21:03:38 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:03:28 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:03:12 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:03:05 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 21:02:55 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 21:02:48 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.039 |  |
| 2026-09-23 21:02:38 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:02:20 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 21:02:18 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:02:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.105 |  |
| 2026-09-23 21:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.85 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 21:01:22 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:00:16 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 21:00:11 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 21:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.85 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 21:06:13 | Baddegama (Gin Ganga) | 3.67 | 🟡 Alert | 0.000 |  |
| 2026-09-23 21:25:56 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-09-23 21:07:01 | Peradeniya (Mahaweli Ganga) | 3.77 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-09-23 21:04:41 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-23 21:08:19 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-23 21:03:52 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-23 21:06:04 | Rathnapura (Kalu Ganga) | 4.23 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-23 21:04:02 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-23 21:03:05 | Glencourse (Kelani Ganga) | 12.56 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 21:06:08 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 21:02:20 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 21:02:55 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 21:00:16 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 21:04:57 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 20:04:03 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:04:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:02:38 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:01:22 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:04:18 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:24:47 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:08:05 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:02:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:03:28 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:05:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:04:37 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:03:38 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:02:18 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 21:06:44 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-09-23 21:05:36 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-09-23 21:00:11 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 21:08:11 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | -0.028 |  |
| 2026-09-23 21:05:48 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.030 |  |
| 2026-09-23 21:02:48 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.039 |  |
| 2026-09-23 21:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)