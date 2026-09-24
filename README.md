# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_11:07:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 11:07:11 | Thawalama (Gin Ganga) | 5.31 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-24 11:07:03 | Hanwella (Kelani Ganga) | 4.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-24 11:06:56 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | 0.220 | 🔺 Rising |
| 2026-09-24 11:06:26 | Nawalapitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-09-24 11:06:18 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.074 |  |
| 2026-09-24 11:06:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:06:09 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:05:59 | Baddegama (Gin Ganga) | 4.28 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-24 11:05:29 | Kithulgala (Kelani Ganga) | 2.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-09-24 11:05:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:05:05 | Urawa (Nilwala Ganga) | 2.54 | 🟡 Alert | -0.111 |  |
| 2026-09-24 11:05:05 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-24 11:05:03 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 11:04:53 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:04:21 | Panadugama (Nilwala Ganga) | 6.64 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-09-24 11:04:20 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 11:04:16 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-09-24 11:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 11:03:44 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 11:03:07 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:02:47 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 11:02:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:02:16 | Deraniyagala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.546 | 🔺 Rising |
| 2026-09-24 11:02:12 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-24 11:02:10 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-24 11:02:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:01:51 | Magura (Kalu Ganga) | 4.76 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-09-24 11:01:37 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:01:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:00:58 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:00:36 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.020 |  |
| 2026-09-24 11:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 11:05:59 | Baddegama (Gin Ganga) | 4.28 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-24 11:04:21 | Panadugama (Nilwala Ganga) | 6.64 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-09-24 11:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 11:06:56 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | 0.220 | 🔺 Rising |
| 2026-09-24 11:01:51 | Magura (Kalu Ganga) | 4.76 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-09-24 11:07:11 | Thawalama (Gin Ganga) | 5.31 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-24 11:04:16 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-09-24 10:03:14 | Pitabeddara (Nilwala Ganga) | 4.80 | 🟡 Alert | -0.032 |  |
| 2026-09-24 11:05:05 | Urawa (Nilwala Ganga) | 2.54 | 🟡 Alert | -0.111 |  |
| 2026-09-24 11:02:16 | Deraniyagala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.546 | 🔺 Rising |
| 2026-09-24 11:06:26 | Nawalapitiya (Mahaweli Ganga) | 2.94 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-09-24 10:05:10 | Glencourse (Kelani Ganga) | 13.09 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-24 11:05:29 | Kithulgala (Kelani Ganga) | 2.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-09-24 10:04:57 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-24 11:05:05 | Peradeniya (Mahaweli Ganga) | 4.30 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-24 10:03:49 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-24 11:02:12 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-24 11:07:03 | Hanwella (Kelani Ganga) | 4.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-24 11:04:20 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 11:05:03 | Dunamale (Aththanagalu Oya) | 2.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 10:06:24 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 11:02:47 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 11:03:44 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 11:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:06:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:01:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:00:58 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 10:01:43 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:02:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:04:53 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:02:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:06:09 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:01:37 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:03:07 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:05:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 11:02:10 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-24 11:00:36 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.020 |  |
| 2026-09-24 10:05:13 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-09-24 11:06:18 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)