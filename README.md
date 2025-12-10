# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_13:05:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,161 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 13:05:59 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2025-12-10 13:05:45 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2025-12-10 13:05:44 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:32 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:13 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:08 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:05 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2025-12-10 13:04:57 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:04:40 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-10 13:04:19 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.039 |  |
| 2025-12-10 13:04:14 | Thanthirimale (Malwathu Oya) | 3.72 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-10 13:04:14 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.032 |  |
| 2025-12-10 13:03:48 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2025-12-10 13:03:37 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-10 13:03:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-10 13:03:23 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:03:20 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:03:03 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.080 |  |
| 2025-12-10 13:02:51 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:02:47 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 13:01:58 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:01:30 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:01:27 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.030 |  |
| 2025-12-10 13:01:27 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:01:16 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:01:15 | Yaka Wewa (Ma Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2025-12-10 13:01:10 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.079 |  |
| 2025-12-10 13:01:06 | Horowpothana (Yan Oya) | 5.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 13:00:44 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:00:25 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2025-12-10 13:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:20:38 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:08:39 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.032 |  |
| 2025-12-10 12:08:39 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-10 12:08:05 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:07:44 | Weraganthota (Mahaweli Ganga) | -0.50 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2025-12-10 12:07:36 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 13:00:25 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2025-12-10 13:04:14 | Thanthirimale (Malwathu Oya) | 3.72 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-10 13:03:37 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-10 13:03:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-10 13:01:06 | Horowpothana (Yan Oya) | 5.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 13:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 13:01:27 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:02:47 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:03:23 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:03:20 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:04:57 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 13:01:30 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:01:16 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:13 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:00:44 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:01:58 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:44 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:08 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:05:32 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:05:23 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 13:02:51 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 12:05:04 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 13:04:40 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-10 12:04:41 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-10 13:03:48 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2025-12-10 13:05:59 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2025-12-10 12:08:39 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2025-12-10 13:05:05 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2025-12-10 13:01:27 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.030 |  |
| 2025-12-10 12:01:55 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2025-12-10 13:04:14 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.032 |  |
| 2025-12-10 13:04:19 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.039 |  |
| 2025-12-10 13:01:15 | Yaka Wewa (Ma Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2025-12-10 13:05:45 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.048 |  |
| 2025-12-10 12:01:40 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.052 |  |
| 2025-12-10 13:01:10 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.079 |  |
| 2025-12-10 13:03:03 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)