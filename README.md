# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_17:11:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,351 measurements** from **39** stations.
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
| 2026-11-18 17:11:12 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:09:58 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:08:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:08:30 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 17:08:25 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:07:04 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:06:43 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:06:29 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | -0.041 |  |
| 2026-11-18 17:06:03 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:06:03 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.010 |  |
| 2026-11-18 17:05:02 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-11-18 17:04:33 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-11-18 17:04:29 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-11-18 17:04:16 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-18 17:04:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 17:03:40 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-11-18 17:03:37 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:03:17 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:02:54 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 17:02:50 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-18 17:02:46 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | -0.033 |  |
| 2026-11-18 17:02:42 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:02:36 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-11-18 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.108 |  |
| 2026-11-18 17:02:31 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-18 17:02:25 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 17:02:21 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.016 |  |
| 2026-11-18 17:02:19 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-18 17:02:11 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:02:09 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:02:09 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 17:01:59 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:01:52 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:01:31 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.013 |  |
| 2026-11-18 17:01:28 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:01:10 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:00:25 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:00:15 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.109 |  |
| 2026-11-18 17:00:09 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 17:04:16 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-18 17:02:19 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-18 17:02:25 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 17:04:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 17:02:31 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-18 17:08:30 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-18 17:02:09 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 17:01:10 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:01:28 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:03:37 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:06:43 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:02:09 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:00:09 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:08:37 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:01:52 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:02:42 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:07:04 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:00:25 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:06:03 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:02:11 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:03:17 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:01:59 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:08:25 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:11:12 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 17:06:03 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.010 |  |
| 2026-11-18 17:02:50 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-18 17:02:54 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 17:04:29 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-11-18 17:03:40 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2026-11-18 17:01:31 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.013 |  |
| 2026-11-18 17:02:21 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.016 |  |
| 2026-11-18 17:04:33 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-11-18 17:05:02 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-11-18 17:02:36 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-11-18 17:02:46 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | -0.033 |  |
| 2026-11-18 17:06:29 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | -0.041 |  |
| 2026-11-18 17:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.108 |  |
| 2026-11-18 17:00:15 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)