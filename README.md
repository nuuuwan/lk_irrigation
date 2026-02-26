# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_01:36:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,028 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 01:36:45 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:16:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:13:47 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-27 01:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.469 | 🔺 Rising |
| 2026-02-27 01:09:10 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:08:57 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-02-27 01:07:17 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:06:29 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.013 |  |
| 2026-02-27 01:06:22 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-02-27 01:05:31 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-27 01:05:28 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:04:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.137 |  |
| 2026-02-27 01:03:42 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.506 | 🔺 Rising |
| 2026-02-27 01:03:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-02-27 01:03:32 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 01:03:32 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-27 01:03:18 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:03:03 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:02:26 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:02:25 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-27 01:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.395 | 🔺 Rising |
| 2026-02-27 01:02:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:01:51 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:01:29 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-02-27 01:01:12 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-27 01:01:08 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 01:03:42 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.506 | 🔺 Rising |
| 2026-02-27 01:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.469 | 🔺 Rising |
| 2026-02-27 01:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.395 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-27 01:01:12 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-02-27 00:03:00 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-27 01:13:47 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-27 00:01:35 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-27 01:02:25 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-27 01:03:32 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 00:06:39 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-27 01:02:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 00:01:25 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:05:28 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:01:51 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 22:03:30 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:02:26 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-27 00:03:13 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:03:03 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 00:02:24 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 00:00:39 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:36:45 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:06:22 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:09:10 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:03:18 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:07:17 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:16:46 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:01:08 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 00:10:21 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-02-27 01:03:32 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-27 01:05:31 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-27 01:03:40 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2026-02-27 01:06:29 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.013 |  |
| 2026-02-27 01:08:57 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.018 |  |
| 2026-02-27 01:01:29 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-02-27 01:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-02-27 01:04:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)