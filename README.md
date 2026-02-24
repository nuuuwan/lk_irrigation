# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_14:14:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,844 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 14:14:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:13:52 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-02-24 14:08:05 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.041 |  |
| 2026-02-24 14:07:32 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:07:18 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:06:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:05:46 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-02-24 14:05:42 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-24 14:04:55 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 14:04:38 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-02-24 14:04:30 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:04:20 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:04:01 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:03:56 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-24 14:03:34 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 14:03:25 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:03:18 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-24 14:03:06 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.031 |  |
| 2026-02-24 14:03:00 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:53 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:02:52 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:42 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-24 14:02:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:02:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 14:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:02:03 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-24 14:01:57 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:55 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:44 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-02-24 14:01:33 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:01:29 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:01:24 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:11 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:00:55 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-24 14:00:17 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:00:17 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.247 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 14:01:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-02-24 14:03:56 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-24 14:02:03 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-24 14:03:34 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 14:03:18 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-24 14:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-24 14:00:55 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-24 14:04:55 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 14:02:25 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 14:03:25 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:02:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:04:20 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:55 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:00:17 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:02:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:24 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:44 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:57 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:02:53 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:06:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:07:18 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:07:32 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:11 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:14:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:05:42 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:04:30 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:01:29 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:03:00 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:04:01 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:01:33 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:52 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:42 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-24 14:05:46 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-02-24 14:04:38 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-02-24 14:03:06 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.031 |  |
| 2026-02-24 14:13:52 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-02-24 14:08:05 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.041 |  |
| 2026-02-24 14:00:17 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)