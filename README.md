# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_00:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,255 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 00:10:21 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.036 |  |
| 2026-01-01 00:09:12 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-01 00:09:02 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 00:08:40 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-01 00:08:38 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:08:32 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-01-01 00:08:08 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:07:13 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 00:06:48 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:05:58 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.169 |  |
| 2026-01-01 00:05:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-01 00:05:44 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:05:40 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-01 00:04:31 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-01-01 00:04:31 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 00:03:35 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 450.000 | 🔺 Rising |
| 2026-01-01 00:03:33 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 450.000 | 🔺 Rising |
| 2026-01-01 00:03:32 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:30 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-01 00:03:18 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:12 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:07 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-01-01 00:02:56 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.041 |  |
| 2026-01-01 00:02:54 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:02:47 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-01 00:02:47 | Siyambalanduwa (Heda Oya) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 00:02:45 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 00:02:32 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:01:59 | Nakkala (Kumbukkan Oya) | 1.79 | 🟢 Normal | -0.312 |  |
| 2026-01-01 00:01:46 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:15:43 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 00:03:35 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 450.000 | 🔺 Rising |
| 2026-01-01 00:05:40 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-01 00:05:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-01 00:09:12 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-01 00:02:47 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-01 00:02:45 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 23:02:18 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 00:04:31 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 00:07:13 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 00:02:47 | Siyambalanduwa (Heda Oya) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 22:10:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 00:09:02 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 00:02:32 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:06:48 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:01:46 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:08:08 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:05:44 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:05:14 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:18 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:02:54 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:12 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:02:32 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-31 23:10:31 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:08:38 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:32 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:08:40 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-01 00:03:30 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-01 00:03:07 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-31 22:09:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.018 |  |
| 2026-01-01 00:08:32 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-01-01 00:04:31 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-01-01 00:10:21 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.036 |  |
| 2026-01-01 00:02:56 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.041 |  |
| 2026-01-01 00:05:58 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.169 |  |
| 2026-01-01 00:01:59 | Nakkala (Kumbukkan Oya) | 1.79 | 🟢 Normal | -0.312 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)