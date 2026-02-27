# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_03:26:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 03:26:23 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:22:07 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:13:19 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:12:17 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:12:15 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:10:29 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:10:27 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:10:07 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:10:04 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:07:54 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.026 |  |
| 2026-02-28 03:07:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-02-28 03:06:59 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:06:47 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:06:11 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:06:00 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:05:21 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:05:05 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-28 03:04:17 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:04:08 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:57 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:12 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:10 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 03:03:05 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:03 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:02:56 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:02:43 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:02:37 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.177 |  |
| 2026-02-28 03:02:37 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 03:02:21 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:01:39 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.007 |  |
| 2026-02-28 03:01:35 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-28 03:01:21 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:01:10 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:00:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-02-28 02:46:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:45:53 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 03:05:05 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-28 03:01:35 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-28 03:02:37 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-28 03:03:10 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 03:10:04 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:10:27 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:01:21 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:57 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:13:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 01:17:33 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:05:21 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:12:17 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:22:07 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:04:17 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:02:56 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:26:23 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:06:59 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:03 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:04:08 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:06:47 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:06:11 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:03:42 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:32:29 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:12:19 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:13:19 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:03:05 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:02:43 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-28 03:01:39 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | -0.007 |  |
| 2026-02-28 03:06:00 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:10:29 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:00:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:01:10 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:02:21 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-28 03:07:54 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.026 |  |
| 2026-02-27 18:05:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.028 |  |
| 2026-02-28 03:07:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-02-27 22:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.087 |  |
| 2026-02-28 03:02:37 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)