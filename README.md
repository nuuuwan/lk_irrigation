# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_05:36:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,223 measurements** from **39** stations.
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
| 2026-11-05 05:36:12 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.157 |  |
| 2026-11-05 05:34:12 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:21:46 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.008 |  |
| 2026-11-05 05:20:53 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.157 |  |
| 2026-11-05 05:16:00 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:14:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.017 |  |
| 2026-11-05 05:14:02 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-05 05:12:16 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-05 05:11:56 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.157 |  |
| 2026-11-05 05:09:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-11-05 05:09:09 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.005 |  |
| 2026-11-05 05:08:26 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-05 05:07:47 | Thanamalwila (Kirindi Oya) | 2.31 | 🟢 Normal | -0.439 |  |
| 2026-11-05 05:06:05 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-05 05:05:47 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.145 |  |
| 2026-11-05 05:05:33 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-05 05:05:18 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-11-05 05:05:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 05:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | 0.000 |  |
| 2026-11-05 05:04:44 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-05 05:04:32 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 05:04:19 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.051 |  |
| 2026-11-05 05:04:03 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 05:04:03 | Moragaswewa (Deduru Oya) | 3.79 | 🟢 Normal | -0.103 |  |
| 2026-11-05 05:03:54 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.089 |  |
| 2026-11-05 05:03:42 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.255 |  |
| 2026-11-05 05:03:34 | Urawa (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.121 |  |
| 2026-11-05 05:03:16 | Dunamale (Aththanagalu Oya) | 3.07 | 🟢 Normal | -0.020 |  |
| 2026-11-05 05:02:42 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 05:02:39 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:02:29 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.101 |  |
| 2026-11-05 05:01:14 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | -0.200 |  |
| 2026-11-05 05:01:08 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:00:55 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-11-05 05:00:38 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 05:00:13 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 05:00:08 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 04:59:31 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 05:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | 0.000 |  |
| 2026-11-05 05:06:05 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-05 05:08:26 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-05 05:12:16 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-05 05:00:13 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 05:05:33 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-05 05:04:32 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 05:14:02 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-05 05:00:38 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 05:00:08 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 05:05:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 05:04:44 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-05 05:04:03 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 05:16:00 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:17:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:02:39 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:01:08 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:34:12 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 05:09:09 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.005 |  |
| 2026-11-05 05:21:46 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.008 |  |
| 2026-11-05 05:02:42 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 05:05:18 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-11-05 05:14:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.017 |  |
| 2026-11-05 05:03:16 | Dunamale (Aththanagalu Oya) | 3.07 | 🟢 Normal | -0.020 |  |
| 2026-11-05 05:09:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-05 05:00:55 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 05:04:19 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.051 |  |
| 2026-11-05 05:03:54 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.089 |  |
| 2026-11-05 05:02:29 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.101 |  |
| 2026-11-05 05:04:03 | Moragaswewa (Deduru Oya) | 3.79 | 🟢 Normal | -0.103 |  |
| 2026-11-05 05:03:34 | Urawa (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.121 |  |
| 2026-11-05 05:05:47 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.145 |  |
| 2026-11-05 05:36:12 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.157 |  |
| 2026-11-05 05:01:14 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | -0.200 |  |
| 2026-11-05 05:03:42 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.255 |  |
| 2026-11-05 05:07:47 | Thanamalwila (Kirindi Oya) | 2.31 | 🟢 Normal | -0.439 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)