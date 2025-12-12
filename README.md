# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_05:33:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,569 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 05:33:28 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.014 |  |
| 2025-12-12 05:21:19 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-12 05:19:30 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.078 |  |
| 2025-12-12 05:14:53 | Horowpothana (Yan Oya) | 4.65 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-12 05:11:29 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.112 |  |
| 2025-12-12 05:10:38 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-12 05:09:12 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-12 05:07:09 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -132.000 |  |
| 2025-12-12 05:07:06 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -132.000 |  |
| 2025-12-12 05:06:42 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:05:47 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.163 |  |
| 2025-12-12 05:05:27 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.090 |  |
| 2025-12-12 05:05:19 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:05:13 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-12 05:04:58 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 05:04:58 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.057 |  |
| 2025-12-12 05:04:12 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-12 05:04:09 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-12 05:03:04 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.052 |  |
| 2025-12-12 05:02:13 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:02:11 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:02:00 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 05:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-12 05:01:26 | Yaka Wewa (Ma Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2025-12-12 05:01:11 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2025-12-12 05:01:11 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:00:59 | Moraketiya (Walawe Ganga) | 1.52 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-12 05:00:39 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-12 05:00:27 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 04:37:09 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.056 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 04:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-12 05:14:53 | Horowpothana (Yan Oya) | 4.65 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 04:02:57 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2025-12-12 05:01:11 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2025-12-12 05:00:39 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-12 05:04:12 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-12 05:21:19 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-12 05:10:38 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-12 05:05:13 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-12 05:09:12 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-12 05:04:09 | Siyambalanduwa (Heda Oya) | 1.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-12 05:02:00 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 05:00:59 | Moraketiya (Walawe Ganga) | 1.52 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-12 05:00:27 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 05:04:58 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 05:01:11 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:02:11 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 04:02:30 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:02:13 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:05:19 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:06:42 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-12 05:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-12 05:33:28 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.014 |  |
| 2025-12-12 05:01:26 | Yaka Wewa (Ma Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-12 04:03:40 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2025-12-12 05:03:04 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.052 |  |
| 2025-12-12 05:04:58 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.057 |  |
| 2025-12-12 05:19:30 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.078 |  |
| 2025-12-12 05:05:27 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | -0.090 |  |
| 2025-12-12 04:11:22 | Thaldena (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.101 |  |
| 2025-12-12 05:11:29 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.112 |  |
| 2025-12-12 05:05:47 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.163 |  |
| 2025-12-12 04:03:31 | Padiyathalawa (Maduru Oya) | 2.25 | 🟢 Normal | -0.267 |  |
| 2025-12-12 05:07:09 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -132.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)