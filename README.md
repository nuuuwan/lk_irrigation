# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_20:07:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,477 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 20:07:33 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:07:18 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:07:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.072 |  |
| 2026-01-06 20:06:21 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-01-06 20:06:16 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:05:51 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -0.096 |  |
| 2026-01-06 20:05:45 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:05:41 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.079 |  |
| 2026-01-06 20:05:24 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:05:10 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-06 20:04:22 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:04:17 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-06 20:04:10 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 20:04:07 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:03:47 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:03:27 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | -0.022 |  |
| 2026-01-06 20:03:18 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-06 20:03:15 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:03:09 | Manampitiya (Mahaweli Ganga) | 3.82 | 🟡 Alert | -0.010 |  |
| 2026-01-06 20:02:44 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:02:44 | Siyambalanduwa (Heda Oya) | 3.15 | 🟢 Normal | -0.505 |  |
| 2026-01-06 20:02:43 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:02:43 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.060 |  |
| 2026-01-06 20:02:13 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:01:59 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:01:56 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 20:01:55 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | -0.089 |  |
| 2026-01-06 20:01:48 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-06 20:01:43 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-06 20:01:42 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.117 |  |
| 2026-01-06 20:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:20:36 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.117 |  |
| 2026-01-06 19:14:39 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.017 |  |
| 2026-01-06 19:11:16 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 20:03:09 | Manampitiya (Mahaweli Ganga) | 3.82 | 🟡 Alert | -0.010 |  |
| 2026-01-06 20:05:10 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-06 20:01:56 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-06 20:01:43 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 20:04:10 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 20:07:18 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:06:16 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:02:13 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:03:15 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:05:24 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:02:44 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:01:59 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:04:34 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:07:33 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:04:22 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:03:47 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:02:43 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-06 20:04:07 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:09:22 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-06 20:03:18 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-06 20:04:17 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-06 20:01:48 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-06 19:14:39 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.017 |  |
| 2026-01-06 20:06:21 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-01-06 20:03:27 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | -0.022 |  |
| 2026-01-06 19:08:51 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2026-01-06 19:11:16 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.026 |  |
| 2026-01-06 20:02:43 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.060 |  |
| 2026-01-06 19:05:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-01-06 20:07:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.072 |  |
| 2026-01-06 20:05:41 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.079 |  |
| 2026-01-06 20:01:55 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | -0.089 |  |
| 2026-01-06 20:05:51 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -0.096 |  |
| 2026-01-06 20:01:42 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.117 |  |
| 2026-01-06 20:02:44 | Siyambalanduwa (Heda Oya) | 3.15 | 🟢 Normal | -0.505 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)