# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_13:13:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,627 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 13:13:20 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:10:49 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:09:18 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:07:53 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:06:59 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-02 13:06:42 | Siyambalanduwa (Heda Oya) | 1.42 | 🟢 Normal | -0.075 |  |
| 2026-01-02 13:05:29 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-02 13:04:42 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-01-02 13:04:31 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:04:15 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:03:40 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-01-02 13:03:37 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-02 13:03:11 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 13:03:10 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:03:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:03:02 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:02:59 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-02 13:02:58 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-01-02 13:02:56 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:02:41 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.015 |  |
| 2026-01-02 13:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-02 13:02:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:02:06 | Galgamuwa (Mee Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:02:01 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.206 |  |
| 2026-01-02 13:02:01 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-01-02 13:01:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:49 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-01-02 13:01:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:26 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:22 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:18 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.114 |  |
| 2026-01-02 13:00:59 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:00:53 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:00:45 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-01-02 12:22:15 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 13:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-02 13:05:29 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-02 13:03:37 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-02 12:18:40 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-02 13:02:59 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-02 13:03:11 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 05:06:54 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:03:04 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:02:56 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:00:59 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:02:06 | Galgamuwa (Mee Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:13:20 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:26 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:38 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:09:18 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:03:02 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:03:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:04:31 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:05:10 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:01:22 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:04:15 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:07:53 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:06:59 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-02 13:02:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:00:53 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:03:10 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:10:49 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-01-02 13:02:41 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.015 |  |
| 2026-01-02 13:04:42 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-01-02 13:02:01 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-01-02 13:02:58 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-01-02 13:00:45 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-01-02 13:01:49 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.041 |  |
| 2026-01-02 13:03:40 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-01-02 13:06:42 | Siyambalanduwa (Heda Oya) | 1.42 | 🟢 Normal | -0.075 |  |
| 2026-01-02 13:01:18 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.114 |  |
| 2026-01-02 13:02:01 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)