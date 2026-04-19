# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_19:23:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,536 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 19:23:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.001 |  |
| 2026-04-19 19:20:27 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:11:56 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.008 |  |
| 2026-04-19 19:11:24 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:11:06 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-19 19:10:29 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-04-19 19:10:01 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:08:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 19:07:36 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-19 19:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.037 |  |
| 2026-04-19 19:07:31 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-04-19 19:07:23 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:07:03 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-19 19:06:18 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:06:17 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:05:54 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 19:05:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:05:08 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.061 |  |
| 2026-04-19 19:04:45 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:04:44 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:04:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-04-19 19:04:25 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.086 |  |
| 2026-04-19 19:03:49 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-19 19:03:42 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:03:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.140 |  |
| 2026-04-19 19:03:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:03:37 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:03:14 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-19 19:02:44 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:02:30 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:02:16 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:02:09 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 19:01:41 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:00:53 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 19:00:13 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-19 19:00:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 19:04:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-04-19 19:07:31 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-04-19 19:03:49 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-19 19:03:14 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-19 19:07:03 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-19 19:11:06 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-19 19:00:13 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-19 19:02:09 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 19:07:36 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-19 19:00:53 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 19:05:54 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 19:08:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 19:23:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.001 |  |
| 2026-04-19 19:10:01 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:00:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:01:41 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:03:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:03:42 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:03:37 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:20:27 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:04:45 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:06:18 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:07:23 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:11:24 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:05:11 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:06:17 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-19 19:11:56 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.008 |  |
| 2026-04-19 19:04:44 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:02:30 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:02:16 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:02:44 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-19 19:10:29 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-04-19 19:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.037 |  |
| 2026-04-19 19:05:08 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.061 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-19 19:04:25 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.086 |  |
| 2026-04-19 19:03:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)