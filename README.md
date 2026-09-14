# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_07:31:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,438 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 07:31:59 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-14 07:23:11 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:20:49 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.041 |  |
| 2026-09-14 07:17:01 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:12:37 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:12:23 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:12:07 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:11:23 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-09-14 07:07:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.294 |  |
| 2026-09-14 07:06:22 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.107 |  |
| 2026-09-14 07:06:07 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.041 |  |
| 2026-09-14 07:05:47 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:05:45 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:05:32 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:05:02 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.079 |  |
| 2026-09-14 07:04:52 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:04:39 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:04:25 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-09-14 07:04:18 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:04:17 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-09-14 07:03:58 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.049 |  |
| 2026-09-14 07:03:45 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-14 07:03:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:03:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.081 |  |
| 2026-09-14 07:03:18 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.031 |  |
| 2026-09-14 07:02:55 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-09-14 07:02:53 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-14 07:02:53 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 07:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.385 |  |
| 2026-09-14 07:02:29 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 07:02:11 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-14 07:01:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:01:51 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-14 07:01:50 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:01:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.124 |  |
| 2026-09-14 07:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:01:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:00:42 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:00:39 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:00:15 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 07:11:23 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-09-14 07:03:45 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-09-14 07:01:51 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-14 07:02:11 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-14 07:02:53 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-14 07:31:59 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-14 07:02:53 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 07:02:29 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 07:17:01 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:12:23 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:01:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:04:18 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:00:42 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:23:11 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:01:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:05:47 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:00:39 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:05:32 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:04:39 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:04:52 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:05:45 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:12:37 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:03:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:01:50 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 07:04:25 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-09-14 07:00:15 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-09-14 06:05:14 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.023 |  |
| 2026-09-14 07:02:55 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-09-14 07:03:18 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.031 |  |
| 2026-09-14 07:04:17 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.031 |  |
| 2026-09-14 07:20:49 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.041 |  |
| 2026-09-14 07:03:58 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.049 |  |
| 2026-09-14 07:05:02 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.079 |  |
| 2026-09-14 07:03:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.081 |  |
| 2026-09-14 07:06:22 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.107 |  |
| 2026-09-14 07:01:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.124 |  |
| 2026-09-14 07:07:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.294 |  |
| 2026-09-14 07:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.385 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)