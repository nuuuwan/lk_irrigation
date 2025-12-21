# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_03:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,433 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 03:03:06 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:58 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.061 |  |
| 2025-12-22 03:02:47 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2025-12-22 03:02:35 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:35 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:24 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:14 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 4.220 | 🔺 Rising |
| 2025-12-22 03:01:59 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2025-12-22 03:01:59 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:54 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:51 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 4.220 | 🔺 Rising |
| 2025-12-22 03:01:19 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:00:50 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:00:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.050 |  |
| 2025-12-22 02:48:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:46:18 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:40:12 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2025-12-22 02:25:10 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:17:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-22 02:10:03 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-22 02:09:47 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:08:21 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:07:38 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:07:37 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:06:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:05:52 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:05:20 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 03:02:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 4.220 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-22 02:17:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-22 00:03:54 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 03:01:19 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:00:50 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:01:43 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:03:06 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:35 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:05:20 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:24 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:06:44 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:54 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:25:10 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:51 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:05:52 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:35 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:03:06 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:48:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:01:34 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:01:59 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-22 03:02:14 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:08:21 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:07:38 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 02:40:12 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2025-12-22 02:03:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-22 02:10:03 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-22 03:02:47 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-22 02:03:05 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.035 |  |
| 2025-12-22 03:01:59 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-22 02:04:26 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2025-12-22 03:00:36 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.050 |  |
| 2025-12-22 02:03:59 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.058 |  |
| 2025-12-22 03:02:58 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.061 |  |
| 2025-12-22 02:03:02 | Horowpothana (Yan Oya) | 4.24 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)