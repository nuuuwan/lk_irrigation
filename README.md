# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_08:13:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,415 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 08:13:14 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:11:10 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.046 |  |
| 2026-02-07 08:09:35 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:09:00 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:07:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.111 |  |
| 2026-02-07 08:06:57 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 08:05:57 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.065 |  |
| 2026-02-07 08:05:51 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-02-07 08:05:45 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.143 |  |
| 2026-02-07 08:05:36 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:05:35 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:05:10 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.013 |  |
| 2026-02-07 08:05:05 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-02-07 08:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 08:04:20 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.256 |  |
| 2026-02-07 08:03:46 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:44 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:42 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:31 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-07 08:03:24 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:21 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:15 | Horowpothana (Yan Oya) | 2.72 | 🟢 Normal | -0.030 |  |
| 2026-02-07 08:03:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:04 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 08:02:53 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-07 08:02:52 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 08:02:47 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:02:45 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:02:38 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:02:27 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-07 08:02:15 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 08:02:07 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-07 08:01:46 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.030 |  |
| 2026-02-07 08:01:45 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:01:01 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:00:25 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:57:18 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 08:02:27 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-07 08:03:31 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-07 08:02:53 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-07 08:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 08:03:04 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 07:10:50 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-07 08:02:15 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 08:02:52 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 08:06:57 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 08:03:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:01:45 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:05:35 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:05:36 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:09:00 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:01:01 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:02:38 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:09:35 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:42 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:13:14 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:24 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:00:25 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:44 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:02:45 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:21 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:15:11 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:02:47 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:03:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 08:05:05 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-02-07 08:02:07 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-07 08:05:10 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.013 |  |
| 2026-02-07 08:03:15 | Horowpothana (Yan Oya) | 2.72 | 🟢 Normal | -0.030 |  |
| 2026-02-07 08:01:46 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.030 |  |
| 2026-02-07 08:05:51 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-02-07 08:11:10 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.046 |  |
| 2026-02-07 08:05:57 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.065 |  |
| 2026-02-07 07:03:45 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.075 |  |
| 2026-02-07 08:07:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.111 |  |
| 2026-02-07 08:05:45 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.143 |  |
| 2026-02-07 08:04:20 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)