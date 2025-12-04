# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_06:12:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,846 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 06:12:22 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-04 06:12:09 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.009 |  |
| 2025-12-04 06:10:14 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.045 |  |
| 2025-12-04 06:09:32 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:09:19 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:08:50 | Thanthirimale (Malwathu Oya) | 6.39 | 🟡 Alert | -1.756 |  |
| 2025-12-04 06:08:42 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | -0.082 |  |
| 2025-12-04 06:07:59 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:07:45 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.049 |  |
| 2025-12-04 06:07:28 | Thanthirimale (Malwathu Oya) | 6.43 | 🟡 Alert | -1.756 |  |
| 2025-12-04 06:07:19 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.019 |  |
| 2025-12-04 06:06:53 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.017 |  |
| 2025-12-04 06:06:32 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2025-12-04 06:06:14 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2025-12-04 06:05:10 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.115 |  |
| 2025-12-04 06:05:00 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.030 |  |
| 2025-12-04 06:04:40 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 06:04:29 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:04:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:04:18 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-04 06:04:17 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:04:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-04 06:03:51 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:03:45 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 06:03:39 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:03:39 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:01:59 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2025-12-04 06:01:51 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-04 06:01:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:01:33 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:01:28 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.116 |  |
| 2025-12-04 06:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.223 |  |
| 2025-12-04 06:01:12 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 06:08:50 | Thanthirimale (Malwathu Oya) | 6.39 | 🟡 Alert | -1.756 |  |
| 2025-12-04 06:04:18 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-04 06:03:45 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 06:04:02 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-04 06:12:22 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-04 06:04:40 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 06:01:33 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:03:39 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:09:19 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:07:59 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:04:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:03:51 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:01:37 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:09:32 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:04:17 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:03:39 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:01:12 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:04:29 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 06:12:09 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.009 |  |
| 2025-12-04 06:06:14 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2025-12-04 06:01:59 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2025-12-04 06:06:53 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.017 |  |
| 2025-12-04 06:07:19 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.019 |  |
| 2025-12-04 06:01:51 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-04 06:06:32 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2025-12-04 06:05:00 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.030 |  |
| 2025-12-04 06:10:14 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.045 |  |
| 2025-12-04 06:07:45 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.049 |  |
| 2025-12-04 06:08:42 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | -0.082 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-04 06:05:10 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.115 |  |
| 2025-12-04 06:01:28 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.116 |  |
| 2025-12-04 06:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.223 |  |
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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)