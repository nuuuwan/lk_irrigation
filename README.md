# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_04:17:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,913 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 04:17:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:14:39 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.035 |  |
| 2026-09-18 04:12:06 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.022 |  |
| 2026-09-18 04:11:47 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.138 |  |
| 2026-09-18 04:08:27 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.040 |  |
| 2026-09-18 04:07:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-18 04:07:07 | Baddegama (Gin Ganga) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:05:51 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-09-18 04:05:33 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:05:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:05:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.058 |  |
| 2026-09-18 04:05:16 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:04:19 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.049 |  |
| 2026-09-18 04:04:08 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-18 04:03:39 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:02:41 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | -0.110 |  |
| 2026-09-18 04:02:39 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:02:37 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-18 04:02:08 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 04:02:04 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-09-18 04:01:54 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-09-18 04:01:54 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.168 |  |
| 2026-09-18 04:01:50 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:01:45 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-18 04:01:25 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 04:01:23 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:01:00 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-18 04:00:54 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-18 03:58:26 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 04:02:41 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | -0.110 |  |
| 2026-09-18 02:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-18 04:07:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-18 04:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-18 04:00:54 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-18 04:01:25 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 03:00:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 04:04:08 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-18 04:02:08 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 03:06:21 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:02:39 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:05:16 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:05:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:03:39 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:03:09 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:07:07 | Baddegama (Gin Ganga) | 3.43 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:06:13 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:01:45 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:17:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:01:23 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 03:01:30 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:01:50 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 04:02:37 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-18 04:02:04 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-09-18 04:01:00 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-18 04:01:54 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-09-18 03:33:02 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-09-18 04:05:51 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-09-18 04:12:06 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.022 |  |
| 2026-09-18 02:03:40 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-09-18 04:14:39 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.035 |  |
| 2026-09-18 04:08:27 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.040 |  |
| 2026-09-18 04:04:19 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.049 |  |
| 2026-09-18 04:05:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.058 |  |
| 2026-09-18 04:11:47 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.138 |  |
| 2026-09-18 04:01:54 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)