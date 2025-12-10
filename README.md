# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_05:25:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,861 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 05:25:01 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:24:32 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.007 |  |
| 2025-12-10 05:20:35 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:16:33 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-10 05:13:10 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:10:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.057 |  |
| 2025-12-10 05:09:05 | Padiyathalawa (Maduru Oya) | 1.74 | 🟢 Normal | -126.000 |  |
| 2025-12-10 05:09:03 | Padiyathalawa (Maduru Oya) | 1.81 | 🟢 Normal | -126.000 |  |
| 2025-12-10 05:08:11 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2025-12-10 05:08:10 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2025-12-10 05:08:08 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2025-12-10 05:08:07 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2025-12-10 05:08:06 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2025-12-10 05:08:02 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.030 |  |
| 2025-12-10 05:07:50 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.191 |  |
| 2025-12-10 05:07:14 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:07:00 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:06:28 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.255 |  |
| 2025-12-10 05:06:27 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:05:30 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2025-12-10 05:05:17 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.080 |  |
| 2025-12-10 05:04:50 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:04:15 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-10 05:04:12 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.030 |  |
| 2025-12-10 05:03:54 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-10 05:02:47 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.027 |  |
| 2025-12-10 05:02:43 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.012 |  |
| 2025-12-10 05:02:33 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:02:25 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:12 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:10 | Yaka Wewa (Ma Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-10 05:01:59 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:01:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-10 05:01:15 | Horowpothana (Yan Oya) | 3.96 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-10 05:00:29 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 05:00:14 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:46:58 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:42:55 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.255 |  |
| 2025-12-10 04:40:21 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 05:08:11 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-10 05:01:15 | Horowpothana (Yan Oya) | 3.96 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-10 05:01:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-10 05:03:54 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-10 05:16:33 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-10 05:04:15 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-10 05:00:29 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 05:25:01 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:13:10 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:20:35 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:07:00 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:00:14 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:12 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:25 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:06:27 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:15:33 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:07:14 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:24:32 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.007 |  |
| 2025-12-10 05:01:59 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:02:33 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:04:50 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:02:43 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.012 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-10 05:05:30 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-10 05:02:47 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.027 |  |
| 2025-12-10 05:08:02 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | -0.030 |  |
| 2025-12-10 05:02:10 | Yaka Wewa (Ma Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-10 05:04:12 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.030 |  |
| 2025-12-10 05:10:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.057 |  |
| 2025-12-10 05:05:17 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.080 |  |
| 2025-12-10 05:07:50 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.191 |  |
| 2025-12-10 05:06:28 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.255 |  |
| 2025-12-10 05:09:05 | Padiyathalawa (Maduru Oya) | 1.74 | 🟢 Normal | -126.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)