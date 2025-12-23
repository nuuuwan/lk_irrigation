# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_10:09:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,610 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 10:09:58 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:09:01 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2025-12-23 10:08:59 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:08:43 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.011 |  |
| 2025-12-23 10:08:29 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2025-12-23 10:05:48 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-23 10:05:42 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-23 10:05:35 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:05:01 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.055 |  |
| 2025-12-23 10:04:50 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-23 10:04:49 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:04:20 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:04:11 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2025-12-23 10:03:49 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.020 |  |
| 2025-12-23 10:03:42 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:03:40 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:03:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2025-12-23 10:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-23 10:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2025-12-23 10:03:18 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2025-12-23 10:03:15 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:03:14 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2025-12-23 10:02:47 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 10:02:43 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:02:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 10:02:19 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-23 10:01:49 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-23 10:01:38 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:01:36 | Manampitiya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-23 10:01:32 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:01:25 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.031 |  |
| 2025-12-23 10:01:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2025-12-23 10:01:13 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2025-12-23 10:01:10 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:00:52 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 10:01:13 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2025-12-23 10:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-23 10:05:42 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-23 10:01:36 | Manampitiya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-23 10:02:47 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 06:11:09 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-23 10:02:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 10:05:48 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-23 10:09:58 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:01:32 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:03:32 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:08:59 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:01:10 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:03:42 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:01:38 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:04:20 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:02:43 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:03:15 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 09:10:26 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:05:35 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:04:49 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:03:40 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 10:09:01 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.009 |  |
| 2025-12-23 10:02:19 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-23 10:01:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2025-12-23 10:01:49 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-23 10:08:43 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.011 |  |
| 2025-12-23 10:03:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2025-12-23 10:04:50 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-23 10:03:14 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2025-12-23 10:03:49 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.020 |  |
| 2025-12-23 10:03:18 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2025-12-23 10:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.029 |  |
| 2025-12-23 10:01:25 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.031 |  |
| 2025-12-23 10:04:11 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2025-12-23 10:08:29 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2025-12-23 09:01:48 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.053 |  |
| 2025-12-23 10:05:01 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.055 |  |
| 2025-12-23 10:00:52 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)