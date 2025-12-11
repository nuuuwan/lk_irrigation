# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_07:20:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,777 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 07:20:20 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:08:31 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.018 |  |
| 2025-12-11 07:07:20 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.041 |  |
| 2025-12-11 07:07:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:06:53 | Horowpothana (Yan Oya) | 4.67 | 🟢 Normal | -0.014 |  |
| 2025-12-11 07:06:41 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2025-12-11 07:06:20 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-11 07:05:14 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 07:04:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:04:47 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:04:46 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:04:37 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.048 |  |
| 2025-12-11 07:04:29 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 07:04:01 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.039 |  |
| 2025-12-11 07:04:00 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2025-12-11 07:03:39 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:03:37 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 07:03:26 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2025-12-11 07:03:24 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:03:17 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:03:13 | Yaka Wewa (Ma Oya) | 1.44 | 🟢 Normal | -0.019 |  |
| 2025-12-11 07:03:12 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.021 |  |
| 2025-12-11 07:03:02 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | -1.627 |  |
| 2025-12-11 07:02:56 | Thanthirimale (Malwathu Oya) | 4.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 07:02:43 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:02:11 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:02:08 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-11 07:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.083 |  |
| 2025-12-11 07:02:07 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 07:02:04 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-11 07:01:41 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.025 |  |
| 2025-12-11 07:01:41 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:01:09 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:01:07 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2025-12-11 07:00:13 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:57:08 | Weraganthota (Mahaweli Ganga) | -0.96 | 🟢 Normal | -1.627 |  |
| 2025-12-11 06:35:05 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | -0.018 |  |
| 2025-12-11 06:23:11 | Horowpothana (Yan Oya) | 4.68 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 07:02:08 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2025-12-11 07:02:04 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-11 07:03:37 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 07:05:14 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 07:04:29 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 07:02:56 | Thanthirimale (Malwathu Oya) | 4.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 07:06:20 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-11 07:03:17 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:00:13 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 05:00:48 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:02:43 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 06:01:23 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:01:09 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:01:41 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:02:11 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:04:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:03:39 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:04:47 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:03:24 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:07:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:20:20 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:04:46 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 07:06:41 | Rathnapura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2025-12-11 07:03:26 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.010 |  |
| 2025-12-11 07:02:07 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-11 07:01:07 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2025-12-11 07:06:53 | Horowpothana (Yan Oya) | 4.67 | 🟢 Normal | -0.014 |  |
| 2025-12-11 07:08:31 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.018 |  |
| 2025-12-11 07:04:00 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2025-12-11 07:03:13 | Yaka Wewa (Ma Oya) | 1.44 | 🟢 Normal | -0.019 |  |
| 2025-12-11 07:03:12 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.021 |  |
| 2025-12-11 07:01:41 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.025 |  |
| 2025-12-11 07:04:01 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.039 |  |
| 2025-12-11 07:07:20 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.041 |  |
| 2025-12-11 07:04:37 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.048 |  |
| 2025-12-11 07:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.083 |  |
| 2025-12-11 07:03:02 | Weraganthota (Mahaweli Ganga) | -1.12 | 🟢 Normal | -1.627 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)