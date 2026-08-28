# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_01:22:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,819 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 01:22:13 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:19:18 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 01:17:20 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:16:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-29 01:10:23 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.045 |  |
| 2026-08-29 01:10:14 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-08-29 01:06:56 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:06:46 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 00:01:39 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-29 01:10:14 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-08-29 01:02:25 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-29 01:05:10 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-29 01:03:49 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 01:16:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-29 00:01:59 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-29 01:02:21 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 01:19:18 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 01:03:12 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 01:04:21 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:06:56 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:01:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:04:27 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:01:08 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 00:01:28 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-28 23:03:38 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:02:16 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:05:48 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:01:09 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:01:59 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 00:01:50 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:05:24 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:06:18 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:17:20 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:03:18 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:22:13 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:02:44 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:01:57 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 01:06:46 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:01:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-29 01:06:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-08-29 01:02:22 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-08-29 01:10:23 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.045 |  |
| 2026-08-29 01:05:34 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)