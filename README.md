# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_15:07:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 15:07:32 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 15:07:23 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:07:05 | Thanthirimale (Malwathu Oya) | 5.95 | 🟡 Alert | -0.063 |  |
| 2025-12-04 15:07:00 | Weraganthota (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.579 | 🔺 Rising |
| 2025-12-04 15:05:55 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2025-12-04 15:05:55 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-04 15:05:42 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.019 |  |
| 2025-12-04 15:05:31 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-04 15:05:24 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2025-12-04 15:04:38 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:04:35 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:04:10 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:58 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:45 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2025-12-04 15:03:20 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:15 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:08 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:03 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.060 |  |
| 2025-12-04 15:02:42 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:37 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:28 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-04 15:02:13 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:06 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-04 15:02:04 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:02 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:01 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 15:01:54 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2025-12-04 15:01:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-04 15:01:20 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.030 |  |
| 2025-12-04 15:01:14 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:01:11 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2025-12-04 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:00:50 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-04 15:00:10 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:11:21 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:11:20 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:10:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.069 |  |
| 2025-12-04 14:10:16 | Thanthirimale (Malwathu Oya) | 6.01 | 🟡 Alert | -0.063 |  |
| 2025-12-04 14:09:52 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-04 14:08:55 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-04 14:08:38 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 15:07:05 | Thanthirimale (Malwathu Oya) | 5.95 | 🟡 Alert | -0.063 |  |
| 2025-12-04 15:07:00 | Weraganthota (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.579 | 🔺 Rising |
| 2025-12-04 15:03:45 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2025-12-04 15:02:28 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-04 15:05:55 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-04 15:05:31 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-04 15:02:01 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 15:07:32 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:37 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:04:38 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:08 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:07:23 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:04 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:42 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:04:10 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:20 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:13 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:02 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:04:35 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:58 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:03:15 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:01:14 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 15:02:06 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-04 14:08:38 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 15:00:10 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-04 15:00:50 | Nakkala (Kumbukkan Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-04 15:05:42 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.019 |  |
| 2025-12-04 15:05:55 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2025-12-04 15:01:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-04 15:01:54 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2025-12-04 15:01:11 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2025-12-04 15:01:20 | Ellagawa (Kalu Ganga) | 5.44 | 🟢 Normal | -0.030 |  |
| 2025-12-04 15:05:24 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.040 |  |
| 2025-12-04 15:03:03 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.060 |  |
| 2025-12-04 14:10:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.069 |  |
| 2025-12-04 14:06:23 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)