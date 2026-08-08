# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_03:09:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,390 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 03:09:55 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:09:39 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:08:14 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.037 |  |
| 2026-08-09 03:07:30 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:07:20 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 03:05:49 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 03:05:22 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-08-09 03:05:15 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:56 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.006 |  |
| 2026-08-09 03:04:40 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:35 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:28 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:24 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.042 |  |
| 2026-08-09 03:04:21 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.029 |  |
| 2026-08-09 03:04:20 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:11 | Peradeniya (Mahaweli Ganga) | 3.69 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-08-09 03:04:04 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-08-09 03:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-09 03:03:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-09 03:03:09 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:03:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:03:09 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 03:02:51 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:48 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:26 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.001 |  |
| 2026-08-09 03:02:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:54 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.032 |  |
| 2026-08-09 03:01:44 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:34 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:15 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 02:14:23 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-08-09 03:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-09 03:04:11 | Peradeniya (Mahaweli Ganga) | 3.69 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-08-09 02:02:28 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-09 03:07:20 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 03:03:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-09 02:01:56 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 03:03:09 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 03:05:49 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 03:02:26 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.001 |  |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:15 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:51 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:03:09 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:09:55 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:05:44 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:05:15 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:03:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:34 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:07:30 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:35 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:02:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:40 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:09:39 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:01:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:01:44 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:28 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:56 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.006 |  |
| 2026-08-09 03:04:04 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-08-09 03:04:21 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.029 |  |
| 2026-08-09 03:01:54 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.032 |  |
| 2026-08-09 03:08:14 | Glencourse (Kelani Ganga) | 10.81 | 🟢 Normal | -0.037 |  |
| 2026-08-09 03:05:22 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.040 |  |
| 2026-08-09 03:04:24 | Kithulgala (Kelani Ganga) | 2.34 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)