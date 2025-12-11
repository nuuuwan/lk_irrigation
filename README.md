# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_10:07:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 10:07:59 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:07:45 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.009 |  |
| 2025-12-11 10:07:21 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2025-12-11 10:06:33 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:06:18 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:06:02 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:06:01 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.050 |  |
| 2025-12-11 10:05:52 | Yaka Wewa (Ma Oya) | 1.38 | 🟢 Normal | -0.018 |  |
| 2025-12-11 10:05:22 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:05:20 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:04:51 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.117 |  |
| 2025-12-11 10:04:47 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.162 |  |
| 2025-12-11 10:04:26 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:04:16 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.030 |  |
| 2025-12-11 10:04:16 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:03:53 | Thanthirimale (Malwathu Oya) | 4.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 10:03:33 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.030 |  |
| 2025-12-11 10:03:26 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:03:19 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:03:02 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:55 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:49 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.040 |  |
| 2025-12-11 10:02:31 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:29 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2025-12-11 10:02:27 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-11 10:02:13 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.070 |  |
| 2025-12-11 10:02:10 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 10:02:10 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.092 |  |
| 2025-12-11 10:01:47 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:01:33 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:00:18 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:00:11 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:00:10 | Horowpothana (Yan Oya) | 4.63 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 10:03:53 | Thanthirimale (Malwathu Oya) | 4.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-11 09:03:14 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 09:01:31 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 10:02:10 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 10:02:10 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:00:11 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:06:33 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:31 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:49 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 09:02:42 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:03:02 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:01:47 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:03:26 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:07:59 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:00:18 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:03:19 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:02:55 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:06:02 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:05:22 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:01:33 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 10:07:45 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.009 |  |
| 2025-12-11 10:06:18 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:04:16 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:04:26 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:05:20 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-11 10:07:21 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2025-12-11 10:05:52 | Yaka Wewa (Ma Oya) | 1.38 | 🟢 Normal | -0.018 |  |
| 2025-12-11 10:02:29 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2025-12-11 10:00:10 | Horowpothana (Yan Oya) | 4.63 | 🟢 Normal | -0.020 |  |
| 2025-12-11 10:03:33 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.030 |  |
| 2025-12-11 10:04:16 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.030 |  |
| 2025-12-11 10:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.040 |  |
| 2025-12-11 10:06:01 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.050 |  |
| 2025-12-11 10:02:27 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-11 10:02:13 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.070 |  |
| 2025-12-11 10:02:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.092 |  |
| 2025-12-11 10:04:51 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.117 |  |
| 2025-12-11 10:04:47 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)