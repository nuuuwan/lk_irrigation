# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_03:16:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,745 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 03:16:37 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.005 |  |
| 2025-12-04 03:16:12 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:16:08 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:15:13 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -36.000 |  |
| 2025-12-04 03:15:12 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -36.000 |  |
| 2025-12-04 03:10:54 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.017 |  |
| 2025-12-04 03:10:27 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:09:40 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.057 |  |
| 2025-12-04 03:09:33 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | -0.082 |  |
| 2025-12-04 03:08:22 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:07:50 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:07:28 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:06:50 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 03:06:11 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.018 |  |
| 2025-12-04 03:05:42 | Yaka Wewa (Ma Oya) | 1.39 | 🟢 Normal | -0.305 |  |
| 2025-12-04 03:05:00 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.048 |  |
| 2025-12-04 03:04:31 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:04:27 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:04:21 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-04 03:03:56 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -2.880 |  |
| 2025-12-04 03:03:28 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-04 03:03:18 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.68 | 🟢 Normal | -2.880 |  |
| 2025-12-04 03:03:07 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-04 03:03:00 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:02:53 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 03:02:45 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2025-12-04 03:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -2.880 |  |
| 2025-12-04 03:02:16 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-04 03:01:59 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:01:54 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:01:44 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.025 |  |
| 2025-12-04 03:00:34 | Thanthirimale (Malwathu Oya) | 6.53 | 🟡 Alert | -0.051 |  |
| 2025-12-04 03:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.595 |  |
| 2025-12-04 02:58:19 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.595 |  |
| 2025-12-04 02:32:39 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 02:32:03 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.019 |  |
| 2025-12-04 02:25:29 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -0.082 |  |
| 2025-12-04 02:21:26 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 03:00:34 | Thanthirimale (Malwathu Oya) | 6.53 | 🟡 Alert | -0.051 |  |
| 2025-12-04 03:03:07 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-04 03:02:16 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-04 03:06:50 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 03:02:53 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 03:07:28 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:04:31 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 02:10:20 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:08:22 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:16:12 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:03:00 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:01:54 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:16:08 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:03:56 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:03:18 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:10:27 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:04:27 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:01:59 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 03:16:37 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.005 |  |
| 2025-12-03 20:18:19 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.008 |  |
| 2025-12-04 03:02:45 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2025-12-04 03:04:21 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-04 03:10:54 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.017 |  |
| 2025-12-04 03:06:11 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.018 |  |
| 2025-12-04 03:03:28 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-04 03:01:44 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.025 |  |
| 2025-12-04 03:05:00 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.048 |  |
| 2025-12-04 03:09:40 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.057 |  |
| 2025-12-04 03:09:33 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | -0.082 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-04 03:05:42 | Yaka Wewa (Ma Oya) | 1.39 | 🟢 Normal | -0.305 |  |
| 2025-12-04 03:00:20 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.595 |  |
| 2025-12-04 03:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -2.880 |  |
| 2025-12-03 18:03:18 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |
| 2025-12-04 03:15:13 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)