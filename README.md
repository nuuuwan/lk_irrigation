# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_04:08:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,857 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 04:08:10 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:07:59 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-24 04:06:47 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-08-24 04:06:41 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:06:27 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:06:09 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-08-24 04:06:07 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-08-24 04:05:50 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.012 |  |
| 2026-08-24 04:05:27 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 04:04:04 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 04:03:47 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-08-24 04:03:29 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-24 04:03:23 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 04:03:15 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:02:53 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-24 04:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.043 |  |
| 2026-08-24 04:02:44 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:02:20 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:02:18 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:01:52 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:01:50 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 04:01:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 04:01:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:00:52 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:00:48 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 04:00:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 04:06:09 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-08-24 03:02:49 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-24 04:03:29 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-24 03:07:56 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-24 04:01:50 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 04:05:27 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 04:03:23 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 04:01:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 04:04:04 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 04:00:48 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 03:08:21 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-23 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:00:18 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:00:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:02:20 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:01:52 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:04:57 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:08:10 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:01:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 02:01:53 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:00:52 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:03:15 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:02:44 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:06:27 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:01:26 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-24 03:04:24 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:06:41 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-24 02:08:30 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:02:18 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 04:03:47 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-08-24 04:07:59 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-24 04:02:53 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-24 04:05:50 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.012 |  |
| 2026-08-24 03:05:50 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-08-24 04:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.043 |  |
| 2026-08-24 04:06:47 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-08-24 03:05:28 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)