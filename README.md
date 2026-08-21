# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_01:16:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,962 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 01:16:42 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 2.851 | 🔺 Rising |
| 2026-08-22 01:13:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-22 01:09:26 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:06:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:06:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:05:42 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-08-22 01:04:49 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 01:04:41 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-08-22 01:03:51 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-22 01:03:50 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-08-22 01:03:42 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:03:40 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-22 01:03:30 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:03:21 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:03:03 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.040 |  |
| 2026-08-22 01:02:51 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:02:37 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-22 01:02:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:02:19 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:02:19 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:48 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.150 |  |
| 2026-08-22 01:01:47 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:33 | Manampitiya (Mahaweli Ganga) | -0.95 | 🟢 Normal | 2.851 | 🔺 Rising |
| 2026-08-22 01:01:27 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:18 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-22 01:01:06 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-08-22 01:00:37 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 01:16:42 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 2.851 | 🔺 Rising |
| 2026-08-22 00:06:21 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-08-22 01:13:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.07 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-22 01:02:37 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-22 01:01:18 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-22 00:02:37 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-22 01:04:49 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:27 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 00:02:28 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:00:37 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:06 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:09:26 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:02:51 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:03:21 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:02:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 00:01:17 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:01:47 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:02:19 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:03:42 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:06:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:03:30 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:06:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 00:08:26 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-22 00:04:59 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 01:02:19 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-22 00:10:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-08-22 00:09:55 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-22 01:03:51 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-22 01:04:41 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-08-22 01:03:40 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-22 01:03:50 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-08-22 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-08-22 01:03:03 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.040 |  |
| 2026-08-22 01:05:42 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-08-22 01:01:48 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)