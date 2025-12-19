# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_05:31:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,881 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 05:31:52 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:21:41 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:21:13 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:14:26 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-19 05:11:20 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2025-12-19 05:10:36 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:09:49 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 05:08:05 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:06:53 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:06:30 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2025-12-19 05:05:56 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:05:55 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2025-12-19 05:05:18 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:05:00 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2025-12-19 05:04:37 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:04:35 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 05:03:57 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:03:53 | Manampitiya (Mahaweli Ganga) | 4.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-19 05:03:52 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:03:11 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:02:38 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:02:30 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 05:02:27 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.020 |  |
| 2025-12-19 05:02:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:02:04 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:01:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2025-12-19 05:01:26 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:01:11 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:00:41 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:59:25 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.006 |  |
| 2025-12-19 04:49:12 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 05:03:53 | Manampitiya (Mahaweli Ganga) | 4.95 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-19 05:06:30 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-19 04:03:09 | Horowpothana (Yan Oya) | 5.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 05:04:35 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-19 05:09:49 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 05:02:30 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 05:14:26 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-19 04:49:12 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-19 05:02:06 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:01:26 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:31:52 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:02:01 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:03:11 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:02:38 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:10:36 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:04:37 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:00:41 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:08:05 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:05:18 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:05:56 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:21:41 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:01:11 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-19 04:59:25 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.006 |  |
| 2025-12-19 05:05:55 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2025-12-19 05:11:20 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2025-12-19 05:03:57 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:03:52 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:02:04 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:06:53 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-19 05:05:00 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2025-12-19 05:02:27 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.020 |  |
| 2025-12-19 05:01:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2025-12-19 04:19:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.031 |  |
| 2025-12-19 03:03:18 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.051 |  |
| 2025-12-19 04:04:34 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)