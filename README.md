# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_13:14:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,009 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 13:14:08 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2025-12-11 13:12:41 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.036 |  |
| 2025-12-11 13:11:57 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:11:03 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 13:10:36 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:10:28 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:07:30 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.043 |  |
| 2025-12-11 13:05:56 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 13:05:47 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2025-12-11 13:04:13 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:04:07 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.030 |  |
| 2025-12-11 13:03:52 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:03:41 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:03:35 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:03:34 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:03:24 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:03:17 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:03:13 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.021 |  |
| 2025-12-11 13:03:12 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-11 13:03:11 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2025-12-11 13:03:08 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:03:07 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 13:02:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:24 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.041 |  |
| 2025-12-11 13:02:11 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:11 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:01:46 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.031 |  |
| 2025-12-11 13:01:42 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:01:39 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-11 13:01:12 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-11 13:01:11 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2025-12-11 13:01:06 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:01:05 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:00:45 | Horowpothana (Yan Oya) | 4.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:00:23 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 13:01:12 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-11 13:03:12 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-11 13:01:39 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-11 13:11:03 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 13:03:07 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 13:05:56 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 13:02:11 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:00:23 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:01:05 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:03:52 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:00:45 | Horowpothana (Yan Oya) | 4.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:03:34 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:03 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:03:17 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:04:13 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:10:28 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:24 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:10:36 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:11:57 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:02:11 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:01:06 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 13:14:08 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2025-12-11 13:03:41 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:03:35 | Galgamuwa (Mee Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:03:24 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:03:08 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:01:42 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-11 13:05:47 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2025-12-11 13:03:13 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.021 |  |
| 2025-12-11 13:04:07 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.030 |  |
| 2025-12-11 13:03:11 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2025-12-11 13:01:46 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.031 |  |
| 2025-12-11 13:12:41 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.036 |  |
| 2025-12-11 13:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.041 |  |
| 2025-12-11 13:07:30 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.043 |  |
| 2025-12-11 13:01:11 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)