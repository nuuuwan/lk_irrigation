# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_23:16:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,783 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 23:16:05 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:14:17 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:08:50 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-09 23:07:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:07:26 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:07:07 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:06:33 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:05:55 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:05:36 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 23:04:34 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:04:13 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:04:13 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |
| 2026-04-09 23:04:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:03:57 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.078 |  |
| 2026-04-09 23:03:53 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:03:46 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.020 |  |
| 2026-04-09 23:03:16 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:03:04 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-09 23:02:36 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-04-09 23:02:35 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:12 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:01:41 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:01:36 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:01:07 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:01:01 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 23:01:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-09 23:00:56 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:25:37 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-09 22:25:36 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 23:02:36 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-04-09 23:03:04 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-09 23:01:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-09 23:08:50 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-09 23:01:01 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 23:05:36 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 22:00:11 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:01:36 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:07:26 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:04:13 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:01:41 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:07:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:14:17 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:06:33 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:03:16 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:12 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:00:56 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:35 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:55 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:04:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:07:07 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:05:55 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:03:53 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:04:34 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:11 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:16:05 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:03:46 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.020 |  |
| 2026-04-09 22:06:03 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-04-09 23:03:57 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.078 |  |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-09 23:04:13 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.091 |  |
| 2026-04-09 22:12:15 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)