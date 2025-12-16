# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_20:11:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,774 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 20:11:44 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.028 |  |
| 2025-12-16 20:11:41 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:11:27 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2025-12-16 20:11:13 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:10:38 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:10:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:08:56 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 20:08:44 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:08:08 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:07:50 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-16 20:07:42 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:07:25 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:07:04 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:05:51 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 20:05:28 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:56 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:54 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:39 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:17 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:03:49 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:03:32 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:03:26 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:03:17 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2025-12-16 20:03:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 20:03:08 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2025-12-16 20:02:42 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:02:24 | Yaka Wewa (Ma Oya) | 1.48 | 🟢 Normal | -0.040 |  |
| 2025-12-16 20:02:19 | Horowpothana (Yan Oya) | 5.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 20:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.134 |  |
| 2025-12-16 20:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:01:59 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:01:58 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:01:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:01:46 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:01:22 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:00:43 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:00:23 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 20:07:50 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-16 20:03:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 20:05:51 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 20:02:19 | Horowpothana (Yan Oya) | 5.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 20:08:56 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 20:07:25 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:01:22 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:56 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:01:58 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:11:41 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:07:42 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:08:44 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:01:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:03:26 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:39 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:08:08 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:54 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:11:13 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:03:49 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:17 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:10:38 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:00:43 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:00:23 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:02:42 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:16:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:11:27 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2025-12-16 20:07:04 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:03:32 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:01:59 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:01:46 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:03:17 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2025-12-16 20:11:44 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.028 |  |
| 2025-12-16 20:03:08 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2025-12-16 20:02:24 | Yaka Wewa (Ma Oya) | 1.48 | 🟢 Normal | -0.040 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 20:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.134 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)