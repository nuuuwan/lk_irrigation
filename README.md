# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_23:29:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,184 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 23:29:48 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:18:58 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-24 23:13:46 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:09:50 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:09:04 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:07:09 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:48 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:16 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:06 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.012 |  |
| 2026-02-24 23:05:23 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.014 |  |
| 2026-02-24 23:04:33 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:03:37 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:03:21 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-24 23:03:15 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:03:15 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-24 23:03:08 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:03:04 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-02-24 23:02:54 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:02:50 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-24 23:02:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:02:38 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:02:27 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:02:09 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:02:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-02-24 23:02:04 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.027 |  |
| 2026-02-24 23:01:49 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:36 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:22 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:13 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:00:50 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.750 | 🔺 Rising |
| 2026-02-24 23:00:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.013 |  |
| 2026-02-24 23:00:32 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 23:00:50 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.750 | 🔺 Rising |
| 2026-02-24 23:00:32 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-24 23:02:50 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-24 23:03:21 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-24 23:03:15 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-24 23:18:58 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-24 23:02:54 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:03:15 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-24 22:00:49 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:22 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:03:37 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:02:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:13:46 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:36 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:29:48 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:07:09 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:16 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:48 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:01:49 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:04:33 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:09:50 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:02:27 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:09:04 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:02:04 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:02:38 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:02:09 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:01:13 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:03:08 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-02-24 23:06:06 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.012 |  |
| 2026-02-24 23:00:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.013 |  |
| 2026-02-24 23:05:23 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.014 |  |
| 2026-02-24 23:03:04 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-02-24 23:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.027 |  |
| 2026-02-24 23:02:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)