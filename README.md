# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_01:28:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 01:28:58 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-01 01:25:38 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:15:37 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:12:49 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-01 01:11:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.018 |  |
| 2026-01-01 01:11:18 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:09:46 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:07:58 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.052 |  |
| 2026-01-01 01:07:24 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-01 01:06:38 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:05:56 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 01:05:30 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:04:42 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:04:38 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 01:04:28 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:03:27 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.022 |  |
| 2026-01-01 01:03:02 | Manampitiya (Mahaweli Ganga) | 4.05 | 🟡 Alert | 242.769 | 🔺 Rising |
| 2026-01-01 01:02:36 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-01 01:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-01-01 01:02:23 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.040 |  |
| 2026-01-01 01:02:23 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 242.769 | 🔺 Rising |
| 2026-01-01 01:02:21 | Siyambalanduwa (Heda Oya) | 3.45 | 🟢 Normal | -0.564 |  |
| 2026-01-01 01:02:19 | Katharagama (Menik Ganga) | 0.60 | 🟢 Normal | -0.064 |  |
| 2026-01-01 01:01:46 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-01 01:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-01 01:01:38 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-01-01 01:00:59 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.417 |  |
| 2026-01-01 01:00:50 | Kuda Oya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.094 |  |
| 2026-01-01 01:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 01:03:02 | Manampitiya (Mahaweli Ganga) | 4.05 | 🟡 Alert | 242.769 | 🔺 Rising |
| 2026-01-01 00:03:35 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 450.000 | 🔺 Rising |
| 2026-01-01 01:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-01-01 01:07:24 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-01 01:05:56 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 01:04:38 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 01:01:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-01 01:12:49 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 23:02:18 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 01:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:10:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 01:28:58 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-01 01:04:28 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:11:18 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:05:30 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:15:37 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:09:46 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:08:08 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:05:44 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:25:38 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:06:38 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:18 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:12 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:04:42 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:08:38 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:01:38 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-01-01 01:02:36 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-01 01:01:46 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-01 01:11:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.018 |  |
| 2026-01-01 01:03:27 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.022 |  |
| 2026-01-01 01:02:23 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.040 |  |
| 2026-01-01 01:07:58 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.052 |  |
| 2026-01-01 01:02:19 | Katharagama (Menik Ganga) | 0.60 | 🟢 Normal | -0.064 |  |
| 2026-01-01 01:00:50 | Kuda Oya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.094 |  |
| 2026-01-01 01:00:59 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.417 |  |
| 2026-01-01 01:02:21 | Siyambalanduwa (Heda Oya) | 3.45 | 🟢 Normal | -0.564 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)