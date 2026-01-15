# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_23:26:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 23:26:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-15 23:23:22 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:19:04 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-01-15 23:15:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.026 |  |
| 2026-01-15 23:13:50 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.027 |  |
| 2026-01-15 23:13:22 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:06:05 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:05:34 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 23:04:51 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:04:20 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:04:01 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-15 23:04:00 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-15 23:03:52 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:03:46 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:37 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-15 23:03:33 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:26 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:03:14 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:04 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:04 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.061 |  |
| 2026-01-15 23:02:50 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:02:45 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:02:29 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:02:11 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-01-15 23:01:46 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:01:42 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-01-15 23:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 23:01:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:01:20 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 23:01:01 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:00:53 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:00:08 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-15 22:46:45 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 23:02:11 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-01-15 23:04:01 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-15 23:03:37 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-15 23:26:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-15 23:04:00 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-15 23:01:20 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 23:05:34 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 23:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 23:03:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:46 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:14 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:01:46 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:13:22 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 18:03:50 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:02:45 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:04:20 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:00:08 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:06:05 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:04:51 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:33 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:23:22 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:01:27 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:03:04 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 23:19:04 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-01-15 23:02:50 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:03:26 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:01:01 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:03:52 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:02:29 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:00:53 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-01-15 23:01:42 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-01-15 22:05:48 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2026-01-15 22:03:52 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.023 |  |
| 2026-01-15 23:15:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.026 |  |
| 2026-01-15 23:13:50 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.027 |  |
| 2026-01-15 18:02:13 | Thanthirimale (Malwathu Oya) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-01-15 21:09:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.048 |  |
| 2026-01-15 23:03:04 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.061 |  |
| 2026-01-15 18:07:05 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.400 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)