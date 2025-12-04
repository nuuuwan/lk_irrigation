# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_08:01:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 08:01:38 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:35 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:18 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:00:31 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:59:47 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:38:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.086 |  |
| 2025-12-04 07:24:28 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-04 07:17:51 | Thanthirimale (Malwathu Oya) | 6.33 | 🟡 Alert | -0.052 |  |
| 2025-12-04 07:17:01 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.036 |  |
| 2025-12-04 07:12:24 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2025-12-04 07:11:33 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:10:55 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:10:25 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:10:06 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2025-12-04 07:09:52 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:07:51 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:07:13 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.125 |  |
| 2025-12-04 07:07:02 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.040 |  |
| 2025-12-04 07:06:14 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 07:05:54 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.011 |  |
| 2025-12-04 07:05:43 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.098 |  |
| 2025-12-04 07:05:12 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.002 |  |
| 2025-12-04 07:05:10 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.047 |  |
| 2025-12-04 07:04:58 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:04:24 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-04 07:04:01 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.051 |  |
| 2025-12-04 07:03:55 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 07:03:40 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2025-12-04 07:03:15 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.010 |  |
| 2025-12-04 07:03:09 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.022 |  |
| 2025-12-04 07:02:48 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-04 07:02:39 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 07:17:51 | Thanthirimale (Malwathu Oya) | 6.33 | 🟡 Alert | -0.052 |  |
| 2025-12-04 07:02:18 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-04 07:06:14 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 07:03:55 | Katharagama (Menik Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 07:24:28 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-04 07:11:33 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:09:52 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:02:39 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:10:55 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.000 |  |
| 2025-12-04 08:00:31 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:01:15 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:07:51 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:10:25 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:04:58 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:59:47 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-04 07:05:12 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.002 |  |
| 2025-12-04 07:12:24 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.009 |  |
| 2025-12-04 07:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-04 07:02:04 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:35 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:09 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:38 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-04 08:01:18 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.010 |  |
| 2025-12-04 07:03:40 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2025-12-04 07:05:54 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.011 |  |
| 2025-12-04 07:10:06 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2025-12-04 07:04:24 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-04 07:03:09 | Hanwella (Kelani Ganga) | 3.99 | 🟢 Normal | -0.022 |  |
| 2025-12-04 07:17:01 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | -0.036 |  |
| 2025-12-04 07:07:02 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.040 |  |
| 2025-12-04 07:05:10 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.047 |  |
| 2025-12-04 07:04:01 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.051 |  |
| 2025-12-04 07:38:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.086 |  |
| 2025-12-04 07:05:43 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.098 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-04 07:07:13 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)