# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_23:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,257 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 23:15:10 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:12:11 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.056 |  |
| 2026-05-21 23:10:14 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:08:51 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:08:44 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-21 23:08:42 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:08:12 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:08:05 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.343 |  |
| 2026-05-21 23:06:46 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:06:20 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.343 |  |
| 2026-05-21 23:05:51 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 23:05:48 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:05:32 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.087 |  |
| 2026-05-21 23:05:27 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:05:23 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-05-21 23:04:48 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:04:08 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-21 23:04:07 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.029 |  |
| 2026-05-21 23:03:40 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:03:26 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.062 |  |
| 2026-05-21 23:03:02 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-21 23:02:48 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:46 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:45 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-21 23:02:32 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.025 |  |
| 2026-05-21 23:02:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:12 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:01:53 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 23:01:43 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:01:13 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:01:07 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-21 23:00:58 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:00:24 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 23:05:23 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-05-21 23:03:02 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-21 23:08:44 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-21 23:01:07 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-21 23:05:51 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-21 23:01:53 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 22:02:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-21 23:02:46 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:00:24 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:12 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-21 22:01:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:08:51 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:00:58 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:05:48 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:04:48 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:05:27 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:15:10 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:01:43 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-21 22:03:15 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:10:14 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:08:42 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:06:46 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:03:40 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:01:13 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:02:48 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:04:08 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-05-21 23:02:45 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-21 21:26:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.014 |  |
| 2026-05-21 23:02:32 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.025 |  |
| 2026-05-21 23:04:07 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.029 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-21 23:12:11 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.056 |  |
| 2026-05-21 23:03:26 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.062 |  |
| 2026-05-21 23:05:32 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.087 |  |
| 2026-05-21 23:08:05 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.343 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)