# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_17:16:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,456 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 17:16:46 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 17:15:45 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.060 |  |
| 2025-12-18 17:08:50 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:08:40 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 17:07:40 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:07:17 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:07:03 | Galgamuwa (Mee Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:06:44 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 17:05:31 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.039 |  |
| 2025-12-18 17:05:21 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-18 17:04:22 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:04:12 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.005 |  |
| 2025-12-18 17:04:04 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:03:34 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:03:21 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2025-12-18 17:03:21 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.067 |  |
| 2025-12-18 17:03:09 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:02:48 | Padiyathalawa (Maduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:34 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:29 | Siyambalanduwa (Heda Oya) | 1.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 17:02:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:15 | Manampitiya (Mahaweli Ganga) | 4.58 | 🟠 Minor Flood | 0.108 | 🔺 Rising |
| 2025-12-18 17:02:13 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 17:02:07 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-18 17:02:00 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:01:38 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:01:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.124 |  |
| 2025-12-18 17:01:25 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 17:01:17 | Weraganthota (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 17:01:13 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 17:01:12 | Thanthirimale (Malwathu Oya) | 5.32 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2025-12-18 17:01:07 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:00:49 | Horowpothana (Yan Oya) | 5.31 | 🟢 Normal | -0.011 |  |
| 2025-12-18 17:00:34 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-18 17:00:09 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:00:08 | Nakkala (Kumbukkan Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-18 16:59:21 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 17:02:15 | Manampitiya (Mahaweli Ganga) | 4.58 | 🟠 Minor Flood | 0.108 | 🔺 Rising |
| 2025-12-18 17:01:12 | Thanthirimale (Malwathu Oya) | 5.32 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2025-12-18 17:02:07 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-18 17:00:34 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-18 17:02:29 | Siyambalanduwa (Heda Oya) | 1.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 17:01:13 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 17:06:44 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-18 17:05:21 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-18 17:02:13 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 17:16:46 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 17:01:17 | Weraganthota (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 17:01:25 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 17:08:40 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 17:04:12 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.005 |  |
| 2025-12-18 17:01:38 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:00:08 | Nakkala (Kumbukkan Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:00 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:07:03 | Galgamuwa (Mee Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:03:34 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:04:04 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:34 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:07:17 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:48 | Padiyathalawa (Maduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:01:07 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:07:40 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:08:50 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-18 17:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:03:09 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:04:22 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:00:09 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-18 17:00:49 | Horowpothana (Yan Oya) | 5.31 | 🟢 Normal | -0.011 |  |
| 2025-12-18 17:03:21 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2025-12-18 16:59:21 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.024 |  |
| 2025-12-18 17:05:31 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.039 |  |
| 2025-12-18 17:15:45 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.060 |  |
| 2025-12-18 17:03:21 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.067 |  |
| 2025-12-18 17:01:27 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)