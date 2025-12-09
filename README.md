# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_22:09:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,641 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 22:09:27 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:08:34 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:08:23 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.078 |  |
| 2025-12-09 22:07:21 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:07:19 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-09 22:06:09 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:06:01 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2025-12-09 22:05:28 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:05:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:05:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2025-12-09 22:05:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2025-12-09 22:05:02 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:04:14 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-09 22:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 22:03:47 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:03:41 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:03:37 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.021 |  |
| 2025-12-09 22:03:34 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:03:26 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-09 22:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 22:02:17 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:02:08 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 22:02:04 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | -0.068 |  |
| 2025-12-09 22:01:54 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2025-12-09 22:01:49 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:01:28 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.078 |  |
| 2025-12-09 22:01:02 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-09 22:00:32 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:26:10 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:22:18 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.078 |  |
| 2025-12-09 21:20:12 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 21:01:33 | Urawa (Nilwala Ganga) | 2.80 | 🟡 Alert | -0.305 |  |
| 2025-12-09 22:01:54 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 22:04:14 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-09 22:01:02 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-09 21:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 22:07:19 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-09 22:02:08 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 22:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 22:04:06 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 22:03:34 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:03:47 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:02:17 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:09:27 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:05:28 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:00:32 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:26:10 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:08:34 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:07:21 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:05:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:06:09 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:03:41 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 22:05:02 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:20:12 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.008 |  |
| 2025-12-09 22:05:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2025-12-09 22:03:26 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 22:03:37 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.021 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-09 22:06:01 | Rathnapura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2025-12-09 22:05:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2025-12-09 21:02:42 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.065 |  |
| 2025-12-09 22:02:04 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | -0.068 |  |
| 2025-12-09 22:08:23 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.078 |  |
| 2025-12-09 22:01:28 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)