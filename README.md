# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_22:06:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 22:06:50 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-06 22:06:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | -0.014 |  |
| 2025-12-06 22:05:05 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.050 |  |
| 2025-12-06 22:04:59 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:04:41 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:04:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-06 22:04:37 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.019 |  |
| 2025-12-06 22:03:57 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-06 22:03:19 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2025-12-06 22:03:09 | Hanwella (Kelani Ganga) | 2.65 | 🟢 Normal | -0.022 |  |
| 2025-12-06 22:03:05 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:03:00 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 22:02:42 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:38 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:31 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:14 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:08 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2025-12-06 22:01:52 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-06 22:01:50 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:01:31 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-06 22:01:24 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:01:19 | Thanthirimale (Malwathu Oya) | 6.53 | 🟡 Alert | -0.039 |  |
| 2025-12-06 22:01:13 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-06 22:00:47 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:00:33 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 21:26:00 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-06 21:22:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.014 |  |
| 2025-12-06 21:22:30 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-06 21:20:32 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 21:09:17 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 21:09:14 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 22:01:19 | Thanthirimale (Malwathu Oya) | 6.53 | 🟡 Alert | -0.039 |  |
| 2025-12-06 22:01:13 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-06 22:03:57 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-06 22:06:50 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-06 22:03:00 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-06 22:04:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-06 21:09:14 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-06 22:00:47 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:01:50 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:00:33 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 21:20:32 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:14 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 20:05:21 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:03:05 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:38 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:31 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:42 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:01:24 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:04:41 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:04:59 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:03:19 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-06 22:01:52 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-06 22:01:31 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-06 21:04:55 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-06 22:06:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | -0.014 |  |
| 2025-12-06 22:04:37 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.019 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-06 22:02:08 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2025-12-06 22:03:09 | Hanwella (Kelani Ganga) | 2.65 | 🟢 Normal | -0.022 |  |
| 2025-12-06 21:05:14 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.041 |  |
| 2025-12-06 22:05:05 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.050 |  |
| 2025-12-06 21:06:49 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.059 |  |
| 2025-12-06 21:05:28 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.060 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)