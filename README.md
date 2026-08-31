# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_14:11:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,112 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 14:11:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:11:12 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-08-31 14:10:30 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:09:54 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:08:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:08:42 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:08:13 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.018 |  |
| 2026-08-31 14:07:20 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.267 |  |
| 2026-08-31 14:06:06 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.030 |  |
| 2026-08-31 14:06:01 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:05:16 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:04:58 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:04:31 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-08-31 14:04:30 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:04:27 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 14:04:19 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:04:06 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:03:42 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-08-31 14:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-08-31 14:03:23 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:03:17 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 14:03:15 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:03:08 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:45 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:41 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:27 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-31 14:02:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:22 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:11 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:09 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:05 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:54 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:52 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.092 |  |
| 2026-08-31 14:01:48 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:17 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:00 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:00:21 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:39:55 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 14:03:42 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-08-31 14:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-08-31 14:02:27 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-31 14:04:27 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 14:03:17 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 14:05:16 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:17 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:00:21 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:48 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:41 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:05 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:11 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:04:19 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:01:00 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:03:08 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:08:42 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:03:23 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:04:58 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:09 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:08:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:02:45 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:39:55 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:09:54 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:04:30 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:11:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-31 14:10:30 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:04:06 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:03:15 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:06:01 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.010 |  |
| 2026-08-31 14:04:31 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2026-08-31 14:08:13 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.018 |  |
| 2026-08-31 14:11:12 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-08-31 14:06:06 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.030 |  |
| 2026-08-31 13:10:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.071 |  |
| 2026-08-31 14:01:52 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.092 |  |
| 2026-08-31 14:07:20 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)