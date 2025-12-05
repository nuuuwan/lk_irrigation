# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_19:09:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,168 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 19:09:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 19:08:48 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 19:08:14 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.028 |  |
| 2025-12-05 19:08:08 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-05 19:07:59 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:07:41 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.010 |  |
| 2025-12-05 19:06:51 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 19:06:21 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:06:14 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-05 19:06:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:06:05 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:05:59 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 19:05:23 | Thanthirimale (Malwathu Oya) | 6.59 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2025-12-05 19:04:38 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:03:47 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:03:35 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:03:22 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 19:03:20 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:03:10 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.039 |  |
| 2025-12-05 19:02:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2025-12-05 19:02:42 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 19:02:32 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | -0.012 |  |
| 2025-12-05 19:02:22 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.013 |  |
| 2025-12-05 19:02:14 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:02:01 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-05 19:01:54 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:01:42 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:01:15 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-05 19:00:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 19:00:13 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-05 18:24:42 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:14:27 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.013 |  |
| 2025-12-05 18:13:33 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 19:05:23 | Thanthirimale (Malwathu Oya) | 6.59 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2025-12-05 19:00:13 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-05 19:06:14 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 19:08:08 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 19:02:42 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 19:02:01 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-05 19:00:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-05 18:02:10 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 19:03:22 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 19:05:59 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 19:06:51 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 19:08:48 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 19:09:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 19:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:02:14 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:06:05 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:01:42 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:06:21 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:03:35 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:06:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:04:38 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:03:47 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:01:54 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:03:20 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 19:07:59 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:07:12 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2025-12-05 19:01:15 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-05 19:07:41 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.010 |  |
| 2025-12-05 19:02:32 | Panadugama (Nilwala Ganga) | 4.35 | 🟢 Normal | -0.012 |  |
| 2025-12-05 19:02:22 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.013 |  |
| 2025-12-05 19:02:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2025-12-05 19:08:14 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.028 |  |
| 2025-12-05 19:03:10 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.039 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)