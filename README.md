# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_22:15:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,641 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 22:15:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2025-12-27 22:11:17 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 22:10:22 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:09:15 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:08:01 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:07:37 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:07:01 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2025-12-27 22:06:52 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:06:39 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:06:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-27 22:05:23 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:05:20 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:04:35 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:04:19 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 22:04:13 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.119 |  |
| 2025-12-27 22:03:57 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:03:52 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2025-12-27 22:03:33 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:03:27 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2025-12-27 22:02:36 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-27 22:02:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:02:06 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:50 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:44 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:38 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:34 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 22:00:54 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:52 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-27 22:00:33 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:08 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 22:03:27 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2025-12-27 22:15:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2025-12-27 22:02:36 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-27 22:06:34 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-27 22:00:52 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-27 22:01:34 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 22:11:17 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 22:04:19 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:08 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:54 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:50 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:07:37 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:02:06 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:05:20 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:00:33 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:18:12 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:44 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:06:39 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:55 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:01:38 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:03:57 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:06:52 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:03:12 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:09:15 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:10:22 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-27 21:07:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:05:23 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:07:01 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2025-12-27 22:04:35 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:02:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:03:33 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:08:01 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2025-12-27 22:03:52 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2025-12-27 21:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.045 |  |
| 2025-12-27 22:04:13 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)