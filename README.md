# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_03:21:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,524 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 03:21:23 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:12:23 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.006 |  |
| 2026-01-09 03:11:47 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -2.118 |  |
| 2026-01-09 03:11:30 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -2.118 |  |
| 2026-01-09 03:11:07 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:09:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:09:29 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-09 03:08:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-09 03:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.024 |  |
| 2026-01-09 03:07:11 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-09 03:07:03 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:06:44 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:06:30 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -72.000 |  |
| 2026-01-09 03:06:29 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -72.000 |  |
| 2026-01-09 03:06:27 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -72.000 |  |
| 2026-01-09 03:06:10 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:49 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:43 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:37 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-09 03:05:08 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-01-09 03:04:58 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:04:55 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.056 |  |
| 2026-01-09 03:04:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-01-09 03:04:16 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.023 |  |
| 2026-01-09 03:03:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:03:44 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:02:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:49 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:25 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:16 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:09 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:02:02 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:52 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:50 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-01-09 03:01:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:01:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:21 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-01-09 03:01:18 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.195 |  |
| 2026-01-09 03:01:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:00:19 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:59:51 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 02:59:41 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 03:08:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-09 03:07:11 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-09 03:09:29 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 03:09:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:11:07 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:49 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:00:19 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:03:50 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:49 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:05:43 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:02 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:02:25 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:04:58 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:52 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:06:44 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:21:23 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:07:03 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:01:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 03:12:23 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.006 |  |
| 2026-01-09 03:05:37 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:03:44 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:02:09 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:01:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-09 03:01:21 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-01-09 03:05:08 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-01-09 03:04:25 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-01-09 03:04:16 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.023 |  |
| 2026-01-09 03:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.024 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-09 03:01:50 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-01-09 03:04:55 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.056 |  |
| 2026-01-09 03:01:18 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.195 |  |
| 2026-01-09 03:11:47 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -2.118 |  |
| 2026-01-09 03:06:30 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)