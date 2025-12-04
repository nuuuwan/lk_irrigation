# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_09:41:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,956 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 09:41:57 | Thanthirimale (Malwathu Oya) | 6.24 | 🟡 Alert | -0.026 |  |
| 2025-12-04 09:21:46 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-04 09:21:24 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:13:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2025-12-04 09:12:31 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:11:00 | Manampitiya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.009 |  |
| 2025-12-04 09:10:31 | Weraganthota (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.053 |  |
| 2025-12-04 09:09:22 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:09:09 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | -0.012 |  |
| 2025-12-04 09:08:42 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.018 |  |
| 2025-12-04 09:08:38 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.018 |  |
| 2025-12-04 09:07:29 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.039 |  |
| 2025-12-04 09:06:13 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:06:03 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:05:56 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.070 |  |
| 2025-12-04 09:05:36 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:05:21 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:05:19 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.201 |  |
| 2025-12-04 09:05:02 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 09:04:16 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:03:41 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:03:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.033 |  |
| 2025-12-04 09:03:15 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-04 09:02:59 | Hanwella (Kelani Ganga) | 3.91 | 🟢 Normal | -0.041 |  |
| 2025-12-04 09:02:43 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:02:26 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.128 |  |
| 2025-12-04 09:02:21 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:02:20 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:02:15 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:02:14 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.012 |  |
| 2025-12-04 09:02:09 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.011 |  |
| 2025-12-04 09:02:02 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.010 |  |
| 2025-12-04 09:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:01:20 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:01:10 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:01:02 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:00:40 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 09:41:57 | Thanthirimale (Malwathu Oya) | 6.24 | 🟡 Alert | -0.026 |  |
| 2025-12-04 09:21:46 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-04 09:05:02 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 09:02:43 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:01:10 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:12:31 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:02:21 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:07:29 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:05:21 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:06:03 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:01:21 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:01:02 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:01:20 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:06:13 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:02:20 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:09:22 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:05:36 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:02:15 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:03:41 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:21:24 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:11:00 | Manampitiya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.009 |  |
| 2025-12-04 09:02:02 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.010 |  |
| 2025-12-04 09:03:15 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-04 09:02:09 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.011 |  |
| 2025-12-04 09:02:14 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.012 |  |
| 2025-12-04 09:09:09 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | -0.012 |  |
| 2025-12-04 09:08:38 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.018 |  |
| 2025-12-04 09:08:42 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.018 |  |
| 2025-12-04 09:13:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2025-12-04 09:03:38 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.033 |  |
| 2025-12-04 09:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.039 |  |
| 2025-12-04 09:02:59 | Hanwella (Kelani Ganga) | 3.91 | 🟢 Normal | -0.041 |  |
| 2025-12-04 09:10:31 | Weraganthota (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.053 |  |
| 2025-12-04 09:05:56 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.070 |  |
| 2025-12-04 09:02:26 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.128 |  |
| 2025-12-04 09:05:19 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)