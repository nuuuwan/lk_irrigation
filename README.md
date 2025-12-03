# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_20:18:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,522 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 20:18:19 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.008 |  |
| 2025-12-03 20:17:28 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.008 |  |
| 2025-12-03 20:17:14 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:14:18 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:12:10 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.116 |  |
| 2025-12-03 20:08:40 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-03 20:07:36 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:07:29 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:06:40 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-03 20:06:17 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:05:41 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.048 |  |
| 2025-12-03 20:04:41 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | -0.062 |  |
| 2025-12-03 20:04:40 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:04:40 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.140 |  |
| 2025-12-03 20:04:21 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:04:15 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.043 |  |
| 2025-12-03 20:04:11 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:04:08 | Katharagama (Menik Ganga) | 0.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-03 20:03:45 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-03 20:03:29 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-03 20:03:26 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2025-12-03 20:03:02 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | -0.086 |  |
| 2025-12-03 20:02:45 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-03 20:02:41 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 20:02:25 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.043 |  |
| 2025-12-03 20:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-03 20:01:37 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-03 20:01:28 | Nagalagam Street (Kelani Ganga) | 1.08 | 🟢 Normal | -0.015 |  |
| 2025-12-03 20:01:19 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 20:01:17 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:00:32 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:35:33 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 18:05:04 | Thanthirimale (Malwathu Oya) | 6.91 | 🟠 Minor Flood | -0.056 |  |
| 2025-12-03 20:02:45 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-03 20:04:08 | Katharagama (Menik Ganga) | 0.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-03 20:03:45 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-03 20:06:40 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-03 20:01:19 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 20:02:41 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 20:00:32 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:07:29 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:14:18 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:05:41 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:17:14 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:04:11 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:07:36 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:04:40 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:04:21 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:06:17 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:01:17 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:18:19 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.008 |  |
| 2025-12-03 20:17:28 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.008 |  |
| 2025-12-03 20:03:29 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-03 20:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-03 20:01:37 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-03 20:01:28 | Nagalagam Street (Kelani Ganga) | 1.08 | 🟢 Normal | -0.015 |  |
| 2025-12-03 20:03:26 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2025-12-03 20:08:40 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-03 20:04:15 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.043 |  |
| 2025-12-03 20:02:25 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.043 |  |
| 2025-12-03 20:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.048 |  |
| 2025-12-03 20:04:41 | Horowpothana (Yan Oya) | 2.79 | 🟢 Normal | -0.062 |  |
| 2025-12-03 20:03:02 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | -0.086 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-03 20:12:10 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.116 |  |
| 2025-12-03 20:04:40 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.140 |  |
| 2025-12-03 18:03:18 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)