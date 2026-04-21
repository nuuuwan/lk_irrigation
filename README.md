# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_20:19:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,362 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 20:19:33 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-21 20:13:22 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-21 20:13:19 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.018 |  |
| 2026-04-21 20:12:48 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:09:54 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.070 |  |
| 2026-04-21 20:09:04 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.012 |  |
| 2026-04-21 20:08:28 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-04-21 20:08:23 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.041 |  |
| 2026-04-21 20:07:11 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-04-21 20:07:06 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-21 20:07:02 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | -0.128 |  |
| 2026-04-21 20:06:52 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:06:14 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 20:05:46 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.049 |  |
| 2026-04-21 20:05:39 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-04-21 20:05:36 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:04:49 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.069 |  |
| 2026-04-21 20:03:44 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-21 20:03:33 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-04-21 20:03:30 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-04-21 20:03:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.122 |  |
| 2026-04-21 20:03:19 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-21 20:03:13 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:03:13 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | 0.961 | 🔺 Rising |
| 2026-04-21 20:02:56 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.081 |  |
| 2026-04-21 20:02:52 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:02:49 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.031 |  |
| 2026-04-21 20:02:40 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.163 |  |
| 2026-04-21 20:02:05 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.099 |  |
| 2026-04-21 20:01:50 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:01:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-21 20:01:34 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.099 |  |
| 2026-04-21 20:01:22 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-04-21 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-04-21 20:00:08 | Wellawaya (Kirindi Oya) | 2.14 | 🟢 Normal | -0.389 |  |
| 2026-04-21 19:55:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.163 |  |
| 2026-04-21 19:50:36 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 20:03:13 | Kuda Oya (Kirindi Oya) | 2.62 | 🟢 Normal | 0.961 | 🔺 Rising |
| 2026-04-21 20:05:39 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 20:01:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-21 20:13:22 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 20:06:14 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 20:07:06 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-21 20:03:19 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-21 20:19:33 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-21 20:01:50 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:12:48 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:50:36 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:02:52 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:03:13 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:02:40 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:06:52 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-21 20:03:44 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-21 20:09:04 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.012 |  |
| 2026-04-21 20:13:19 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.018 |  |
| 2026-04-21 20:01:22 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-04-21 20:03:30 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.029 |  |
| 2026-04-21 20:02:49 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.031 |  |
| 2026-04-21 20:08:28 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-04-21 20:08:23 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.041 |  |
| 2026-04-21 20:05:46 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | -0.049 |  |
| 2026-04-21 20:07:11 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-04-21 20:03:33 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-04-21 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-04-21 20:04:49 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.069 |  |
| 2026-04-21 20:09:54 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.070 |  |
| 2026-04-21 20:02:56 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.081 |  |
| 2026-04-21 20:02:05 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.099 |  |
| 2026-04-21 20:01:34 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.099 |  |
| 2026-04-21 20:03:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.122 |  |
| 2026-04-21 20:07:02 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | -0.128 |  |
| 2026-04-21 20:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.163 |  |
| 2026-04-21 20:00:08 | Wellawaya (Kirindi Oya) | 2.14 | 🟢 Normal | -0.389 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)