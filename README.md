# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_17:03:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 17:03:44 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 17:03:40 | Kithulgala (Kelani Ganga) | 0.86 | 🟢 Normal | -58.426 |  |
| 2025-12-09 17:03:27 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:03:11 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2025-12-09 17:03:10 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:02:50 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:39 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -58.426 |  |
| 2025-12-09 17:02:16 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 17:02:10 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2025-12-09 17:02:04 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.049 |  |
| 2025-12-09 17:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-09 17:02:00 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:00 | Yaka Wewa (Ma Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:59 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:24 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:01:20 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 17:01:16 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:11 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-09 16:32:31 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:30:46 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:25:14 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2025-12-09 16:22:22 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:14:45 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 16:09:14 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:25 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:08 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:07:59 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:06:26 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 16:06:20 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 16:06:15 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:05:40 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.130 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 16:25:14 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2025-12-09 16:02:57 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2025-12-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-09 16:05:40 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2025-12-09 17:03:44 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 17:01:11 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 17:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-09 16:00:30 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-09 16:04:31 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 17:02:16 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 17:01:20 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 16:14:45 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 17:02:00 | Yaka Wewa (Ma Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:01:33 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:02:34 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:03:08 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:06:15 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:16 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:22:22 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:03:27 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:25 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:00 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:08 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:30:46 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:59 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:50 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:24 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:03:10 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-09 16:03:52 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:03:11 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2025-12-09 16:04:14 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.031 |  |
| 2025-12-09 17:02:10 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2025-12-09 16:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.65 | 🟢 Normal | -0.041 |  |
| 2025-12-09 16:02:45 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2025-12-09 17:02:04 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.049 |  |
| 2025-12-09 16:03:22 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.054 |  |
| 2025-12-09 17:03:40 | Kithulgala (Kelani Ganga) | 0.86 | 🟢 Normal | -58.426 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)