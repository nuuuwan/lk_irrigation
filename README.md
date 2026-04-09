# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_06:27:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,140 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 06:27:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:21:23 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-09 06:17:13 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:10:28 | Panadugama (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-04-09 06:10:05 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:10:03 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-09 06:08:17 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-09 06:07:55 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:06:36 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-04-09 06:06:33 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:06:08 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-04-09 06:06:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:06:05 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-09 06:05:57 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-09 06:05:52 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-04-09 06:05:37 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.033 |  |
| 2026-04-09 06:05:26 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.094 |  |
| 2026-04-09 06:05:23 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:04:34 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.076 |  |
| 2026-04-09 06:03:50 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-09 06:03:43 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:03:21 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:03:21 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:03:08 | Weraganthota (Mahaweli Ganga) | -3.82 | 🟢 Normal | -0.587 |  |
| 2026-04-09 06:03:02 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.040 |  |
| 2026-04-09 06:02:43 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:02:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:02:16 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-09 06:02:11 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:01:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:01:32 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-09 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-04-09 06:01:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:01:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:00:34 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.540 | 🔺 Rising |
| 2026-04-09 06:00:12 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 06:00:34 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.540 | 🔺 Rising |
| 2026-04-09 05:13:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-09 06:03:50 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-09 06:10:03 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-09 06:02:16 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-09 06:06:05 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-09 06:01:32 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-09 06:08:17 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-09 06:21:23 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-09 06:03:21 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:01:09 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:03:43 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:05:23 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 06:00:12 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:01:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:01:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:02:11 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:27:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 18:02:48 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:06:33 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:02:43 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:10:05 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:06:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:02:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:03:21 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:17:13 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:07:55 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-09 06:06:08 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-04-09 06:05:57 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-08 18:02:20 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 06:10:28 | Panadugama (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-04-09 06:06:36 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-04-09 06:05:52 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-04-09 06:01:21 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-04-09 06:05:37 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.033 |  |
| 2026-04-09 06:03:02 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.040 |  |
| 2026-04-09 06:04:34 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.076 |  |
| 2026-04-09 06:05:26 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.094 |  |
| 2026-04-09 06:03:08 | Weraganthota (Mahaweli Ganga) | -3.82 | 🟢 Normal | -0.587 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)