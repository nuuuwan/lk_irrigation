# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_03:22:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 03:22:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-08 03:21:30 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:16:05 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:09:53 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-08 03:07:39 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-04-08 03:07:04 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-08 03:06:05 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-04-08 03:05:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:05:07 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:04:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-08 03:04:02 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-08 03:03:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.030 |  |
| 2026-04-08 03:03:31 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:03:30 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:03:30 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.099 |  |
| 2026-04-08 03:03:20 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:03:10 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:03:09 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 03:02:48 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:02:43 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.031 |  |
| 2026-04-08 03:02:36 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:02:13 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:02:09 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.254 |  |
| 2026-04-08 03:02:08 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 03:01:34 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:01:08 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:01:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:00:35 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:00:21 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 02:56:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-08 02:56:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 03:22:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-08 03:04:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-08 03:02:08 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-08 00:07:04 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 03:03:09 | Thawalama (Gin Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 03:07:04 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-08 03:09:53 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-08 03:00:21 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:03:30 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:01:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 01:27:21 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:02:48 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 00:37:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 01:07:12 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:16:05 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:03:20 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:03:31 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:01:08 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:00:35 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:04:02 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:21:30 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:02:13 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-08 02:03:55 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:07:39 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-04-08 02:07:29 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-08 02:02:07 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:02:36 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:05:27 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:03:10 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-04-08 03:05:07 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-04-07 18:00:44 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-04-08 03:03:39 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-08 03:06:05 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-04-08 03:03:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.030 |  |
| 2026-04-08 03:02:43 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.031 |  |
| 2026-04-07 18:02:51 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.032 |  |
| 2026-04-07 18:01:46 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.060 |  |
| 2026-04-08 03:03:30 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.099 |  |
| 2026-04-08 03:02:09 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.254 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)