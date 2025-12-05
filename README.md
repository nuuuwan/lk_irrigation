# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_00:16:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,333 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 00:16:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-06 00:15:50 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.077 |  |
| 2025-12-06 00:15:20 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.008 |  |
| 2025-12-06 00:12:14 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:11:12 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | 0.453 | 🔺 Rising |
| 2025-12-06 00:11:10 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:10:53 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:09:53 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:09:31 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:09:15 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.019 |  |
| 2025-12-06 00:07:21 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:07:10 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:06:46 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:06:18 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:06:05 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:05:25 | Thanthirimale (Malwathu Oya) | 6.70 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2025-12-06 00:04:28 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 00:04:23 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:04:17 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.061 |  |
| 2025-12-06 00:04:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:03:55 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:03:48 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-06 00:03:45 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:03:14 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.054 |  |
| 2025-12-06 00:03:12 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:02:45 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:02:19 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-06 00:02:18 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-06 00:02:15 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.005 |  |
| 2025-12-06 00:02:05 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:01:41 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:01:35 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:01:30 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 00:01:29 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.003 |  |
| 2025-12-05 23:27:41 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.087 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 00:11:12 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | 0.453 | 🔺 Rising |
| 2025-12-06 00:05:25 | Thanthirimale (Malwathu Oya) | 6.70 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 00:02:19 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-06 00:03:48 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 00:16:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-06 00:02:18 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-06 00:04:28 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 00:01:30 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 00:01:35 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:02:05 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:09:31 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:11:10 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:06:05 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:10:53 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:04:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:03:45 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:01:29 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:07:21 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:06:18 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:09:53 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:12:14 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.003 |  |
| 2025-12-06 00:02:15 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.005 |  |
| 2025-12-06 00:15:20 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.008 |  |
| 2025-12-05 23:10:18 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-06 00:04:23 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:03:55 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:02:45 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:06:46 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-06 00:09:15 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.019 |  |
| 2025-12-06 00:03:14 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.054 |  |
| 2025-12-06 00:04:17 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.061 |  |
| 2025-12-06 00:15:50 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.077 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)