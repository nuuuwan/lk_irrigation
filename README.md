# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_00:10:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 00:10:03 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-09 00:08:54 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-09 00:08:45 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:07:26 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:07:13 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-09 00:07:03 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.087 |  |
| 2025-12-09 00:06:40 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:06:13 | Rathnapura (Kalu Ganga) | 3.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 00:05:45 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 00:04:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:04:20 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 00:04:15 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:03:56 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:03:46 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:03:18 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:57 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:56 | Thanthirimale (Malwathu Oya) | 3.86 | 🟢 Normal | -0.039 |  |
| 2025-12-09 00:02:54 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:38 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:35 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.218 |  |
| 2025-12-09 00:02:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-09 00:02:25 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:14 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 00:02:13 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-09 00:01:58 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:01:33 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:01:23 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:01:16 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-09 00:01:08 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:00:24 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2025-12-09 00:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.016 |  |
| 2025-12-08 23:23:24 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.016 |  |
| 2025-12-08 23:17:36 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 00:00:24 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2025-12-09 00:07:13 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-09 00:02:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-09 00:02:14 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 00:06:13 | Rathnapura (Kalu Ganga) | 3.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 00:01:16 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 00:05:45 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-08 22:04:09 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-09 00:04:20 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 00:01:58 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:25 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:01:33 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:06:40 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:54 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:03:46 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:04:15 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:04:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:38 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:07:26 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:08:45 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:03:56 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:03:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:01:23 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 00:02:57 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:17:36 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.008 |  |
| 2025-12-09 00:10:03 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-09 00:08:54 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-09 00:02:13 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 00:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.016 |  |
| 2025-12-09 00:02:56 | Thanthirimale (Malwathu Oya) | 3.86 | 🟢 Normal | -0.039 |  |
| 2025-12-08 23:05:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.048 |  |
| 2025-12-09 00:07:03 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.087 |  |
| 2025-12-09 00:02:35 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.218 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)