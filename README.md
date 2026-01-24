# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_21:18:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,684 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 21:18:39 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2026-01-24 21:16:13 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:16:01 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:14:14 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:10:13 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-24 21:09:50 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:09:29 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.028 |  |
| 2026-01-24 21:09:26 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:08:45 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:07:03 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:06:58 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:05:52 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 21:05:33 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:05:25 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:05:15 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:05:08 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.105 |  |
| 2026-01-24 21:04:50 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:04:42 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:04:34 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-24 21:04:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:04:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:03:55 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-01-24 21:03:41 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-01-24 21:03:32 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.117 |  |
| 2026-01-24 21:03:04 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:03:02 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:36 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:31 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:30 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.092 |  |
| 2026-01-24 21:02:11 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:01:50 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:01:38 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 21:00:39 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-24 20:37:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 21:03:55 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-01-24 21:10:13 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-01-24 21:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 21:05:52 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 21:01:38 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:04:50 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:31 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:01:50 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:36 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:00:39 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:09:26 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:03:02 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:03:04 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:06:58 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:04:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:16:13 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:07:03 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:04:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:09:50 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:11 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:05:33 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:14:14 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:16:01 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:04:42 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:05:25 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:05:15 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:14:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:18:39 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2026-01-24 21:04:34 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-24 21:03:41 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-24 20:24:28 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-01-24 21:09:29 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.028 |  |
| 2026-01-24 21:02:30 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.092 |  |
| 2026-01-24 21:05:08 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.105 |  |
| 2026-01-24 21:03:32 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)