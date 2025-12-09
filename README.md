# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_03:03:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,772 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 03:03:56 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.022 |  |
| 2025-12-10 03:03:55 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-10 03:03:25 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-10 03:02:49 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -1080.000 |  |
| 2025-12-10 03:02:47 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | -1080.000 |  |
| 2025-12-10 03:02:13 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:02:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.098 |  |
| 2025-12-10 03:02:03 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:01:43 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2025-12-10 03:01:24 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:01:01 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 03:00:20 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-10 02:59:57 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 18.288 | 🔺 Rising |
| 2025-12-10 02:59:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 18.288 | 🔺 Rising |
| 2025-12-10 02:44:26 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.639 | 🔺 Rising |
| 2025-12-10 02:40:50 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-10 02:36:10 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.022 |  |
| 2025-12-10 02:34:22 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-10 02:31:17 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.639 | 🔺 Rising |
| 2025-12-10 02:21:01 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.639 | 🔺 Rising |
| 2025-12-10 02:09:11 | Padiyathalawa (Maduru Oya) | 1.77 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-10 02:08:28 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.087 |  |
| 2025-12-10 02:08:16 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-10 02:05:20 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -2.667 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 02:59:57 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 18.288 | 🔺 Rising |
| 2025-12-10 02:44:26 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.639 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-10 03:03:55 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-10 02:34:22 | Panadugama (Nilwala Ganga) | 4.42 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-10 02:04:58 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-10 02:01:56 | Horowpothana (Yan Oya) | 3.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 02:01:56 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 02:40:50 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2025-12-10 03:02:13 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:00:20 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:02:03 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:01:00 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:01:01 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 02:03:26 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:05:35 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 03:01:24 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:54:13 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.006 |  |
| 2025-12-10 02:03:14 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-10 03:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-10 03:03:25 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-10 02:03:26 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-10 00:12:55 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-10 03:01:43 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2025-12-10 02:01:08 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2025-12-10 02:01:30 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.021 |  |
| 2025-12-10 03:03:56 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.022 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-10 02:01:44 | Yaka Wewa (Ma Oya) | 1.54 | 🟢 Normal | -0.030 |  |
| 2025-12-10 02:03:28 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.040 |  |
| 2025-12-10 02:08:28 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.087 |  |
| 2025-12-10 03:02:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.098 |  |
| 2025-12-10 02:05:20 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -2.667 |  |
| 2025-12-10 03:02:49 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -1080.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)