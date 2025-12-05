# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_20:16:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,202 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 20:16:20 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:15:11 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 116.129 | 🔺 Rising |
| 2025-12-05 20:14:40 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 116.129 | 🔺 Rising |
| 2025-12-05 20:11:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-05 20:09:44 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2025-12-05 20:09:31 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2025-12-05 20:09:19 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 20:09:03 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:07:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.028 |  |
| 2025-12-05 20:06:23 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:06:21 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:06:15 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:06:10 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:05:50 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-05 20:05:40 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-05 20:05:11 | Thanthirimale (Malwathu Oya) | 6.61 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2025-12-05 20:04:27 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:04:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 20:03:37 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:03:21 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:02:43 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:02:40 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-05 20:02:40 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2025-12-05 20:02:38 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-05 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:02:17 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-05 20:02:01 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2025-12-05 20:01:45 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:01:44 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:01:35 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:01:30 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:00:27 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 20:00:11 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 20:05:11 | Thanthirimale (Malwathu Oya) | 6.61 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2025-12-05 20:15:11 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 116.129 | 🔺 Rising |
| 2025-12-05 20:02:01 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2025-12-05 20:02:40 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-05 20:09:44 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2025-12-05 20:11:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 20:00:11 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-05 20:04:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 20:05:40 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 20:09:19 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 18:02:10 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 20:00:27 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:02:43 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:01:35 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:16:20 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:06:21 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:01:45 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:06:15 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:06:23 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:09:03 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:01:30 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:01:44 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:06:10 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:04:27 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:03:37 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:06:21 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 20:05:50 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-05 20:02:38 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-05 20:02:17 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-05 20:09:31 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2025-12-05 20:02:40 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2025-12-05 20:07:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.028 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)