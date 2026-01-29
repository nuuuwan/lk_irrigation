# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_19:20:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,090 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 19:20:03 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:19:04 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:17:45 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:17:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:09:13 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-01-29 19:07:34 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:07:32 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:07:21 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:07:02 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:06:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-01-29 19:06:49 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:06:31 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:48 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:39 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:38 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:35 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:05 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:36 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:35 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:04:17 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:17 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:09 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:03:54 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:03:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-29 19:03:25 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-29 19:03:23 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-29 19:02:54 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:53 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:45 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:02:30 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:02:10 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:01:47 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-01-29 19:01:38 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:01:13 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:00:43 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 19:00:39 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 19:09:13 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-01-29 19:03:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-29 19:03:25 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-29 19:03:23 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-29 19:00:39 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-29 19:00:43 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 18:02:43 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 19:06:31 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:17:45 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:17:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:54 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:07:32 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 18:04:09 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:17 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:30 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:48 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:17 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:19:04 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:07:02 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:03:54 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:07:21 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:01:13 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:45 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:38 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:06:49 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:35 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 18:01:27 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:20:03 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:09 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:04:36 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:01:38 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:05:39 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:04:35 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:07:34 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:02:10 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:02:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-29 19:06:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-01-29 19:01:47 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)