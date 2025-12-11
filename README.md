# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_01:08:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 01:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 01:08:15 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2025-12-12 01:06:42 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2025-12-12 01:06:38 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-12 01:06:14 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.047 |  |
| 2025-12-12 01:06:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-12 01:05:55 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-12 01:05:15 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.302 |  |
| 2025-12-12 01:04:59 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2025-12-12 01:04:55 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 01:04:50 | Nakkala (Kumbukkan Oya) | 1.89 | 🟢 Normal | -0.125 |  |
| 2025-12-12 01:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-12 01:03:00 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 01:02:47 | Horowpothana (Yan Oya) | 4.27 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-12 01:02:26 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2025-12-12 01:02:11 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.020 |  |
| 2025-12-12 01:02:00 | Yaka Wewa (Ma Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 01:01:51 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 01:01:50 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-12 01:01:31 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 01:01:12 | Siyambalanduwa (Heda Oya) | 1.52 | 🟢 Normal | -0.041 |  |
| 2025-12-12 01:01:10 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 01:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 01:01:05 | Moragaswewa (Deduru Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 01:00:15 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 00:04:41 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2025-12-12 01:06:42 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 01:08:15 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2025-12-11 23:26:55 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2025-12-12 01:06:38 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-12 00:08:37 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-12 01:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-12 01:06:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-12 01:02:47 | Horowpothana (Yan Oya) | 4.27 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-12 01:01:31 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 01:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 01:01:10 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 01:01:51 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-12 00:11:00 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-12 01:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 01:03:00 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 00:00:20 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 01:01:05 | Moragaswewa (Deduru Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 01:02:00 | Yaka Wewa (Ma Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 00:06:56 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:48 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 01:04:55 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:06:14 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-12 01:05:55 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-12 01:01:50 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-12 01:02:11 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.020 |  |
| 2025-12-12 01:04:59 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2025-12-12 01:02:26 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-12 01:01:12 | Siyambalanduwa (Heda Oya) | 1.52 | 🟢 Normal | -0.041 |  |
| 2025-12-12 01:06:14 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.047 |  |
| 2025-12-12 01:00:15 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.091 |  |
| 2025-12-12 01:04:50 | Nakkala (Kumbukkan Oya) | 1.89 | 🟢 Normal | -0.125 |  |
| 2025-12-12 00:01:45 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -0.205 |  |
| 2025-12-12 01:05:15 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.302 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)