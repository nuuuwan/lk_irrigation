# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_20:28:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,507 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 20:28:44 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -36.000 |  |
| 2026-04-29 20:28:43 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -36.000 |  |
| 2026-04-29 20:13:25 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:11:17 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.046 |  |
| 2026-04-29 20:09:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:09:10 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.047 |  |
| 2026-04-29 20:08:26 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:08:15 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-29 20:07:30 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.030 |  |
| 2026-04-29 20:06:46 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-29 20:06:31 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:05:36 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-04-29 20:05:24 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:05:10 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:04:32 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 20:04:27 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-04-29 20:04:25 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-29 20:03:46 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.058 |  |
| 2026-04-29 20:03:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:03:29 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-04-29 20:02:57 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-29 20:02:44 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:02:42 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:02:35 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-29 20:02:33 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-04-29 20:02:09 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 20:01:50 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 20:01:50 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:01:19 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 20:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:01:18 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.483 |  |
| 2026-04-29 20:00:31 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 20:00:29 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:00:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 19:58:36 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 20:06:46 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-29 20:08:15 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-29 20:00:31 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 20:03:48 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-29 18:03:06 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 20:02:35 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-29 20:04:32 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-29 20:01:19 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 20:02:57 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-29 18:03:08 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 20:02:09 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 20:01:50 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 20:00:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:01:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:02:42 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:00:29 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:09:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:13:25 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:03:29 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:05:24 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:08:26 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:02:44 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:01:50 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:08:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-04-29 20:05:10 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:04:25 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:06:31 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-04-29 20:03:29 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-04-29 20:02:33 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-04-29 20:07:30 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.030 |  |
| 2026-04-29 20:04:27 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-04-29 20:11:17 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.046 |  |
| 2026-04-29 20:09:10 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.047 |  |
| 2026-04-29 18:02:02 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-04-29 20:05:36 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-04-29 20:03:46 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.058 |  |
| 2026-04-29 20:01:18 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.483 |  |
| 2026-04-29 20:28:44 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)