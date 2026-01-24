# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_22:47:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,721 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 22:47:05 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-24 22:45:08 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-01-24 22:44:30 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:34:36 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-01-24 22:33:04 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.007 |  |
| 2026-01-24 22:28:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-24 22:11:07 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.100 |  |
| 2026-01-24 22:10:01 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:08:53 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-01-24 22:07:10 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:57 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:55 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:48 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:19 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:05:56 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:05:46 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-24 22:04:58 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:04:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:04:09 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.012 |  |
| 2026-01-24 22:04:01 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:04:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:03:45 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:03:41 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-24 22:03:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-01-24 22:03:23 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-24 22:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:03:10 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:02:52 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:02:42 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:02:33 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:01:43 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:01:42 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:01:42 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:01:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-01-24 22:00:23 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 22:08:53 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-01-24 22:03:41 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-24 22:05:46 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-24 22:28:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-24 22:47:05 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-24 22:00:23 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:10:01 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:02:33 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:44:30 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:57 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:01:42 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:04:58 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:01:43 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:02:42 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:55 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:04:01 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:07:10 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:04:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:04:01 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-24 21:02:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:48 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:03:10 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:05:56 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:06:19 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:01:42 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:03:45 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 22:33:04 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.007 |  |
| 2026-01-24 22:03:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-01-24 22:03:23 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-24 22:04:09 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.012 |  |
| 2026-01-24 22:45:08 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-01-24 22:34:36 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-24 22:01:22 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2026-01-24 22:11:07 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)