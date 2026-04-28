# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_23:15:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,707 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 23:15:31 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:14:23 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.024 |  |
| 2026-04-28 23:12:44 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.038 |  |
| 2026-04-28 23:11:20 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:10:47 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:10:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-04-28 23:09:45 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:07:57 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-04-28 23:07:56 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:07:45 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.009 |  |
| 2026-04-28 23:06:40 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:06:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-28 23:05:29 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:04:12 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:04:04 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.013 |  |
| 2026-04-28 23:03:56 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-28 23:03:09 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 23:03:00 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-04-28 23:02:47 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-04-28 23:02:46 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-04-28 23:02:41 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.010 |  |
| 2026-04-28 23:02:40 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:02:33 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 23:02:30 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.049 |  |
| 2026-04-28 23:02:25 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:02:16 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-04-28 23:01:46 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:01:42 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:01:29 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:01:26 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:00:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.013 |  |
| 2026-04-28 23:00:21 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 21:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-28 23:06:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-28 22:06:06 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-28 23:02:33 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 23:00:21 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 23:03:09 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 23:01:46 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:01:42 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:04:42 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:11:20 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:15:31 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:07:56 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:09:45 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:07:47 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:01:29 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 22:00:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:02:40 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:06:40 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:02:25 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:04:12 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:05:29 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:07:45 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.009 |  |
| 2026-04-28 23:02:41 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-28 22:02:12 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-28 23:03:56 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-28 23:00:37 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.013 |  |
| 2026-04-28 23:04:04 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.013 |  |
| 2026-04-28 23:10:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-04-28 23:02:46 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-04-28 23:02:47 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-04-28 23:03:00 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-04-28 23:14:23 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.024 |  |
| 2026-04-28 23:02:16 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-04-28 23:12:44 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.038 |  |
| 2026-04-28 23:02:30 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.049 |  |
| 2026-04-28 23:07:57 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)