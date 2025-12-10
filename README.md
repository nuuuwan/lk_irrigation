# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_15:07:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,243 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 15:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:07:32 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:06:18 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:05:31 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:05:17 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2025-12-10 15:05:11 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:04:31 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:04:17 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:03:53 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:03:45 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-10 15:03:35 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2025-12-10 15:03:29 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:03:24 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:03:23 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:03:16 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.023 |  |
| 2025-12-10 15:03:06 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:03:02 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:02:59 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:02:54 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:02:46 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | -0.032 |  |
| 2025-12-10 15:02:45 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:02:39 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2025-12-10 15:02:35 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:02:23 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:02:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 15:02:12 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-10 15:01:57 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.040 |  |
| 2025-12-10 15:01:44 | Horowpothana (Yan Oya) | 5.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:01:38 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.020 |  |
| 2025-12-10 15:01:36 | Yaka Wewa (Ma Oya) | 2.20 | 🟢 Normal | -0.199 |  |
| 2025-12-10 15:01:22 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:01:12 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:01:09 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:01:08 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-10 15:01:02 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:01:00 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.050 |  |
| 2025-12-10 15:00:55 | Weraganthota (Mahaweli Ganga) | -0.51 | 🟢 Normal | -0.030 |  |
| 2025-12-10 14:11:19 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 15:02:12 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-10 15:03:45 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-10 15:01:08 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-10 15:02:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 15:06:18 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:01:44 | Horowpothana (Yan Oya) | 5.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:02:23 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:03:02 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:03:53 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 15:02:59 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:03:23 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:03:24 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:03:06 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:02:45 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:02:54 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:04:17 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:02:35 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 15:05:31 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:07:32 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:04:31 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:01:12 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:03:29 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:05:11 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:01:22 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 15:01:09 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-10 14:05:49 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-10 15:03:35 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2025-12-10 15:02:39 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2025-12-10 15:01:38 | Manampitiya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.020 |  |
| 2025-12-10 15:03:16 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.023 |  |
| 2025-12-10 15:05:17 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2025-12-10 15:00:55 | Weraganthota (Mahaweli Ganga) | -0.51 | 🟢 Normal | -0.030 |  |
| 2025-12-10 15:02:46 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | -0.032 |  |
| 2025-12-10 15:01:57 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.040 |  |
| 2025-12-10 15:01:00 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.050 |  |
| 2025-12-10 15:01:36 | Yaka Wewa (Ma Oya) | 2.20 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)