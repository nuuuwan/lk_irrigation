# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_04:05:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 04:05:12 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:04:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:04:55 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-01-18 04:04:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:04:19 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:04:06 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 04:03:36 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:03:34 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.183 |  |
| 2026-01-18 04:03:32 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:03:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-01-18 04:03:01 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 04:02:48 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:42 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:36 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:25 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:04 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:01:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:01:27 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:01:24 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-18 04:01:20 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-18 04:01:02 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:00:35 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-01-18 03:40:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.007 |  |
| 2026-01-18 03:32:35 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:31:09 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-18 03:25:41 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:22:42 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:15:52 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:12:35 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.013 |  |
| 2026-01-18 03:12:31 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:09:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-01-18 03:09:06 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-18 03:09:05 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-18 03:09:03 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-18 03:09:02 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-18 03:08:35 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 03:03:59 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-18 03:31:09 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-18 01:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-18 04:01:20 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-18 03:08:22 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-18 04:04:06 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 04:03:01 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 04:04:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:35 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:00:44 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:36 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 18:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:06:02 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:42 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:48 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:06:28 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:03:32 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:01:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:02:25 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:04:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:15:52 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 04:05:12 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:22:42 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:32:35 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:40:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.007 |  |
| 2026-01-18 04:04:19 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:03:36 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:02:04 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:01:02 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:01:27 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-18 04:04:55 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-01-18 04:03:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-01-18 03:12:35 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.013 |  |
| 2026-01-18 04:01:24 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-18 04:00:35 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-01-17 18:01:12 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.040 |  |
| 2026-01-18 04:03:34 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)