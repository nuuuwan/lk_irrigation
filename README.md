# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_05:11:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,158 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 05:11:04 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.186 |  |
| 2025-12-08 05:09:32 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.867 | 🔺 Rising |
| 2025-12-08 05:08:41 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-08 05:08:21 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:08:09 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.867 | 🔺 Rising |
| 2025-12-08 05:08:07 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-08 05:05:41 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2025-12-08 05:05:33 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-08 05:05:04 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.061 |  |
| 2025-12-08 05:04:44 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2025-12-08 05:04:34 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-08 05:04:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:04:05 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-08 05:03:33 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 05:03:26 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:03:08 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 05:02:55 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:02:55 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -1.496 |  |
| 2025-12-08 05:02:44 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-08 05:02:31 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:02:31 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-08 05:02:28 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-08 05:02:22 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-08 05:01:18 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.075 |  |
| 2025-12-08 05:00:20 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 04:58:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 13.091 | 🔺 Rising |
| 2025-12-08 04:57:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 13.091 | 🔺 Rising |
| 2025-12-08 04:50:05 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | -1.496 |  |
| 2025-12-08 04:24:59 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 04:21:43 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.026 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 04:58:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 13.091 | 🔺 Rising |
| 2025-12-08 05:09:32 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.867 | 🔺 Rising |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-08 05:04:44 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2025-12-08 05:04:05 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-08 05:05:33 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-08 05:04:34 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-08 05:02:28 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-08 05:02:44 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-08 05:08:07 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 05:03:33 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 05:00:20 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:02:31 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:03:26 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:02:55 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 04:02:50 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:04:08 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 03:03:37 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:08:21 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 04:09:33 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2025-12-08 05:08:41 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-08 05:03:08 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 05:02:31 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-08 04:04:39 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2025-12-08 05:02:22 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-08 05:05:41 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2025-12-08 04:07:23 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2025-12-08 04:02:24 | Thanthirimale (Malwathu Oya) | 4.92 | 🟢 Normal | -0.039 |  |
| 2025-12-08 05:05:04 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.061 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |
| 2025-12-08 05:01:18 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.075 |  |
| 2025-12-08 04:05:27 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.172 |  |
| 2025-12-08 05:11:04 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.186 |  |
| 2025-12-08 05:02:55 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -1.496 |  |
| 2025-12-08 04:07:58 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)