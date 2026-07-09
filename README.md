# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--09_23:30:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **201,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 23:30:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:26:57 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:13:02 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:13:00 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:08:24 | Glencourse (Kelani Ganga) | 9.39 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-07-09 23:06:38 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-07-09 23:05:59 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-09 23:05:43 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.028 |  |
| 2026-07-09 23:05:35 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.056 |  |
| 2026-07-09 23:05:23 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:05:21 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 23:05:17 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:53 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:50 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:22 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:20 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-09 23:03:50 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-07-09 23:03:45 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-09 23:03:27 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:26 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:25 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:07 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:02 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:54 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:44 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-07-09 23:02:36 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:26 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:20 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.236 |  |
| 2026-07-09 23:01:22 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:00:24 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-09 23:02:44 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-07-09 23:08:24 | Glencourse (Kelani Ganga) | 9.39 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-07-09 22:10:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-09 23:04:20 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-09 23:03:45 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-09 23:05:21 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-09 23:00:24 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:53 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:22 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-09 22:02:15 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:27 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-09 22:00:33 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:21 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:05:17 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:05:23 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:36 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:54 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:26:57 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:02 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:26 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:07 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:30:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:02:20 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:26 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:50 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:13:00 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:40 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:04:50 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:13:02 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:01:22 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:03:25 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-09 23:05:59 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-09 23:06:38 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-07-09 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.011 |  |
| 2026-07-09 23:05:43 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.028 |  |
| 2026-07-09 23:05:35 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.056 |  |
| 2026-07-09 23:03:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-07-09 23:02:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.236 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)