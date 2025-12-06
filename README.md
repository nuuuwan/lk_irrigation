# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_05:13:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,319 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 05:13:17 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.008 |  |
| 2025-12-07 05:11:34 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.053 |  |
| 2025-12-07 05:10:49 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2025-12-07 05:10:49 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.076 |  |
| 2025-12-07 05:10:45 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:10:15 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.021 |  |
| 2025-12-07 05:08:00 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 05:07:41 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:07:20 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | -0.076 |  |
| 2025-12-07 05:07:10 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:06:38 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.020 |  |
| 2025-12-07 05:05:55 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-07 05:05:35 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 05:05:07 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:04:42 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-07 05:03:54 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2025-12-07 05:03:19 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:03:17 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-07 05:03:16 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-07 05:03:00 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:02:46 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.049 |  |
| 2025-12-07 05:02:41 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2025-12-07 05:02:18 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-07 05:02:01 | Thanthirimale (Malwathu Oya) | 6.27 | 🟡 Alert | -0.030 |  |
| 2025-12-07 05:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-07 05:01:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:00:59 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:00:55 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-07 05:00:20 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.053 |  |
| 2025-12-07 04:53:12 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.022 |  |
| 2025-12-07 04:39:11 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.076 |  |
| 2025-12-07 04:22:43 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2025-12-07 04:18:44 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.025 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 05:02:01 | Thanthirimale (Malwathu Oya) | 6.27 | 🟡 Alert | -0.030 |  |
| 2025-12-07 05:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2025-12-07 05:05:55 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-07 04:05:19 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-07 05:05:35 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 05:08:00 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 05:03:19 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:01:13 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:02:18 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:05:07 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:03:00 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 04:04:39 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:10:45 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:07:41 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:00:59 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 05:07:10 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 03:05:01 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.005 |  |
| 2025-12-07 05:13:17 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.008 |  |
| 2025-12-07 05:03:54 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2025-12-07 05:00:55 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-07 05:03:17 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-07 05:03:16 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-07 05:10:49 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 05:02:41 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2025-12-07 05:06:38 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.020 |  |
| 2025-12-07 05:04:42 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-07 05:10:15 | Magura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.021 |  |
| 2025-12-07 04:53:12 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.022 |  |
| 2025-12-07 05:02:46 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.049 |  |
| 2025-12-07 05:11:34 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.053 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-07 05:10:49 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.076 |  |
| 2025-12-07 05:07:20 | Glencourse (Kelani Ganga) | 10.12 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)