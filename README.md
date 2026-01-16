# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_23:29:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,550 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 23:29:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2026-01-16 23:23:11 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:20:56 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-16 23:19:40 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:17:56 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:11:47 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-16 23:10:06 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:09:15 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:08:07 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-16 23:06:05 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:05:08 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.074 |  |
| 2026-01-16 23:04:08 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:03:41 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.042 |  |
| 2026-01-16 23:03:31 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-16 23:03:28 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:03:12 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:03:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-16 23:03:08 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:53 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-16 23:02:46 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 23:02:38 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:13 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:10 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:10 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:10 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-16 23:01:55 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:50 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:43 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:29 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:21 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:00:38 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-16 23:00:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 23:08:07 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-16 23:03:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-16 23:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-16 18:00:22 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-16 22:05:38 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-16 23:02:46 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 23:20:56 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-16 23:23:11 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:50 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:03:31 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:10 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-16 18:06:10 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:04:08 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:38 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:03:08 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:09:15 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:19:40 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:55 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:21 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:00:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:10 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:03:12 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:17:56 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:29 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:02:13 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:10:06 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-16 21:06:12 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:01:11 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:06:05 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-16 23:11:47 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-16 23:02:53 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-16 23:02:10 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-16 23:00:38 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-16 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-01-16 23:29:26 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2026-01-16 23:03:41 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.042 |  |
| 2026-01-16 23:05:08 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)