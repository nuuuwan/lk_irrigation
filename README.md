# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_04:08:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,704 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 04:08:51 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:07:51 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.189 |  |
| 2026-02-12 04:07:09 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 04:06:54 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-12 04:06:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:06:28 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:06:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:05:30 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:05:13 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 04:04:34 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:04:24 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.222 |  |
| 2026-02-12 04:04:13 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:04:05 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-12 04:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 04:03:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 04:03:05 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:03:04 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:02:59 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-12 04:02:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:02:37 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:02:07 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:54 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:53 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:25 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.154 |  |
| 2026-02-12 04:01:24 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.010 |  |
| 2026-02-12 04:01:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:12 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.032 |  |
| 2026-02-12 04:00:59 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:58 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:56 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:55 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:54 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:52 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:43 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:41 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:54:21 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:43:29 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:43:06 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:42:42 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:42:31 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.189 |  |
| 2026-02-12 03:18:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 04:06:54 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-02-12 04:03:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 02:45:52 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 04:05:13 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 04:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 04:07:09 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 04:02:59 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-12 04:00:43 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:41 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:08:51 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-11 23:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:03:04 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:53 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:06:03 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:02:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:05:30 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:02:37 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:23 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:02:07 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:00:59 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:03:05 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:04:34 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:43:29 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:06:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:01:54 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-12 04:06:28 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 18:05:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-12 04:01:24 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:01:13 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:04:22 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.010 |  |
| 2026-02-12 04:04:05 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-12 03:05:09 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.015 |  |
| 2026-02-12 03:08:57 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-02-12 03:04:19 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-02-12 04:01:12 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.032 |  |
| 2026-02-12 04:01:25 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.154 |  |
| 2026-02-12 04:07:51 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.189 |  |
| 2026-02-12 04:04:24 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.222 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)