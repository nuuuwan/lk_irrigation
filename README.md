# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_23:12:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,424 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 23:12:13 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2026-04-03 23:09:27 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:08:40 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:08:03 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:06:53 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:06:21 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:06:12 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-04-03 23:05:47 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-04-03 23:05:21 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-03 23:05:16 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-03 23:04:23 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-04-03 23:04:21 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:04:05 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:04:04 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-03 23:03:51 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 23:03:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:03:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-04-03 23:02:59 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.020 |  |
| 2026-04-03 23:02:43 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:02:25 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.170 |  |
| 2026-04-03 23:02:22 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:02:10 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-04-03 23:02:07 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:01:55 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-03 23:01:52 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-03 23:01:43 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:01:30 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 23:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-03 23:01:05 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.040 |  |
| 2026-04-03 23:00:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:00:55 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-03 23:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:00:34 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 22:18:59 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 23:12:13 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2026-04-03 23:00:55 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-03 23:01:55 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-03 23:04:04 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-03 23:03:51 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 23:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-03 23:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 23:09:27 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:00:34 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:00:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:02:07 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:01:30 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:04:05 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:08:40 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:06:53 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:06:21 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:02:43 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:03:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:02:22 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:04:21 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:08:03 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 23:05:16 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-03 23:01:52 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-03 23:02:10 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-04-03 23:04:23 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-04-03 23:02:59 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.020 |  |
| 2026-04-03 23:05:21 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-03 23:05:47 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-04-03 23:06:12 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-04-03 23:03:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-04-03 22:02:53 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-04-03 23:01:05 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.040 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-03 21:48:14 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-04-03 21:11:08 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.076 |  |
| 2026-04-03 23:02:25 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)