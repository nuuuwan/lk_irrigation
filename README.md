# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_04:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,063 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 04:19:49 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -4.320 |  |
| 2026-08-22 04:19:24 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -4.320 |  |
| 2026-08-22 04:18:30 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-22 04:10:47 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-08-22 04:08:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-22 04:06:34 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-08-22 04:06:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:06:03 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.089 |  |
| 2026-08-22 04:05:35 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.012 |  |
| 2026-08-22 04:04:45 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 04:04:29 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 03:01:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-22 04:02:21 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-22 04:04:45 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-22 04:01:32 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-22 04:08:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-22 04:18:30 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-22 03:00:51 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.003 |  |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:01:18 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:01:12 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:00:48 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:03:34 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:01:45 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:02:44 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:02:49 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 03:10:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:00:40 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:03:10 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:01:25 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:01:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:02:07 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:06:05 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:03:16 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:04:12 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:00:19 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-22 04:05:35 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | -0.012 |  |
| 2026-08-22 04:06:34 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-08-22 04:03:30 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-08-22 04:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-08-22 04:04:29 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.030 |  |
| 2026-08-22 04:10:47 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-08-22 02:04:29 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.051 |  |
| 2026-08-22 04:06:03 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.089 |  |
| 2026-08-22 04:02:29 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.231 |  |
| 2026-08-22 04:00:29 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -1.055 |  |
| 2026-08-22 04:19:49 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -4.320 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)