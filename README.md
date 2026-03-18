# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_04:21:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 04:21:44 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:19:32 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-19 04:11:42 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-03-19 04:08:18 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 04:06:48 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -6.750 |  |
| 2026-03-19 04:06:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 04:06:16 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -6.750 |  |
| 2026-03-19 04:06:01 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:05:36 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:05:10 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-03-19 04:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 04:04:13 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-19 04:04:08 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-03-19 04:04:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:03:24 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:03:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:53 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 04:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-19 04:02:48 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:31 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:27 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-03-19 04:02:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 04:02:19 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:12 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 04:01:49 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:19 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:19 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:18 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:18 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-19 04:01:12 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.154 |  |
| 2026-03-19 04:01:01 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-19 04:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:39:02 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 04:19:32 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-19 04:11:42 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-03-19 04:01:01 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-19 04:02:50 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-19 04:04:13 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 23:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-19 04:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 04:01:18 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-19 04:02:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 04:08:18 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 04:02:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 04:02:53 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 04:06:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 03:05:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.005 |  |
| 2026-03-19 04:01:19 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:12 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:39:02 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:31 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:06:01 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:05:36 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:48 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:03:24 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:03:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:01:19 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:02:19 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:04:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:03:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:21:44 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 04:05:10 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-03-19 04:04:08 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-03-19 04:02:27 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-19 04:01:12 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.154 |  |
| 2026-03-19 04:06:48 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -6.750 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)