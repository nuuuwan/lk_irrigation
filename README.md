# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_12:13:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 12:13:39 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:13:27 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.008 |  |
| 2025-12-05 12:09:05 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:08:37 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.072 |  |
| 2025-12-05 12:08:28 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:08:15 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:07:51 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:07:07 | Weraganthota (Mahaweli Ganga) | -0.70 | 🟢 Normal | -0.326 |  |
| 2025-12-05 12:06:40 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.069 |  |
| 2025-12-05 12:06:04 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.039 |  |
| 2025-12-05 12:06:03 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:05:55 | Thanthirimale (Malwathu Oya) | 6.32 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2025-12-05 12:05:52 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:05:26 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.050 |  |
| 2025-12-05 12:04:40 | Katharagama (Menik Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-05 12:04:26 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:04:23 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:04:21 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 12:04:10 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.041 |  |
| 2025-12-05 12:04:06 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.060 |  |
| 2025-12-05 12:03:54 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:02:56 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:02:39 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.011 |  |
| 2025-12-05 12:02:22 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-05 12:02:21 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:02:20 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.119 |  |
| 2025-12-05 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.080 |  |
| 2025-12-05 12:02:13 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:02:02 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 12:01:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-05 12:01:52 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.013 |  |
| 2025-12-05 12:01:46 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.041 |  |
| 2025-12-05 12:01:32 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:01:14 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:01:07 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:00:45 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:00:21 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-05 11:58:15 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 12:05:55 | Thanthirimale (Malwathu Oya) | 6.32 | 🟡 Alert | 0.080 | 🔺 Rising |
| 2025-12-05 12:01:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-05 12:04:21 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 11:58:15 | Manampitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-05 12:02:02 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 12:01:14 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:01:07 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:00:45 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:13:39 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:02:56 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:02:13 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:06:03 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:01:32 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:08:15 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:05:52 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:04:23 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 12:13:27 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | -0.008 |  |
| 2025-12-05 12:08:28 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:07:51 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:04:26 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:00:21 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:03:54 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-05 12:02:39 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.011 |  |
| 2025-12-05 12:02:22 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-05 12:01:52 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.013 |  |
| 2025-12-05 12:04:40 | Katharagama (Menik Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2025-12-05 12:06:04 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.039 |  |
| 2025-12-05 12:01:46 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.041 |  |
| 2025-12-05 12:04:10 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.041 |  |
| 2025-12-05 12:05:26 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.050 |  |
| 2025-12-05 12:04:06 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.060 |  |
| 2025-12-05 12:06:40 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.069 |  |
| 2025-12-05 12:08:37 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.072 |  |
| 2025-12-05 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | -0.080 |  |
| 2025-12-05 12:02:20 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | -0.119 |  |
| 2025-12-05 12:07:07 | Weraganthota (Mahaweli Ganga) | -0.70 | 🟢 Normal | -0.326 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)