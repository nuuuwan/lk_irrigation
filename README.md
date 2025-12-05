# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_23:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,297 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 23:10:18 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-05 23:08:00 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-05 23:07:44 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2025-12-05 23:07:41 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:07:35 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | 0.700 | 🔺 Rising |
| 2025-12-05 23:07:25 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.127 |  |
| 2025-12-05 23:07:02 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:06:02 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-05 23:05:51 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 23:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 67.500 | 🔺 Rising |
| 2025-12-05 23:05:35 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | -0.059 |  |
| 2025-12-05 23:05:25 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.041 |  |
| 2025-12-05 23:05:20 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2025-12-05 23:05:07 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.080 |  |
| 2025-12-05 23:05:00 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 23:04:54 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:04:11 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 23:03:49 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-05 23:03:39 | Thanthirimale (Malwathu Oya) | 6.68 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2025-12-05 23:03:22 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2025-12-05 23:03:11 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 23:03:07 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-05 23:02:51 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:02:40 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 0.00 | 🟢 Normal | 67.500 | 🔺 Rising |
| 2025-12-05 23:02:06 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:01:59 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:01:35 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:00:56 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:00:44 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:00:26 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 22:24:19 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 23:03:39 | Thanthirimale (Malwathu Oya) | 6.68 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2025-12-05 23:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 67.500 | 🔺 Rising |
| 2025-12-05 23:07:35 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | 0.700 | 🔺 Rising |
| 2025-12-05 22:05:50 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 23:05:00 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 23:06:02 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 23:04:11 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 23:03:11 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 23:00:26 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 23:05:51 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 23:00:44 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:02:40 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:02:06 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:00:56 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:07:02 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:02:51 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:01:35 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:01:59 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:07:41 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:04:54 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 23:10:18 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-05 23:03:07 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-05 23:08:00 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-05 23:03:49 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:04:48 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.015 |  |
| 2025-12-05 23:05:20 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2025-12-05 23:07:44 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2025-12-05 23:03:22 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2025-12-05 23:05:25 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.041 |  |
| 2025-12-05 23:05:35 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | -0.059 |  |
| 2025-12-05 23:05:07 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.080 |  |
| 2025-12-05 23:07:25 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.127 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)