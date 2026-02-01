# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_17:30:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,730 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 17:30:39 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:27:59 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.007 |  |
| 2026-02-01 17:19:43 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 17:19:33 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:14:11 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-01 17:08:56 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 17:08:43 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-01 17:08:02 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-02-01 17:07:44 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-01 17:07:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.087 |  |
| 2026-02-01 17:06:32 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-02-01 17:06:31 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:06:01 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:05:40 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:05:15 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-01 17:04:56 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-02-01 17:04:39 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:04:38 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:04:24 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-01 17:04:16 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.048 |  |
| 2026-02-01 17:04:14 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:03:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 17:03:40 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-02-01 17:03:35 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 17:03:20 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 17:02:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:02:52 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-02-01 17:02:17 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:02:09 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:51 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:47 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:45 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.023 |  |
| 2026-02-01 17:01:38 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-02-01 17:01:27 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.015 |  |
| 2026-02-01 17:01:17 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.103 |  |
| 2026-02-01 17:01:16 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.060 |  |
| 2026-02-01 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:00:56 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 17:00:49 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 17:05:15 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-02-01 17:04:24 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-01 17:00:56 | Thanthirimale (Malwathu Oya) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 17:03:20 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 17:19:43 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 17:00:49 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 17:03:35 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 17:08:56 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 17:14:11 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-01 17:05:40 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:45 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:51 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:02:17 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:04:39 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:30:39 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:01:47 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:02:09 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:02:57 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:04:38 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:06:01 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:04:14 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:06:31 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 17:27:59 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.007 |  |
| 2026-02-01 17:08:02 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-02-01 17:07:44 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-01 17:03:40 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-02-01 17:08:43 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-01 17:03:42 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 17:02:52 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-02-01 17:01:27 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.015 |  |
| 2026-02-01 17:01:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.023 |  |
| 2026-02-01 17:04:56 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-02-01 17:06:32 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-02-01 17:04:16 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.048 |  |
| 2026-02-01 17:01:16 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.060 |  |
| 2026-02-01 17:01:38 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-02-01 17:07:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.087 |  |
| 2026-02-01 17:01:17 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)