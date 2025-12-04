# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_05:31:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,812 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 05:31:23 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:26:27 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:22:31 | Katharagama (Menik Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:11:37 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.026 |  |
| 2025-12-04 05:10:56 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.022 |  |
| 2025-12-04 05:09:57 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2025-12-04 05:09:34 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.145 |  |
| 2025-12-04 05:06:59 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.057 |  |
| 2025-12-04 05:06:54 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:06:38 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -1.800 |  |
| 2025-12-04 05:06:31 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 05:06:18 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -1.800 |  |
| 2025-12-04 05:05:57 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-04 05:05:37 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:05:02 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.048 |  |
| 2025-12-04 05:04:36 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 05:04:07 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:04:03 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.088 |  |
| 2025-12-04 05:03:37 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 05:03:33 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:03:27 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:03:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:02:59 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2025-12-04 05:02:30 | Katharagama (Menik Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:02:29 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:02:28 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2025-12-04 05:02:06 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.370 |  |
| 2025-12-04 05:01:56 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:01:41 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | -0.033 |  |
| 2025-12-04 05:01:41 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:01:08 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:00:32 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-04 05:00:12 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.013 |  |
| 2025-12-04 04:57:16 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.088 |  |
| 2025-12-04 04:56:02 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:49:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.370 |  |
| 2025-12-04 04:48:32 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-04 04:42:09 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:39:27 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-04 04:39:09 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 04:01:46 | Thanthirimale (Malwathu Oya) | 6.48 | 🟡 Alert | -0.049 |  |
| 2025-12-04 05:05:57 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-04 05:00:32 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-04 05:03:37 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 05:04:36 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 05:06:31 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 05:05:37 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:31:23 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:26:27 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:22:31 | Katharagama (Menik Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:06:54 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:01:41 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:03:33 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:01:08 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:01:56 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 05:04:07 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:02:06 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:03:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:02:29 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:03:27 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.010 |  |
| 2025-12-04 05:00:12 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.013 |  |
| 2025-12-04 05:09:57 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2025-12-04 05:02:59 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2025-12-04 05:10:56 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.022 |  |
| 2025-12-04 05:11:37 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.026 |  |
| 2025-12-04 05:01:41 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | -0.033 |  |
| 2025-12-04 05:05:02 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | -0.048 |  |
| 2025-12-04 05:02:28 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2025-12-04 05:06:59 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.057 |  |
| 2025-12-04 05:04:03 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.088 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-04 05:09:34 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | -0.145 |  |
| 2025-12-04 05:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.370 |  |
| 2025-12-04 05:06:38 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -1.800 |  |
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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)