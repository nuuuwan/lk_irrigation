# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_19:19:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,223 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 19:19:36 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 19:13:56 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-22 19:09:17 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-22 19:09:15 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:07:52 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-22 19:06:50 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-22 19:06:40 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.044 |  |
| 2026-04-22 19:06:33 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.046 |  |
| 2026-04-22 19:06:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:06:08 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.011 |  |
| 2026-04-22 19:06:08 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-22 19:05:43 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 19:05:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.088 |  |
| 2026-04-22 19:05:40 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-22 19:05:35 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:05:31 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:05:16 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-22 19:04:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 19:04:26 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 19:04:09 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-22 19:04:00 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-04-22 19:02:59 | Kuda Oya (Kirindi Oya) | 3.90 | 🟢 Normal | 1.130 | 🔺 Rising |
| 2026-04-22 19:02:44 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.099 |  |
| 2026-04-22 19:02:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:02:29 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 19:02:06 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-22 19:02:02 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:01:54 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:01:49 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-22 19:01:07 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.031 |  |
| 2026-04-22 19:00:38 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:00:26 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-04-22 19:00:13 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-04-22 19:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.909 | 🔺 Rising |
| 2026-04-22 19:00:00 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 19:02:59 | Kuda Oya (Kirindi Oya) | 3.90 | 🟢 Normal | 1.130 | 🔺 Rising |
| 2026-04-22 19:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.909 | 🔺 Rising |
| 2026-04-22 19:00:13 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-04-22 19:04:00 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-04-22 19:00:26 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-04-22 19:06:08 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-22 19:02:06 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-22 19:06:50 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-22 19:13:56 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-22 19:19:36 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 19:05:16 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-22 19:07:52 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-22 19:09:17 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-22 19:04:26 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 19:05:43 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 19:04:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-22 19:02:29 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 19:00:38 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:02:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:11:05 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:05:35 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:06:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:02:02 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:05:31 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:01:54 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:09:15 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-22 19:04:09 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 19:01:49 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 19:06:08 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.011 |  |
| 2026-04-22 19:01:07 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.031 |  |
| 2026-04-22 19:05:40 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-22 19:06:40 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.044 |  |
| 2026-04-22 19:06:33 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.046 |  |
| 2026-04-22 19:05:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.088 |  |
| 2026-04-22 19:02:44 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)