# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_21:06:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,217 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 21:06:38 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-05-11 21:06:23 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:05:40 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | 0.591 | 🔺 Rising |
| 2026-05-11 21:05:29 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:05:29 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:05:01 | Siyambalanduwa (Heda Oya) | 2.75 | 🟢 Normal | 0.615 | 🔺 Rising |
| 2026-05-11 21:04:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 21:04:44 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-05-11 21:04:44 | Katharagama (Menik Ganga) | 2.39 | 🟢 Normal | -0.041 |  |
| 2026-05-11 21:04:43 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-11 21:04:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 21:04:29 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 21:04:20 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 21:03:43 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.054 |  |
| 2026-05-11 21:03:41 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.206 |  |
| 2026-05-11 21:03:27 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 21:03:07 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.049 |  |
| 2026-05-11 21:02:30 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:25 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:23 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:16 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 21:02:15 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:08 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:05 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:01:26 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 21:01:21 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.072 |  |
| 2026-05-11 21:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 21:00:18 | Nakkala (Kumbukkan Oya) | 2.15 | 🟢 Normal | -0.256 |  |
| 2026-05-11 21:00:17 | Wellawaya (Kirindi Oya) | 1.99 | 🟢 Normal | -0.080 |  |
| 2026-05-11 21:00:14 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 21:05:01 | Siyambalanduwa (Heda Oya) | 2.75 | 🟢 Normal | 0.615 | 🔺 Rising |
| 2026-05-11 21:05:40 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | 0.591 | 🔺 Rising |
| 2026-05-11 21:01:26 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-11 21:02:16 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 21:04:20 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 21:04:43 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-11 20:04:22 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-11 21:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-11 20:05:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 21:04:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 21:03:27 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 21:04:29 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 21:04:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 20:10:55 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 21:05:29 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-11 20:07:25 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:05 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:15 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:05:29 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:06:23 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:25 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:08 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:30 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:02:23 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-11 21:04:44 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-05-11 20:11:30 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-05-11 21:00:14 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-05-11 21:04:44 | Katharagama (Menik Ganga) | 2.39 | 🟢 Normal | -0.041 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-11 21:03:07 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.049 |  |
| 2026-05-11 21:06:38 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-05-11 21:03:43 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.054 |  |
| 2026-05-11 21:01:21 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.072 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-11 21:00:17 | Wellawaya (Kirindi Oya) | 1.99 | 🟢 Normal | -0.080 |  |
| 2026-05-11 20:08:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.135 |  |
| 2026-05-11 21:03:41 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.206 |  |
| 2026-05-11 21:00:18 | Nakkala (Kumbukkan Oya) | 2.15 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)