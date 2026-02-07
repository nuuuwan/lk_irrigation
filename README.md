# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_00:08:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,011 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 00:08:54 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:08:52 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.029 |  |
| 2026-02-08 00:07:59 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-08 00:07:24 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-02-08 00:07:15 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:06:59 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 00:06:53 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-02-08 00:06:47 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-02-08 00:05:58 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:05:38 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-02-08 00:05:11 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.090 |  |
| 2026-02-08 00:04:57 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-02-08 00:04:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-08 00:04:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:03:30 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:02:39 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:50 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:48 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 00:01:38 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:36 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -180.000 |  |
| 2026-02-08 00:01:36 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-02-08 00:01:35 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -180.000 |  |
| 2026-02-08 00:01:34 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:30 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:04 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-08 00:01:03 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -180.000 |  |
| 2026-02-08 00:00:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:00:35 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.042 |  |
| 2026-02-08 00:00:32 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-08 00:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:00:11 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 00:06:53 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-02-08 00:04:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-07 23:43:55 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-08 00:01:04 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-08 00:01:48 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 00:06:59 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 23:08:34 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-08 00:00:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:00:11 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:38 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:30 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:50 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:34 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:05:58 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:02:39 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:04:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:08:54 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:03:30 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:51:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:07:15 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 23:09:44 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-02-08 00:07:24 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-02-08 00:00:32 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-08 00:07:59 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-07 21:10:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-02-08 00:05:38 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-02-08 00:01:36 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-08 00:08:52 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.029 |  |
| 2026-02-08 00:04:57 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-02-08 00:06:47 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-02-07 22:01:33 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.030 |  |
| 2026-02-08 00:00:35 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.042 |  |
| 2026-02-07 23:00:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.073 |  |
| 2026-02-08 00:05:11 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | -0.090 |  |
| 2026-02-08 00:01:36 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)