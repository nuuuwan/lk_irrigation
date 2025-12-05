# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_22:24:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,266 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 22:24:19 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-05 22:11:12 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:07:15 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:07:00 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:06:43 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.553 | 🔺 Rising |
| 2025-12-05 22:06:41 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2025-12-05 22:06:21 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-05 22:06:16 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:06:02 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.111 |  |
| 2025-12-05 22:05:50 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-05 22:05:19 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.016 |  |
| 2025-12-05 22:04:55 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.039 |  |
| 2025-12-05 22:04:55 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-05 22:04:50 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-05 22:04:48 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.015 |  |
| 2025-12-05 22:04:16 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:04:08 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2025-12-05 22:03:50 | Thanthirimale (Malwathu Oya) | 6.65 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2025-12-05 22:03:46 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.005 |  |
| 2025-12-05 22:03:25 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:03:24 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 22:02:46 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:02:27 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:02:26 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:02:15 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:02:14 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2025-12-05 22:01:22 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-05 22:01:14 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:00:58 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:00:27 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:00:21 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 22:03:50 | Thanthirimale (Malwathu Oya) | 6.65 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2025-12-05 22:06:43 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.553 | 🔺 Rising |
| 2025-12-05 22:04:50 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2025-12-05 22:04:08 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2025-12-05 22:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-05 22:05:50 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 22:06:21 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-05 22:04:55 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 22:03:24 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 22:24:19 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-05 22:00:21 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:00:58 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:02:26 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:02:46 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:11:12 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:06:16 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:02:15 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:00:27 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:07:15 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:01:14 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:04:16 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 22:03:46 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.005 |  |
| 2025-12-05 22:07:00 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:03:25 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:02:27 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:01:22 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-05 22:04:48 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.015 |  |
| 2025-12-05 22:05:19 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.016 |  |
| 2025-12-05 22:06:41 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2025-12-05 22:02:14 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2025-12-05 22:04:55 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.039 |  |
| 2025-12-05 22:06:02 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.111 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)