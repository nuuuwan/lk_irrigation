# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_04:19:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,560 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 04:19:26 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-11 04:17:33 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-11 04:15:51 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.017 |  |
| 2026-05-11 04:07:45 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:07:28 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-11 04:06:43 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 04:06:08 | Katharagama (Menik Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 04:05:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-11 04:05:27 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:04:58 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-11 04:04:37 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-05-11 04:04:14 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-05-11 04:03:59 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-11 04:03:32 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 04:03:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:03:24 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:03:07 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-11 04:03:06 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:02:45 | Thanamalwila (Kirindi Oya) | 5.68 | 🔴 Major Flood | -0.136 |  |
| 2026-05-11 04:02:39 | Kuda Oya (Kirindi Oya) | 5.34 | 🟢 Normal | -0.632 |  |
| 2026-05-11 04:02:39 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-11 04:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.123 |  |
| 2026-05-11 04:01:52 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.030 |  |
| 2026-05-11 04:01:48 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-05-11 04:01:46 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 04:01:15 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -1.168 |  |
| 2026-05-11 04:01:03 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.021 |  |
| 2026-05-11 04:00:39 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-11 04:00:17 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.098 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 04:02:45 | Thanamalwila (Kirindi Oya) | 5.68 | 🔴 Major Flood | -0.136 |  |
| 2026-05-11 04:04:58 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-11 04:00:39 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-11 04:01:46 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-11 03:02:45 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 04:05:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-11 04:19:26 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-11 04:06:08 | Katharagama (Menik Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-11 03:04:43 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-11 04:03:07 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-11 04:06:43 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 04:03:32 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 04:07:28 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-11 04:17:33 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-11 04:03:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:03:24 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:02:29 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:05:27 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:07:45 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-11 03:14:53 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:03:06 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-11 04:03:59 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-11 04:04:37 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-05-11 04:15:51 | Wellawaya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.017 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-11 03:09:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-05-11 04:01:48 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-05-11 04:01:03 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.021 |  |
| 2026-05-11 04:02:39 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-11 04:01:52 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.030 |  |
| 2026-05-11 04:04:14 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-05-11 03:10:23 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.040 |  |
| 2026-05-11 03:15:43 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-05-11 04:00:17 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.098 |  |
| 2026-05-11 04:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.123 |  |
| 2026-05-11 04:02:39 | Kuda Oya (Kirindi Oya) | 5.34 | 🟢 Normal | -0.632 |  |
| 2026-05-11 04:01:15 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -1.168 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)