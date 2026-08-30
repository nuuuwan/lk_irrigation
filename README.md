# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_05:29:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,853 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 05:29:44 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.007 |  |
| 2026-08-30 05:18:34 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-08-30 05:18:33 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-08-30 05:16:33 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-30 05:13:33 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:12:15 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.017 |  |
| 2026-08-30 05:11:28 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.015 |  |
| 2026-08-30 05:08:29 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:07:42 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-30 05:06:15 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.026 |  |
| 2026-08-30 05:05:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:05:42 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:05:25 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:04:20 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-08-30 05:03:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |
| 2026-08-30 05:03:15 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:03:08 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.010 |  |
| 2026-08-30 05:03:06 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:03:03 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:02:58 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:02:46 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | -0.029 |  |
| 2026-08-30 05:02:39 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:02:27 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:02:04 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-30 05:01:48 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-08-30 05:01:47 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:43 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-30 05:01:39 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.727 |  |
| 2026-08-30 05:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:24 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:13 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 05:01:13 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:01 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 05:00:56 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 05:18:34 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-08-30 05:01:48 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-08-30 05:04:20 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-08-30 05:02:04 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-30 05:16:33 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-30 05:01:01 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 05:01:13 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 05:07:42 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-30 04:11:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-30 05:00:56 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:13 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:47 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:03:06 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:02:54 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:05:42 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:03:15 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:08:29 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:01:24 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:05:44 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:03:03 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:05:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:05:25 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:00:49 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:02:27 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:02:58 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-08-30 04:06:13 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:13:33 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-30 05:29:44 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.007 |  |
| 2026-08-30 05:03:08 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.010 |  |
| 2026-08-30 05:01:43 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-30 05:11:28 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.015 |  |
| 2026-08-30 05:12:15 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.017 |  |
| 2026-08-30 04:11:28 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-08-30 05:06:15 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.026 |  |
| 2026-08-30 05:02:46 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | -0.029 |  |
| 2026-08-29 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.030 |  |
| 2026-08-30 05:03:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |
| 2026-08-30 05:01:39 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.727 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)