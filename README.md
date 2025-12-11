# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_14:18:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,049 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 14:18:30 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-11 14:12:12 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.031 |  |
| 2025-12-11 14:10:30 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:09:24 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2025-12-11 14:07:07 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 14:06:55 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:06:20 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:06:15 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-11 14:06:05 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:05:50 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:05:29 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2025-12-11 14:05:10 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-11 14:05:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 14:04:38 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-11 14:04:20 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.020 |  |
| 2025-12-11 14:04:12 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2025-12-11 14:04:10 | Horowpothana (Yan Oya) | 4.53 | 🟢 Normal | -0.019 |  |
| 2025-12-11 14:04:10 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:03:34 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:03:26 | Thanthirimale (Malwathu Oya) | 4.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-11 14:03:25 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.050 |  |
| 2025-12-11 14:03:21 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:03:05 | Yaka Wewa (Ma Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:02:49 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 14:02:48 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:02:44 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:02:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:02:29 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:02:11 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.050 |  |
| 2025-12-11 14:01:56 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 14:01:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-11 14:01:23 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2025-12-11 14:01:10 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-11 14:01:08 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2025-12-11 14:01:03 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:00:27 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 13:52:32 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | -0.031 |  |
| 2025-12-11 13:52:30 | Moragaswewa (Deduru Oya) | 8.40 | 🔴 Major Flood | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 14:05:10 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-11 14:01:10 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-11 14:01:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-11 14:04:38 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-11 14:00:27 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 14:02:49 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 14:07:07 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 14:03:26 | Thanthirimale (Malwathu Oya) | 4.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-11 14:18:30 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-11 14:05:07 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 14:01:56 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 14:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:10:30 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:06:20 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:02:11 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:05:50 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:06:05 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:03:21 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:02:44 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 14:09:24 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2025-12-11 14:03:05 | Yaka Wewa (Ma Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:06:55 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:04:10 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:02:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:02:29 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:01:03 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:03:34 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:02:48 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:01:42 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-11 14:04:12 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2025-12-11 14:06:15 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-11 14:04:10 | Horowpothana (Yan Oya) | 4.53 | 🟢 Normal | -0.019 |  |
| 2025-12-11 14:05:29 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.020 |  |
| 2025-12-11 14:04:20 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.020 |  |
| 2025-12-11 14:01:23 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.021 |  |
| 2025-12-11 14:01:08 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2025-12-11 14:12:12 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | -0.031 |  |
| 2025-12-11 14:03:25 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.050 |  |
| 2025-12-11 14:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)