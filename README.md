# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_16:20:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,598 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 16:20:31 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-23 16:14:37 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:14:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:11:43 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 16:10:42 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 16:10:34 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:10:06 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:09:58 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:07:45 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:07:25 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-01-23 16:06:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:05:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:05:48 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:05:31 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:04:45 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:04:08 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:04:02 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.095 |  |
| 2026-01-23 16:03:52 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:03:36 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-23 16:03:28 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:03:14 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:02:54 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:02:51 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-23 16:02:35 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:02:35 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-23 16:02:21 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 16:02:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:02:08 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:02:02 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:57 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:01:55 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:21 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:11 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:00 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:00:58 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:00:57 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:00:11 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.037 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 16:02:51 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-23 16:20:31 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-01-23 16:00:11 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-23 15:13:47 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-23 16:02:35 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-23 16:02:21 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 16:10:42 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 16:11:43 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 16:02:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:02:35 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:00:57 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:02:08 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:14:37 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:55 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:10:06 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:07:45 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:05:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:04:45 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:21 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:14:02 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:03:52 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:05:48 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:09:58 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:03:28 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:06:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:05:31 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:10:34 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:03:14 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:02:02 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:01:11 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 16:07:25 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-01-23 16:01:57 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:00:58 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:04:08 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:02:54 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:01:00 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-23 16:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-23 16:04:02 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)