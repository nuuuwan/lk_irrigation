# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_22:08:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 22:08:49 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:08:02 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.010 |  |
| 2025-12-03 22:07:41 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2025-12-03 22:06:50 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.076 |  |
| 2025-12-03 22:06:50 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2025-12-03 22:06:35 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:06:32 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:06:24 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:04:54 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.050 |  |
| 2025-12-03 22:04:48 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.011 |  |
| 2025-12-03 22:04:37 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:04:03 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.056 |  |
| 2025-12-03 22:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2025-12-03 22:03:30 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:57 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:50 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:45 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 22:02:40 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:31 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:11 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:11 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-03 22:02:09 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:09 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:01:19 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:01:12 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 22:00:44 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 22:00:11 | Thanthirimale (Malwathu Oya) | 6.76 | 🟡 Alert | -0.041 |  |
| 2025-12-03 21:18:32 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 21:15:31 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.033 |  |
| 2025-12-03 21:13:53 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 22:00:11 | Thanthirimale (Malwathu Oya) | 6.76 | 🟡 Alert | -0.041 |  |
| 2025-12-03 22:07:41 | Yaka Wewa (Ma Oya) | 1.42 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2025-12-03 21:00:44 | Dunamale (Aththanagalu Oya) | 2.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 22:02:45 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 22:00:44 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 22:01:12 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 22:02:40 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:11 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:57 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:50 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:31 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:08:49 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:02:09 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:06:32 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:04:37 | Katharagama (Menik Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:06:35 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:06:24 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:01:19 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 22:03:30 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-03 20:18:19 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.008 |  |
| 2025-12-03 22:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2025-12-03 22:02:11 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-03 22:08:02 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.010 |  |
| 2025-12-03 21:13:53 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | -0.011 |  |
| 2025-12-03 22:06:50 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2025-12-03 22:04:48 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.011 |  |
| 2025-12-03 21:05:32 | Horowpothana (Yan Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2025-12-03 21:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.021 |  |
| 2025-12-03 21:15:31 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.033 |  |
| 2025-12-03 22:04:54 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.050 |  |
| 2025-12-03 22:04:03 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.056 |  |
| 2025-12-03 22:06:50 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.076 |  |
| 2025-12-03 21:04:55 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | -0.080 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)