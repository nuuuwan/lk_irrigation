# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_02:05:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,402 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 02:05:20 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:04:26 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2025-12-22 02:04:08 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:03:59 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.058 |  |
| 2025-12-22 02:03:57 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2025-12-22 02:03:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 02:03:14 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:03:05 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.035 |  |
| 2025-12-22 02:03:02 | Horowpothana (Yan Oya) | 4.24 | 🟢 Normal | -0.121 |  |
| 2025-12-22 02:02:43 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:02:42 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:02:35 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:02:14 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 02:02:09 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -1.895 |  |
| 2025-12-22 02:01:50 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -1.895 |  |
| 2025-12-22 02:01:43 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:01:34 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:00:56 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:00:10 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.102 |  |
| 2025-12-22 01:53:53 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 01:48:15 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:40:12 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.006 |  |
| 2025-12-22 01:33:06 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2025-12-22 01:24:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.102 |  |
| 2025-12-22 01:17:39 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:17:38 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:17:36 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:15:45 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.049 |  |
| 2025-12-22 01:09:10 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.003 |  |
| 2025-12-22 01:08:35 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:08:33 | Horowpothana (Yan Oya) | 4.35 | 🟢 Normal | -0.121 |  |
| 2025-12-22 01:08:19 | Horowpothana (Yan Oya) | 4.31 | 🟢 Normal | -0.121 |  |
| 2025-12-22 01:07:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 01:07:23 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.039 |  |
| 2025-12-22 01:07:15 | Horowpothana (Yan Oya) | 4.36 | 🟢 Normal | -0.121 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 01:02:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-22 01:53:53 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 00:03:54 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 01:07:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 02:00:56 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:03:14 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 00:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:01:43 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:02:35 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:05:20 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:02:43 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:04:08 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:02:42 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:03:06 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:05:38 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:03:06 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 00:11:59 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:01:34 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:48:15 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:01:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-22 01:09:10 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.003 |  |
| 2025-12-22 01:40:12 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.006 |  |
| 2025-12-22 01:33:06 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2025-12-22 02:03:57 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2025-12-22 02:03:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 02:02:14 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 01:03:28 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-22 02:03:05 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.035 |  |
| 2025-12-21 22:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2025-12-22 01:07:23 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.039 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-22 02:04:26 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2025-12-22 02:03:59 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.058 |  |
| 2025-12-22 02:00:10 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.102 |  |
| 2025-12-22 02:03:02 | Horowpothana (Yan Oya) | 4.24 | 🟢 Normal | -0.121 |  |
| 2025-12-22 02:02:09 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)