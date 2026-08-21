# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_18:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,711 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 18:12:05 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-21 18:11:55 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:08:50 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-08-21 18:07:55 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:06:55 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 18:05:37 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-21 18:05:18 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.066 |  |
| 2026-08-21 18:04:20 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:19 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:15 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 18:03:40 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 18:03:25 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 18:03:07 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:59 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-21 18:02:48 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-08-21 18:02:47 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:38 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.022 |  |
| 2026-08-21 18:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:14 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:09 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-08-21 18:02:08 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:49 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -449.538 |  |
| 2026-08-21 18:01:39 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:17 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:10 | Putupaula (Kalu Ganga) | 5.72 | 🔴 Major Flood | -449.538 |  |
| 2026-08-21 18:01:09 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:09 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-21 18:00:41 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:00:33 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:00:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 18:01:09 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-21 18:05:18 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-21 18:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 18:03:40 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 18:12:05 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-21 18:02:14 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-21 18:03:25 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 18:04:15 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 18:06:55 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:00:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 17:00:29 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:39 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:08 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:19 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:00:41 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:03:07 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:07:55 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:00:33 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:11:55 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:20 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:09 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:01:17 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:47 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:05:37 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-21 18:02:59 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-21 17:01:07 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.010 |  |
| 2026-08-21 18:02:48 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-08-21 18:02:09 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-08-21 18:02:38 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.022 |  |
| 2026-08-21 18:08:50 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-08-21 18:04:24 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.066 |  |
| 2026-08-21 18:01:49 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -449.538 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)