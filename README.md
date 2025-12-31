# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_02:24:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 02:24:19 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-01 02:22:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -2.118 |  |
| 2026-01-01 02:22:26 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -2.118 |  |
| 2026-01-01 02:13:07 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.055 |  |
| 2026-01-01 02:10:50 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:09:57 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:08:42 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -2.458 |  |
| 2026-01-01 02:08:24 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-01-01 02:08:22 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-01-01 02:07:00 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.005 |  |
| 2026-01-01 02:06:57 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:06:38 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-01 02:06:07 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:05:44 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.038 |  |
| 2026-01-01 02:05:21 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-01-01 02:05:19 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | -1.048 |  |
| 2026-01-01 02:05:17 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-01-01 02:05:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:05:00 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-01-01 02:03:55 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-01 02:03:33 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-01 02:03:13 | Siyambalanduwa (Heda Oya) | 2.87 | 🟢 Normal | -0.572 |  |
| 2026-01-01 02:02:49 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.060 |  |
| 2026-01-01 02:02:39 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:02:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:02:06 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:02:06 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-01 02:01:46 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-01 02:01:05 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:00:38 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-01 02:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:51:34 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 02:08:24 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-01-01 02:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-01-01 02:06:38 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-01 02:03:33 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-01 02:24:19 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-01 02:01:46 | Horowpothana (Yan Oya) | 2.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 02:02:06 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 22:10:48 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 02:03:55 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-01 02:02:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:02:39 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:05:30 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-01 01:15:37 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:01:05 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:10:50 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:09:57 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:05:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:06:57 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:18 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 00:03:12 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:06:07 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:05:00 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-01 02:07:00 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.005 |  |
| 2026-01-01 02:00:38 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-01 02:05:21 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-01-01 02:05:17 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-01-01 02:05:44 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.038 |  |
| 2026-01-01 02:13:07 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | -0.055 |  |
| 2026-01-01 02:02:49 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.060 |  |
| 2026-01-01 01:00:50 | Kuda Oya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.094 |  |
| 2026-01-01 01:00:59 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.417 |  |
| 2026-01-01 02:03:13 | Siyambalanduwa (Heda Oya) | 2.87 | 🟢 Normal | -0.572 |  |
| 2026-01-01 02:05:19 | Katharagama (Menik Ganga) | -0.50 | 🟢 Normal | -1.048 |  |
| 2026-01-01 02:22:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -2.118 |  |
| 2026-01-01 02:08:42 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -2.458 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)