# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_16:42:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,384 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 16:42:44 | Thanthirimale (Malwathu Oya) | 7.05 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-03 16:18:18 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.017 |  |
| 2025-12-03 16:15:52 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2025-12-03 16:14:02 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.017 |  |
| 2025-12-03 16:12:58 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.043 |  |
| 2025-12-03 16:11:47 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:10:35 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.018 |  |
| 2025-12-03 16:09:42 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:08:17 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:08:10 | Nagalagam Street (Kelani Ganga) | 1.23 | 🟡 Alert | -0.072 |  |
| 2025-12-03 16:06:53 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:06:34 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:05:54 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:05:41 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.966 |  |
| 2025-12-03 16:05:41 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.087 |  |
| 2025-12-03 16:04:37 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:04:07 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:03:58 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-03 16:03:56 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:03:44 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.063 |  |
| 2025-12-03 16:03:44 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:03:43 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:03:38 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:03:31 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-03 16:03:01 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:02:59 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.083 |  |
| 2025-12-03 16:02:29 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:02:03 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:02:03 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:01:17 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.150 |  |
| 2025-12-03 16:01:10 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.024 |  |
| 2025-12-03 16:00:22 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.053 |  |
| 2025-12-03 16:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:00:06 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 16:42:44 | Thanthirimale (Malwathu Oya) | 7.05 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-03 16:08:10 | Nagalagam Street (Kelani Ganga) | 1.23 | 🟡 Alert | -0.072 |  |
| 2025-12-03 16:03:58 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-03 15:01:03 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:09:42 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:03:43 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:03:56 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:08:17 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:02:29 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:02:03 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:06:53 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:00:06 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:15:52 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2025-12-03 16:05:54 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:04:37 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:11:47 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:03:38 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:04:07 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:02:03 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:03:44 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:03:01 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:06:34 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:02:59 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-03 16:18:18 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.017 |  |
| 2025-12-03 16:14:02 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.017 |  |
| 2025-12-03 16:10:35 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.018 |  |
| 2025-12-03 16:03:31 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-03 16:01:10 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.024 |  |
| 2025-12-03 16:12:58 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.043 |  |
| 2025-12-03 16:00:22 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.053 |  |
| 2025-12-03 16:03:44 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.063 |  |
| 2025-12-03 16:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | -0.083 |  |
| 2025-12-03 16:05:41 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.087 |  |
| 2025-12-03 16:01:17 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | -0.150 |  |
| 2025-12-03 16:05:41 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.966 |  |

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)