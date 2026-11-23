# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_06:14:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,337 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 06:14:02 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -5.143 |  |
| 2026-11-23 06:13:41 | Panadugama (Nilwala Ganga) | 4.10 | 🟢 Normal | -5.143 |  |
| 2026-11-23 06:12:53 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -5.143 |  |
| 2026-11-23 06:12:20 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.225 |  |
| 2026-11-23 06:06:53 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.019 |  |
| 2026-11-23 06:06:50 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-23 06:06:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.164 |  |
| 2026-11-23 06:06:23 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:06:13 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-23 06:05:28 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.326 |  |
| 2026-11-23 06:05:08 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-23 06:05:08 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-23 06:05:00 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-23 06:04:25 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:44 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:42 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:39 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.021 |  |
| 2026-11-23 06:03:21 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:21 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:20 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:03 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.097 |  |
| 2026-11-23 06:02:47 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.032 |  |
| 2026-11-23 06:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 1.020 | 🔺 Rising |
| 2026-11-23 06:02:38 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-11-23 06:02:33 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:02:19 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-23 06:02:19 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 06:02:16 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:01:57 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-23 06:01:32 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.103 |  |
| 2026-11-23 06:01:27 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 1.406 | 🔺 Rising |
| 2026-11-23 06:00:55 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-23 06:00:50 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-11-23 06:00:29 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.231 |  |
| 2026-11-23 06:00:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:00:09 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.090 |  |
| 2026-11-23 05:55:03 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 1.406 | 🔺 Rising |
| 2026-11-23 05:48:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 1.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 06:01:27 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 1.406 | 🔺 Rising |
| 2026-11-23 06:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 1.020 | 🔺 Rising |
| 2026-11-23 06:00:50 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-11-23 06:06:50 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-23 06:02:19 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-23 06:06:13 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-23 06:02:19 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-23 06:05:08 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-23 04:02:03 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-23 06:05:00 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-23 06:05:08 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-23 06:02:33 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:00:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:44 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:20 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:21 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:02:16 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:42 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:06:23 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:03:21 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:04:25 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 06:06:53 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.019 |  |
| 2026-11-23 06:02:38 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-11-23 06:01:57 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-11-23 06:00:55 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-11-23 06:03:39 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 06:02:47 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.032 |  |
| 2026-11-23 06:00:09 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.090 |  |
| 2026-11-23 06:03:03 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.097 |  |
| 2026-11-23 06:01:32 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.103 |  |
| 2026-11-23 06:06:45 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.164 |  |
| 2026-11-23 06:12:20 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.225 |  |
| 2026-11-23 06:00:29 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.231 |  |
| 2026-11-23 06:05:28 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.326 |  |
| 2026-11-23 06:14:02 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -5.143 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)