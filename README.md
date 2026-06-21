# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_02:13:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,882 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 02:13:40 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:13:38 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:11:44 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:07:50 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-22 02:07:36 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-06-22 02:05:28 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:05:08 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -1.385 |  |
| 2026-06-22 02:04:42 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -1.385 |  |
| 2026-06-22 02:04:34 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.338 |  |
| 2026-06-22 02:04:31 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:04:16 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:04:14 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:03:41 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:03:27 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.025 |  |
| 2026-06-22 02:03:17 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-22 02:03:02 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-22 02:02:45 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-06-22 02:02:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-06-22 02:02:24 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:02:22 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:02:14 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:02:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:01:56 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-22 02:01:48 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-22 02:01:36 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.122 |  |
| 2026-06-22 02:01:26 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 02:01:16 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2026-06-22 02:01:14 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:00:57 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-06-22 02:00:56 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:00:27 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-22 01:39:04 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.025 |  |
| 2026-06-22 01:31:20 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 01:06:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 01:06:10 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 02:07:50 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-22 02:03:02 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-22 02:01:26 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-22 01:08:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 02:00:56 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:02:24 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 23:02:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:11:44 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:05:28 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:04:31 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:04:16 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 01:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:00:27 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:02:22 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:02:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:02:14 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:01:14 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:13:40 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-22 02:03:17 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-22 02:01:48 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-06-22 02:00:57 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.011 |  |
| 2026-06-22 01:02:39 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-06-22 02:01:56 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-22 02:02:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-22 02:07:36 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.021 |  |
| 2026-06-22 02:03:27 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.025 |  |
| 2026-06-22 00:32:10 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-06-22 02:02:45 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-06-22 02:01:16 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2026-06-22 02:01:36 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.122 |  |
| 2026-06-22 02:04:34 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.338 |  |
| 2026-06-22 02:05:08 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -1.385 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)