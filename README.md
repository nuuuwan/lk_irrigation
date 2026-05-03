# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_11:12:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,710 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 11:12:20 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.056 |  |
| 2026-05-03 11:12:16 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-05-03 11:11:46 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-05-03 11:11:20 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-05-03 11:11:05 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:10:53 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-03 11:10:39 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.030 |  |
| 2026-05-03 11:06:47 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.019 |  |
| 2026-05-03 11:06:13 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-03 11:04:40 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:04:23 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:04:02 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 11:03:47 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-05-03 11:03:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:03:21 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-03 11:03:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 11:03:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-05-03 11:03:00 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:59 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:57 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 12.600 | 🔺 Rising |
| 2026-05-03 11:01:47 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.052 |  |
| 2026-05-03 11:01:46 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.109 |  |
| 2026-05-03 11:01:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:44 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:41 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-05-03 11:01:37 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 12.600 | 🔺 Rising |
| 2026-05-03 11:01:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:25 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-03 11:01:09 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-05-03 11:01:09 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:08 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:00:47 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:00:42 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 11:00:13 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-05-03 10:59:50 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 10:41:27 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 11:01:57 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 12.600 | 🔺 Rising |
| 2026-05-03 11:03:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-05-03 11:06:13 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-03 11:10:53 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-03 11:03:21 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-03 11:01:25 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-03 10:01:46 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-03 11:03:21 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 11:00:42 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 11:04:02 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 11:04:40 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:33 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:03:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:09 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:08 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:00:47 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:45 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:59 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:03:00 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:10:39 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:11:05 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:04:23 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:01:44 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 11:11:46 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-05-03 11:11:20 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-05-03 11:12:16 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-05-03 11:01:09 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-05-03 11:01:41 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-05-03 10:41:27 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.012 |  |
| 2026-05-03 11:06:47 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.019 |  |
| 2026-05-03 11:03:47 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-05-03 11:06:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.030 |  |
| 2026-05-03 10:18:30 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-05-03 11:00:13 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-05-03 11:01:47 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.052 |  |
| 2026-05-03 11:12:20 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.056 |  |
| 2026-05-03 11:01:46 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.109 |  |
| 2026-05-03 10:02:18 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)