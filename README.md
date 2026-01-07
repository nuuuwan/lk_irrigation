# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_22:10:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,445 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 22:10:55 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-01-07 22:08:41 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-01-07 22:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 22:07:38 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.028 |  |
| 2026-01-07 22:07:00 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-01-07 22:05:54 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:05:49 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:05:38 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:05:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.028 |  |
| 2026-01-07 22:04:55 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:04:25 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-01-07 22:04:24 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-07 22:03:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-01-07 22:03:15 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:03:15 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-07 22:03:10 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:02:48 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:02:42 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-07 22:02:40 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:02:32 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-01-07 22:02:27 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-01-07 22:02:13 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:02:12 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-01-07 22:01:59 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:49 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:47 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:19 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.012 |  |
| 2026-01-07 22:01:12 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:05 | Manampitiya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-01-07 22:00:59 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:00:30 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-01-07 22:00:30 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:21:16 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:15:13 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 22:04:25 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-01-07 22:02:27 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-01-07 22:10:55 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-01-07 22:07:00 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-01-07 22:03:15 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-07 21:06:47 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-07 22:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 22:02:13 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:12 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:00:30 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:47 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:02:48 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:05:49 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:02:40 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:03:10 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:59 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:03:15 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:05:54 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:05:38 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:49 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:04:55 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:02:42 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:06:35 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-01-07 22:00:30 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2026-01-07 22:02:32 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-01-07 22:04:24 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-01-07 22:08:41 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-01-07 22:01:19 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.012 |  |
| 2026-01-07 22:01:05 | Manampitiya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-01-07 22:02:12 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-07 22:05:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.028 |  |
| 2026-01-07 22:07:38 | Urawa (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.028 |  |
| 2026-01-07 21:05:18 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-01-07 22:03:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)