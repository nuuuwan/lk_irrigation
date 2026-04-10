# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_13:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 13:17:39 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:17:15 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:16:44 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:12:36 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:10:47 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.027 |  |
| 2026-04-10 13:08:10 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:07:50 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:07:43 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:07:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:06:23 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.012 |  |
| 2026-04-10 13:06:03 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:06:03 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.051 |  |
| 2026-04-10 13:05:45 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:04:33 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 13:04:12 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:03:55 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-10 13:03:39 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:03:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:02:52 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-04-10 13:02:52 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-04-10 13:02:36 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:02:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 13:02:25 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 13:02:22 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:02:12 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:01:49 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-10 13:01:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:01:15 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:01:13 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 13:01:09 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 13:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 13:01:01 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:00:48 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:00:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:00:14 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 12:59:46 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.123 |  |
| 2026-04-10 12:56:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:40:04 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 13:02:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-10 13:02:25 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 13:01:09 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-10 13:01:13 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 13:00:14 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 13:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 13:04:33 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-10 13:01:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:03:39 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:03:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:02:22 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:02:12 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:40:04 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:17:39 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:16:44 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:08:10 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:04:12 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:12:36 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:00:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:07:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:17:15 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:00:48 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:02:36 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:07:43 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:05:45 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:01:15 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 13:07:50 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:06:03 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:02:52 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:01:01 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-10 13:06:23 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.012 |  |
| 2026-04-10 13:03:55 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-10 13:01:49 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-04-10 13:10:47 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.027 |  |
| 2026-04-10 13:02:52 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-04-10 13:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-04-10 12:04:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-10 13:06:03 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.051 |  |
| 2026-04-10 12:59:46 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)