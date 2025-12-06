# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_20:03:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,021 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 20:03:41 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.011 |  |
| 2025-12-06 20:03:20 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:03:06 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.062 |  |
| 2025-12-06 20:02:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:50 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-06 20:02:39 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2025-12-06 20:02:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.134 |  |
| 2025-12-06 20:02:28 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:05 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:02:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:19 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:10 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:00:20 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-06 19:35:03 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:34:03 | Thanthirimale (Malwathu Oya) | 6.65 | 🟡 Alert | -0.027 |  |
| 2025-12-06 19:20:16 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:14:38 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:12:55 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-06 19:12:33 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:11:47 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.051 |  |
| 2025-12-06 19:10:14 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:09:42 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:09:41 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.089 |  |
| 2025-12-06 19:07:08 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:06:56 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | -0.011 |  |
| 2025-12-06 19:06:47 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.012 |  |
| 2025-12-06 19:06:13 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:06:09 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.040 |  |
| 2025-12-06 19:05:49 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:05:12 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.062 |  |
| 2025-12-06 19:05:09 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 19:34:03 | Thanthirimale (Malwathu Oya) | 6.65 | 🟡 Alert | -0.027 |  |
| 2025-12-06 19:01:36 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 20:02:50 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-06 19:04:41 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-06 19:05:00 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 20:01:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:03 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:10 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:09:42 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:12:33 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:35:03 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:02:28 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:02:24 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:01:19 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:05:49 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:20:16 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:03:20 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-06 19:05:09 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:00:20 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:02:05 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-06 20:03:41 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-06 19:06:47 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.012 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-06 20:02:39 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2025-12-06 19:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.020 |  |
| 2025-12-06 19:00:50 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.034 |  |
| 2025-12-06 19:06:09 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.040 |  |
| 2025-12-06 19:11:47 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.051 |  |
| 2025-12-06 19:04:50 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | -0.057 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-06 20:03:06 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.062 |  |
| 2025-12-06 19:09:41 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.089 |  |
| 2025-12-06 20:02:29 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)