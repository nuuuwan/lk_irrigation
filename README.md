# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_07:25:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,438 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 07:25:58 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.007 |  |
| 2026-05-04 07:24:06 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.007 |  |
| 2026-05-04 07:13:22 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.008 |  |
| 2026-05-04 07:11:43 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:10:56 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:08:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.053 |  |
| 2026-05-04 07:05:08 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.047 |  |
| 2026-05-04 07:05:05 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-05-04 07:04:56 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:04:54 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-05-04 07:04:31 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:04:29 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.116 |  |
| 2026-05-04 07:04:27 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-04 07:04:21 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.029 |  |
| 2026-05-04 07:04:17 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:04:01 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:03:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:03:28 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-04 07:03:27 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:03:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:03:08 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-05-04 07:02:56 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-04 07:02:53 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:21 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:21 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-04 07:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.051 |  |
| 2026-05-04 07:02:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:09 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 07:02:09 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:01:49 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.167 |  |
| 2026-05-04 07:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-04 07:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:01:25 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.054 |  |
| 2026-05-04 07:01:09 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-05-04 07:00:28 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.122 |  |
| 2026-05-04 07:00:12 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 07:02:21 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-04 07:02:56 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-04 07:03:28 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-04 07:04:27 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-04 06:10:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 07:02:09 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 07:00:12 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:09 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:04:56 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:04:17 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:10:56 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:53 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:03:27 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:04:01 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:03:22 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:04:31 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:11:43 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:03:51 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:02:21 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-04 07:25:58 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.007 |  |
| 2026-05-04 07:24:06 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.007 |  |
| 2026-05-04 07:13:22 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.008 |  |
| 2026-05-04 07:01:36 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-04 07:01:09 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-05-04 07:05:05 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-05-04 07:04:21 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.029 |  |
| 2026-05-04 07:04:54 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-05-04 07:05:08 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.047 |  |
| 2026-05-04 07:03:08 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-05-04 07:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.051 |  |
| 2026-05-04 07:08:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.053 |  |
| 2026-05-04 07:01:25 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.054 |  |
| 2026-05-04 06:02:45 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.107 |  |
| 2026-05-04 07:04:29 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.116 |  |
| 2026-05-04 07:00:28 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.122 |  |
| 2026-05-04 07:01:49 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)