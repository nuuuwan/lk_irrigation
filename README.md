# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_21:10:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,461 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 21:10:00 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-26 21:07:27 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:07:11 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-26 21:06:42 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:06:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:06:05 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:06:05 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:05:46 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:05:20 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-26 21:05:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-01-26 21:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.063 |  |
| 2026-01-26 21:04:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2026-01-26 21:03:38 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-26 21:03:12 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:03:11 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:03:07 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.030 |  |
| 2026-01-26 21:03:05 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-26 21:02:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:02:42 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:02:22 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.421 |  |
| 2026-01-26 21:02:15 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:01:52 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-26 21:01:48 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 21:01:44 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-26 21:01:31 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-26 21:01:22 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:01:21 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:01:12 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-01-26 21:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:00:16 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:00:13 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:00:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 20:17:31 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 20:16:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 20:06:50 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-01-26 21:03:05 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-26 21:01:44 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-01-26 21:03:38 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-26 21:05:20 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-26 21:01:48 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 20:08:42 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:00:09 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:00:13 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:00:09 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:01:21 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:06:05 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:30 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:03:11 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:03:12 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:02:15 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-26 20:03:39 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:06:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:02:42 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:00:16 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:06:05 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:02:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:07:27 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:05:46 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-26 20:16:37 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:01:22 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:06:42 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-26 21:10:00 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-26 21:07:11 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-26 21:01:31 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-26 21:01:12 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-01-26 21:01:52 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-26 21:03:07 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.030 |  |
| 2026-01-26 21:05:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-01-26 21:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.063 |  |
| 2026-01-26 21:04:09 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2026-01-26 21:02:22 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.421 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)