# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_21:29:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,373 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 21:29:28 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.027 |  |
| 2026-02-12 21:17:30 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-12 21:16:28 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:10:40 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-02-12 21:09:22 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:09:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.653 | 🔺 Rising |
| 2026-02-12 21:08:07 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:08:05 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:07:58 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:07:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2026-02-12 21:07:40 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-12 21:07:36 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:07:35 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:06:58 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:05:44 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-02-12 21:05:44 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:05:42 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-02-12 21:05:42 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:05:41 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-02-12 21:05:40 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-02-12 21:05:38 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-02-12 21:05:26 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:05:04 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.101 |  |
| 2026-02-12 21:04:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:04:07 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-12 21:04:02 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:04:02 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:03:55 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-12 21:03:47 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-12 21:03:38 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:03:08 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:48 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-12 21:02:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:42 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:30 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-12 21:02:24 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:15 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-02-12 21:01:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:01:21 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 21:01:14 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:00:59 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:00:17 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 21:05:44 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-02-12 21:09:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.653 | 🔺 Rising |
| 2026-02-12 21:02:15 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-02-12 21:03:47 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-12 21:07:40 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-12 21:03:55 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-12 21:02:48 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 21:01:21 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 21:01:14 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:04:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:01:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:06:58 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:08:07 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:03:38 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 21:17:30 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-12 21:00:17 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:07:58 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:04:02 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:16:28 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:08:05 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:42 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:05:26 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:04:02 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:05:42 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:03:08 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:05:44 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:09:22 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:24 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:07:35 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-12 21:02:30 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-12 21:04:07 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-12 21:10:40 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-02-12 21:29:28 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.027 |  |
| 2026-02-12 21:07:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2026-02-12 21:05:04 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)