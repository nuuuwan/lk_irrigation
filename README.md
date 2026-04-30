# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_12:05:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 12:05:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:04:56 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.020 |  |
| 2026-04-30 12:04:40 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.048 |  |
| 2026-04-30 12:04:39 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-04-30 12:04:31 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:04:29 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-04-30 12:03:40 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:35 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-04-30 12:03:35 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 12:03:29 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 12:03:28 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-04-30 12:03:21 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-30 12:03:17 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2026-04-30 12:03:10 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:09 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:00 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 12:02:47 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-30 12:02:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:02:41 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 12:02:28 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-04-30 12:02:19 | Thanthirimale (Malwathu Oya) | 2.85 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 12:02:02 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.011 |  |
| 2026-04-30 12:01:43 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-30 12:01:30 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:28 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:10 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:00:59 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:00:53 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:00:27 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-04-30 11:30:02 | Thanthirimale (Malwathu Oya) | 2.77 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 11:23:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:21:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:16:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 12:03:35 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 12:02:19 | Thanthirimale (Malwathu Oya) | 2.85 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-04-30 12:02:47 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-30 12:04:29 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-04-30 12:03:29 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-30 11:03:34 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-30 12:03:00 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 10:00:27 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 12:02:41 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 12:01:43 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:28 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:04:31 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:40 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:10 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:28 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:10 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:23:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:02:46 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:03:01 | Dunamale (Aththanagalu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:09 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:05:04 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:06:16 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:00:53 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:30 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-30 11:21:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:00:59 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-04-30 12:03:35 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-04-30 12:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-30 12:03:21 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-30 12:02:02 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.011 |  |
| 2026-04-30 12:03:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-04-30 12:00:27 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-04-30 10:08:22 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-30 12:02:28 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-04-30 12:04:56 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.020 |  |
| 2026-04-30 12:04:39 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-04-30 12:03:17 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.021 |  |
| 2026-04-30 12:04:40 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)