# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_00:26:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,721 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 00:26:23 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.034 |  |
| 2026-05-08 00:22:02 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -0.232 |  |
| 2026-05-08 00:17:26 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-05-08 00:17:05 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -72.000 |  |
| 2026-05-08 00:17:04 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -72.000 |  |
| 2026-05-08 00:11:56 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-08 00:09:11 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -144.000 |  |
| 2026-05-08 00:09:10 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -144.000 |  |
| 2026-05-08 00:07:45 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-05-08 00:06:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.111 |  |
| 2026-05-08 00:06:27 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-08 00:05:59 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.121 |  |
| 2026-05-08 00:05:51 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.149 |  |
| 2026-05-08 00:05:40 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 23.586 | 🔺 Rising |
| 2026-05-08 00:05:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 23.586 | 🔺 Rising |
| 2026-05-08 00:05:06 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.115 |  |
| 2026-05-08 00:05:05 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-08 00:05:01 | Thanamalwila (Kirindi Oya) | 3.45 | 🟢 Normal | 0.605 | 🔺 Rising |
| 2026-05-08 00:04:46 | Nakkala (Kumbukkan Oya) | 1.99 | 🟢 Normal | -0.252 |  |
| 2026-05-08 00:04:27 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-05-08 00:03:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-08 00:03:34 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-05-08 00:03:15 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.025 |  |
| 2026-05-08 00:03:15 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.049 |  |
| 2026-05-08 00:03:00 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:02:41 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.393 |  |
| 2026-05-08 00:02:40 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:02:35 | Kuda Oya (Kirindi Oya) | 3.73 | 🟢 Normal | -0.070 |  |
| 2026-05-08 00:02:23 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:02:22 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-08 00:01:50 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-05-08 00:01:40 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:01:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:00:30 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 00:05:40 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 23.586 | 🔺 Rising |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-08 00:05:01 | Thanamalwila (Kirindi Oya) | 3.45 | 🟢 Normal | 0.605 | 🔺 Rising |
| 2026-05-08 00:03:34 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-05-08 00:17:26 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.419 | 🔺 Rising |
| 2026-05-08 00:04:27 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-05-08 00:01:50 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-05-08 00:07:45 | Panadugama (Nilwala Ganga) | 4.49 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-05-08 00:03:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-08 00:11:56 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-08 00:05:05 | Pitabeddara (Nilwala Ganga) | 2.82 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-08 00:06:27 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-07 23:04:06 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-07 23:01:52 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 22:01:14 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:01:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:02:23 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:02:40 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:00:30 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 00:03:00 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 20:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 00:02:22 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-07 23:06:13 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.022 |  |
| 2026-05-08 00:03:15 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.025 |  |
| 2026-05-08 00:26:23 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.034 |  |
| 2026-05-08 00:03:15 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.049 |  |
| 2026-05-07 22:07:35 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.056 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-08 00:02:35 | Kuda Oya (Kirindi Oya) | 3.73 | 🟢 Normal | -0.070 |  |
| 2026-05-08 00:06:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.111 |  |
| 2026-05-08 00:05:06 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.115 |  |
| 2026-05-08 00:05:59 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.121 |  |
| 2026-05-08 00:05:51 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.149 |  |
| 2026-05-08 00:22:02 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -0.232 |  |
| 2026-05-08 00:04:46 | Nakkala (Kumbukkan Oya) | 1.99 | 🟢 Normal | -0.252 |  |
| 2026-05-08 00:02:41 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.393 |  |
| 2026-05-08 00:17:05 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -72.000 |  |
| 2026-05-08 00:09:11 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)