# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_18:09:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 18:09:27 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 18:07:28 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:06:53 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:06:44 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:05:52 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.087 |  |
| 2025-12-10 18:05:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2025-12-10 18:05:43 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:04:56 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 18:04:44 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-10 18:04:09 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:04:04 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:04:00 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:03:51 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:03:35 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:03:27 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:03:21 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:03:21 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2025-12-10 18:03:15 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:02:56 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:02:50 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 18:02:49 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:02:31 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-10 18:02:21 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 18:02:15 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 18:01:25 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 18:01:20 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:01:16 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:01:02 | Yaka Wewa (Ma Oya) | 1.82 | 🟢 Normal | -0.080 |  |
| 2025-12-10 18:00:56 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:00:14 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.005 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 17:19:35 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 18:02:31 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 18:01:25 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 18:09:27 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-10 18:04:56 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 18:02:21 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 18:02:50 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 18:02:15 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:04:04 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-10 17:04:27 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:05:43 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:04:09 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:01:16 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:14 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.005 |  |
| 2025-12-10 18:04:44 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.009 |  |
| 2025-12-10 18:07:28 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:03:35 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:02:49 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:03:21 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:02:56 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:01:20 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-10 17:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-10 18:03:15 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-10 17:06:33 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.011 |  |
| 2025-12-10 18:03:21 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2025-12-10 18:03:51 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:03:27 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:06:53 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:04:00 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:06:44 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:00:56 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.020 |  |
| 2025-12-10 18:05:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2025-12-10 18:01:02 | Yaka Wewa (Ma Oya) | 1.82 | 🟢 Normal | -0.080 |  |
| 2025-12-10 18:05:52 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.087 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)