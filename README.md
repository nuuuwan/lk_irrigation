# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_13:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,709 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 13:03:15 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-11-03 13:03:05 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 13:02:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-03 13:02:40 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.026 |  |
| 2026-11-03 13:02:38 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.027 |  |
| 2026-11-03 13:02:19 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-11-03 13:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-03 13:01:58 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-11-03 13:01:57 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 13:01:49 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:01:39 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-03 13:01:32 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.091 |  |
| 2026-11-03 13:01:16 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-03 13:01:11 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.180 |  |
| 2026-11-03 13:01:04 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:01:02 | Horowpothana (Yan Oya) | 2.60 | 🟢 Normal | -0.040 |  |
| 2026-11-03 13:00:58 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 12:04:19 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-03 13:01:39 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-03 12:04:05 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-03 12:04:01 | Moragaswewa (Deduru Oya) | 4.18 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-03 13:03:05 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 12:02:54 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 13:01:57 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 13:01:49 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 11:28:38 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:01:04 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 12:04:21 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 12:03:58 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-11-03 13:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-03 12:02:08 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-11-03 12:00:11 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-03 12:05:45 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-11-03 12:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | -0.019 |  |
| 2026-11-03 12:05:55 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-11-03 13:01:58 | Wellawaya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-11-03 12:05:46 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-03 13:01:16 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-03 12:18:17 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-11-03 13:02:40 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.026 |  |
| 2026-11-03 13:02:38 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.027 |  |
| 2026-11-03 13:03:15 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-11-03 13:02:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-03 12:03:28 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.039 |  |
| 2026-11-03 13:01:02 | Horowpothana (Yan Oya) | 2.60 | 🟢 Normal | -0.040 |  |
| 2026-11-03 13:02:19 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-11-03 12:02:36 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.041 |  |
| 2026-11-03 13:00:58 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.047 |  |
| 2026-11-03 12:04:39 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-11-03 12:01:07 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.054 |  |
| 2026-11-03 12:05:44 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.069 |  |
| 2026-11-03 13:01:32 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.091 |  |
| 2026-11-03 12:03:41 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.101 |  |
| 2026-11-03 12:04:19 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.112 |  |
| 2026-11-03 12:01:52 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | -0.140 |  |
| 2026-11-03 13:01:11 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)