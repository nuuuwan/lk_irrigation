# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_10:24:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 10:24:16 | Weraganthota (Mahaweli Ganga) | -0.45 | 🟢 Normal | -0.122 |  |
| 2025-12-04 10:20:27 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.008 |  |
| 2025-12-04 10:20:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2025-12-04 10:12:11 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.012 |  |
| 2025-12-04 10:10:43 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:10:29 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:09:32 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:07:01 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2025-12-04 10:06:18 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:06:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2025-12-04 10:05:56 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:05:23 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:05:17 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:05:16 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2025-12-04 10:05:14 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2025-12-04 10:05:07 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:05:06 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:04:40 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 10:04:09 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:03:51 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:03:39 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.022 |  |
| 2025-12-04 10:03:19 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:03:13 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.030 |  |
| 2025-12-04 10:02:51 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:02:47 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:02:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.040 |  |
| 2025-12-04 10:02:27 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:02:10 | Manampitiya (Mahaweli Ganga) | 2.44 | 🟢 Normal | -0.082 |  |
| 2025-12-04 10:02:09 | Thanthirimale (Malwathu Oya) | 6.20 | 🟡 Alert | -0.119 |  |
| 2025-12-04 10:01:49 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.015 |  |
| 2025-12-04 10:01:39 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:01:22 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:01:18 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:01:10 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:00:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.068 |  |
| 2025-12-04 09:41:57 | Thanthirimale (Malwathu Oya) | 6.24 | 🟡 Alert | -0.119 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 10:02:09 | Thanthirimale (Malwathu Oya) | 6.20 | 🟡 Alert | -0.119 |  |
| 2025-12-04 09:05:02 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 10:04:40 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-04 10:01:18 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:01:22 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:02:51 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:03:19 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:01:39 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:05:07 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:02:27 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:05:56 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 09:06:13 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:04:09 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:05:23 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:09:32 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:01:10 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-04 10:20:27 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.008 |  |
| 2025-12-04 10:05:16 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2025-12-04 10:10:29 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:05:17 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:05:06 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:03:51 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:06:18 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:02:47 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:10:43 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2025-12-04 10:12:11 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.012 |  |
| 2025-12-04 10:01:49 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.015 |  |
| 2025-12-04 10:07:01 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2025-12-04 10:03:39 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.022 |  |
| 2025-12-04 10:06:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2025-12-04 10:03:13 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.030 |  |
| 2025-12-04 10:20:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2025-12-04 10:02:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.040 |  |
| 2025-12-04 10:05:14 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.051 |  |
| 2025-12-04 10:00:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | -0.068 |  |
| 2025-12-04 10:02:10 | Manampitiya (Mahaweli Ganga) | 2.44 | 🟢 Normal | -0.082 |  |
| 2025-12-04 10:24:16 | Weraganthota (Mahaweli Ganga) | -0.45 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)