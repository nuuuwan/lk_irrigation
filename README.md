# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_15:16:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 15:16:34 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 15:12:31 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:09:59 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:09:53 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:09:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:07:24 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:06:59 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:06:56 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:06:26 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:05:05 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:04:55 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-02-13 15:04:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:04:17 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:04:13 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 15:04:03 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-02-13 15:03:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 15:03:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-13 15:03:44 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:03:38 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:03:17 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.032 |  |
| 2026-02-13 15:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.060 |  |
| 2026-02-13 15:02:50 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:42 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -1.021 |  |
| 2026-02-13 15:02:34 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:02:27 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-02-13 15:02:21 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:15 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:09 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:01:54 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.026 |  |
| 2026-02-13 15:01:49 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:01:38 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-13 15:01:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-02-13 15:01:23 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:01:22 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:01:07 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 15:00:54 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-02-13 15:00:33 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-02-13 15:00:31 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:00:11 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.051 |  |
| 2026-02-13 14:57:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 15:01:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-02-13 15:01:38 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-13 15:16:34 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 15:04:13 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 15:03:59 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 15:01:07 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 15:02:15 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:01:49 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:05:05 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:21 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:50 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:09:59 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:09:23 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:04:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:02:09 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:04:17 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:06:59 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:00:31 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:01:23 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:12:31 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:07:24 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 15:03:44 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:06:56 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:03:38 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:09:53 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:02:34 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-13 15:03:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-02-13 15:00:33 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-02-13 15:00:54 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-02-13 15:04:03 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-02-13 15:04:55 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-02-13 15:01:54 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.026 |  |
| 2026-02-13 15:03:17 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.032 |  |
| 2026-02-13 15:02:27 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-02-13 15:00:11 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.051 |  |
| 2026-02-13 15:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.060 |  |
| 2026-02-13 15:02:42 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -1.021 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)