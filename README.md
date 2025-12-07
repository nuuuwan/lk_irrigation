# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_20:16:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,874 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 20:16:56 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.052 |  |
| 2025-12-07 20:14:40 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-07 20:11:52 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-07 20:09:58 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2025-12-07 20:08:41 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2025-12-07 20:08:16 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:07:55 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:07:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 20:07:37 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:06:58 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-07 20:06:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2025-12-07 20:06:26 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-07 20:06:20 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:06:03 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 20:05:12 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-07 20:05:07 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-07 20:04:59 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | -0.029 |  |
| 2025-12-07 20:04:50 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-07 20:04:25 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:04:22 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-07 20:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.021 |  |
| 2025-12-07 20:03:58 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:03:40 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.022 |  |
| 2025-12-07 20:03:29 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.384 | 🔺 Rising |
| 2025-12-07 20:02:25 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 20:02:14 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:02:09 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.005 |  |
| 2025-12-07 20:01:50 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-07 20:01:25 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:01:25 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:00:58 | Thanthirimale (Malwathu Oya) | 5.39 | 🟡 Alert | -0.095 |  |
| 2025-12-07 20:00:38 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:00:27 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 20:00:58 | Thanthirimale (Malwathu Oya) | 5.39 | 🟡 Alert | -0.095 |  |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-07 20:03:29 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.384 | 🔺 Rising |
| 2025-12-07 20:04:50 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-07 20:05:07 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-07 20:11:52 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-07 20:06:26 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 20:06:03 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 20:00:27 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 20:06:58 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-07 20:14:40 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-07 20:02:25 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 20:07:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 20:04:25 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:00:38 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:02:14 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:01:25 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:08:16 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:01:25 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:01:50 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:03:58 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:07:55 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:06:20 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 20:02:09 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.005 |  |
| 2025-12-07 20:08:41 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2025-12-07 20:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-07 20:04:22 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-07 20:05:12 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-07 20:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.021 |  |
| 2025-12-07 20:03:40 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.022 |  |
| 2025-12-07 20:04:59 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | -0.029 |  |
| 2025-12-07 20:06:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2025-12-07 20:09:58 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2025-12-07 20:16:56 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.052 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)