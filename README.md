# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_10:10:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,505 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 10:10:25 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2025-12-07 10:10:06 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:09:32 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-07 10:07:27 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2025-12-07 10:06:20 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:06:14 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.011 |  |
| 2025-12-07 10:05:30 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.061 |  |
| 2025-12-07 10:05:27 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.048 |  |
| 2025-12-07 10:05:20 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-07 10:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.020 |  |
| 2025-12-07 10:04:46 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2025-12-07 10:04:35 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-07 10:04:20 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-07 10:04:12 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:03:51 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:03:44 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:03:43 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.019 |  |
| 2025-12-07 10:03:30 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:03:12 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.070 |  |
| 2025-12-07 10:02:45 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:02:42 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:02:41 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:02:40 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.042 |  |
| 2025-12-07 10:02:38 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2025-12-07 10:02:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.055 |  |
| 2025-12-07 10:02:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:45 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:45 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:38 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.061 |  |
| 2025-12-07 10:01:31 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 10:01:26 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:08 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 09:13:03 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 09:00:15 | Thanthirimale (Malwathu Oya) | 6.08 | 🟡 Alert | -0.056 |  |
| 2025-12-07 09:04:26 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-07 10:09:32 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-07 09:05:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 10:01:45 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:03:44 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:02:42 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:06:20 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:04:12 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:02:45 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:45 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:02:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:01:26 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:03:30 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:10:06 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:03:51 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:02:41 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 10:04:46 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2025-12-07 10:04:20 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-07 10:04:35 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-07 10:01:31 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 10:01:08 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-07 10:06:14 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.011 |  |
| 2025-12-07 09:04:59 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.019 |  |
| 2025-12-07 10:03:43 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.019 |  |
| 2025-12-07 10:05:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.020 |  |
| 2025-12-07 10:05:20 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-07 10:07:27 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2025-12-07 10:02:38 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2025-12-07 10:02:40 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.042 |  |
| 2025-12-07 10:05:27 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.048 |  |
| 2025-12-07 10:02:11 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.055 |  |
| 2025-12-07 10:05:30 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.061 |  |
| 2025-12-07 10:01:38 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.061 |  |
| 2025-12-07 10:10:25 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2025-12-07 10:03:12 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)