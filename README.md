# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_01:18:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 01:18:12 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:10:44 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:09:54 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.027 |  |
| 2026-08-21 01:08:30 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:08:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-21 01:07:15 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-08-21 01:07:14 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:05:48 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:05:43 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:05:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:05:15 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:04:59 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-21 01:04:39 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-08-21 01:04:33 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-21 01:04:26 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 01:03:53 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 01:02:34 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:02:34 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-08-21 01:02:26 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.074 |  |
| 2026-08-21 01:02:17 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.031 |  |
| 2026-08-21 01:02:08 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:54 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:28 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-21 01:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:18 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:17 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:15 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-21 01:01:14 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:02 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.127 |  |
| 2026-08-21 01:00:34 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 00:00:09 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-21 01:08:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-21 01:04:59 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-08-21 01:01:15 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-21 01:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-21 01:03:53 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 01:04:26 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 00:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 01:05:48 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:18 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:14 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:10:44 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:08:30 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:05:43 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:07:14 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:02:34 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:54 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 00:02:44 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:18:12 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:05:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:04:33 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:05:15 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:19 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:01:17 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:02:08 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 01:07:15 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-08-21 01:01:28 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-21 01:04:39 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-08-21 01:00:34 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-08-21 01:02:34 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-08-21 01:09:54 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.027 |  |
| 2026-08-21 01:02:17 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.031 |  |
| 2026-08-21 00:14:30 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.063 |  |
| 2026-08-21 01:02:26 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.074 |  |
| 2026-08-21 01:01:02 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)