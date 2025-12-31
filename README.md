# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_17:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 17:03:50 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:03:39 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 17:03:28 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:03:23 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:02:56 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2025-12-31 17:02:54 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-31 17:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.032 |  |
| 2025-12-31 17:02:32 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:02:31 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 17:02:21 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.051 |  |
| 2025-12-31 17:01:53 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:01:36 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 17:01:24 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.040 |  |
| 2025-12-31 17:01:20 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 17:01:11 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 17:00:48 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-31 17:00:44 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:00:41 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:00:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-31 17:00:07 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:58:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.015 |  |
| 2025-12-31 16:17:45 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2025-12-31 16:12:13 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:12:07 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:10:59 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 16:07:44 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.009 |  |
| 2025-12-31 16:07:37 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:06:48 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:06:24 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 17:02:56 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2025-12-31 17:00:48 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-31 16:02:32 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 17:03:39 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-31 17:00:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-31 17:02:31 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 17:01:11 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 17:01:20 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 17:01:36 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 16:10:59 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 17:01:53 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:00:07 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:03:23 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:04:01 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:12:07 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:12:13 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:06:24 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:07:37 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:00:44 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:03:28 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:03:50 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:02:32 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:05:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 17:00:41 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:04:30 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:00:27 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-31 16:07:44 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.009 |  |
| 2025-12-31 16:05:06 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-31 17:02:54 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:03:22 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-31 16:58:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.015 |  |
| 2025-12-31 17:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.032 |  |
| 2025-12-31 17:01:24 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.040 |  |
| 2025-12-31 17:02:21 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.051 |  |
| 2025-12-31 16:02:43 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.108 |  |
| 2025-12-31 16:00:51 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.517 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)