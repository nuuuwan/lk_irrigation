# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_03:12:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,349 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 03:12:52 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:11:28 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:09:19 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.014 |  |
| 2026-01-01 03:08:32 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 03:08:19 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-01 03:08:12 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-01 03:07:59 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.142 |  |
| 2026-01-01 03:07:52 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 03:06:21 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.005 |  |
| 2026-01-01 03:06:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-01-01 03:05:54 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | -0.450 |  |
| 2026-01-01 03:05:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:05:47 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:04:52 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-01-01 03:04:42 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:04:42 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-01 03:03:30 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:03:02 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.110 |  |
| 2026-01-01 03:02:57 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:02:57 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 03:02:22 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 03:02:06 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-01 03:01:54 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 1.124 | 🔺 Rising |
| 2026-01-01 03:01:09 | Kuda Oya (Kirindi Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-01-01 03:01:06 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:01:05 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:00:59 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 03:01:54 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 1.124 | 🔺 Rising |
| 2026-01-01 03:04:42 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-01 03:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 02:24:19 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-01 03:02:06 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-01 03:08:12 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-01 03:02:22 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-01 03:08:19 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 03:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 03:08:32 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 03:02:57 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 22:10:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 02:03:55 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-01 03:12:52 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:04:42 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:07:52 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:02:57 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:01:06 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:10:50 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:05:47 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:05:51 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:18 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:00:59 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:01:05 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:11:28 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:05:00 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:03:30 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:06:21 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.005 |  |
| 2026-01-01 03:09:19 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.014 |  |
| 2026-01-01 03:01:09 | Kuda Oya (Kirindi Oya) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-01-01 03:06:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-01-01 03:04:52 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-01-01 03:03:02 | Peradeniya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.110 |  |
| 2026-01-01 03:07:59 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | -0.142 |  |
| 2026-01-01 03:05:54 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | -0.450 |  |
| 2026-01-01 02:08:42 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -2.458 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)