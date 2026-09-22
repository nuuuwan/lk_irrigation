# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_14:28:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,918 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 14:28:24 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.049 |  |
| 2026-09-22 14:11:56 | Rathnapura (Kalu Ganga) | 4.31 | 🟢 Normal | -0.063 |  |
| 2026-09-22 14:10:52 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:10:41 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:08:20 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:07:50 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:07:05 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.18 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-22 14:06:37 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:05:38 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:05:22 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.021 |  |
| 2026-09-22 14:05:08 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-22 14:05:08 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:04:35 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.039 |  |
| 2026-09-22 14:04:29 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-22 14:04:27 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-09-22 14:04:15 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-09-22 14:04:13 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-09-22 14:03:35 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 14:03:26 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-22 14:03:17 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.012 |  |
| 2026-09-22 14:03:02 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:03:00 | Glencourse (Kelani Ganga) | 12.65 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:57 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:56 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-22 14:02:54 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:36 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.060 |  |
| 2026-09-22 14:02:28 | Ellagawa (Kalu Ganga) | 8.85 | 🟢 Normal | -0.042 |  |
| 2026-09-22 14:02:22 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:19 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:17 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-09-22 14:02:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:01:57 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-22 14:01:49 | Baddegama (Gin Ganga) | 4.16 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 14:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:01:38 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:01:37 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:01:18 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:00:42 | Magura (Kalu Ganga) | 4.75 | 🟡 Alert | -0.010 |  |
| 2026-09-22 14:00:30 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-22 14:00:24 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-22 14:00:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 14:01:49 | Baddegama (Gin Ganga) | 4.16 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 14:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.18 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-22 14:05:08 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-22 14:00:42 | Magura (Kalu Ganga) | 4.75 | 🟡 Alert | -0.010 |  |
| 2026-09-22 14:00:24 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-22 14:03:26 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-22 14:03:35 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 14:01:57 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-22 14:01:37 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:00:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:05:08 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:01:43 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:57 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:07:50 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:22 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:10:41 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:10:52 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:03:00 | Glencourse (Kelani Ganga) | 12.65 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:15 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:19 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:03:02 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:01:38 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:01:18 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:08:20 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:07:05 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:56 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-22 14:04:15 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-09-22 14:00:30 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-22 14:03:17 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.012 |  |
| 2026-09-22 14:04:29 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-22 14:04:13 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-09-22 14:05:22 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.021 |  |
| 2026-09-22 14:04:27 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-09-22 14:02:17 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-09-22 14:04:35 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.039 |  |
| 2026-09-22 14:02:28 | Ellagawa (Kalu Ganga) | 8.85 | 🟢 Normal | -0.042 |  |
| 2026-09-22 14:28:24 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.049 |  |
| 2026-09-22 14:02:36 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.060 |  |
| 2026-09-22 14:11:56 | Rathnapura (Kalu Ganga) | 4.31 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)