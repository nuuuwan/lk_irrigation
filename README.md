# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_09:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 09:03:22 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:03:18 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | -0.125 |  |
| 2026-11-04 09:02:52 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:47 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:46 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-04 09:02:45 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 09:02:40 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-11-04 09:02:40 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.124 |  |
| 2026-11-04 09:02:17 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 09:02:09 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-11-04 09:02:03 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:02:00 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:01:18 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:01:09 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-11-04 09:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:00:39 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-04 09:00:33 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 09:00:08 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:26:28 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:24:39 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.068 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 08:04:19 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | 2.011 | 🔺 Rising |
| 2026-11-04 09:00:39 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-04 09:02:46 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-04 09:02:17 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-04 08:04:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 08:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 08:03:38 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 09:02:45 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 08:05:33 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 09:00:08 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:01:18 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:03:22 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-04 09:02:00 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 08:04:04 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:02:03 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-04 09:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-04 08:07:39 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-11-04 09:02:47 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:52 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-11-04 09:02:09 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-11-04 08:01:42 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.025 |  |
| 2026-11-04 09:02:40 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.029 |  |
| 2026-11-04 09:00:33 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:05:10 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:26:28 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:00:24 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-11-04 08:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-11-04 08:03:22 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:09:46 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:03:42 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.042 |  |
| 2026-11-04 08:02:54 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.042 |  |
| 2026-11-04 09:01:09 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-11-04 08:24:39 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.068 |  |
| 2026-11-04 08:09:47 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.069 |  |
| 2026-11-04 08:03:12 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.103 |  |
| 2026-11-04 08:03:23 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | -0.107 |  |
| 2026-11-04 08:02:10 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.112 |  |
| 2026-11-04 09:02:40 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.124 |  |
| 2026-11-04 09:03:18 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)