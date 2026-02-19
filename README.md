# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_05:31:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,992 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 05:31:58 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.003 |  |
| 2026-02-19 05:24:09 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 05:13:00 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:11:41 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-19 05:09:52 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-19 05:09:21 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-02-19 05:07:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.125 |  |
| 2026-02-19 05:05:40 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:05:38 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:05:20 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:05:16 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-02-19 05:04:58 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.032 |  |
| 2026-02-19 05:04:49 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:46 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:45 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.097 |  |
| 2026-02-19 05:04:41 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-19 05:04:35 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:33 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:16 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:14 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-19 05:03:50 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:03:38 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:03:37 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:03:30 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-02-19 05:02:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:02:31 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.026 |  |
| 2026-02-19 05:02:27 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:02:21 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:02:15 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-19 05:02:10 | Manampitiya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.089 |  |
| 2026-02-19 05:02:09 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:01:45 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 05:01:34 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-19 05:01:26 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:01:20 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:45:00 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 05:01:34 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-19 05:11:41 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-19 04:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-19 05:09:52 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-19 05:01:45 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 05:02:15 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-19 05:24:09 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 05:02:27 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:05:40 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:49 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:02:09 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:02:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:56 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:04:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:13:00 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:33 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:01:20 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:05:20 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:03:37 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:01:26 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:35 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:03:50 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:04:46 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:03:38 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:02:21 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:31:58 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.003 |  |
| 2026-02-19 05:09:21 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-02-19 05:05:16 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-02-19 05:04:41 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-18 18:01:50 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-19 05:04:14 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-19 05:02:31 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.026 |  |
| 2026-02-19 05:04:58 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.032 |  |
| 2026-02-19 05:03:30 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-02-19 05:02:10 | Manampitiya (Mahaweli Ganga) | 2.51 | 🟢 Normal | -0.089 |  |
| 2026-02-19 05:04:45 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.097 |  |
| 2026-02-19 05:07:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)