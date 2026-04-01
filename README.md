# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_05:11:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,833 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 05:11:36 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:11:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:11:03 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:06:49 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.012 |  |
| 2026-04-02 05:06:43 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-04-02 05:05:53 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:05:12 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.187 |  |
| 2026-04-02 05:04:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:04:37 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.092 |  |
| 2026-04-02 05:04:37 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-02 05:04:22 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-02 05:04:08 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:03:45 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -4.421 |  |
| 2026-04-02 05:03:42 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-04-02 05:03:31 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-02 05:02:57 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | -0.020 |  |
| 2026-04-02 05:02:56 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 05:02:48 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -4.421 |  |
| 2026-04-02 05:02:38 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:35 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:29 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 05:02:22 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:09 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 05:02:06 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:01:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.066 |  |
| 2026-04-02 05:01:50 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.024 |  |
| 2026-04-02 05:01:43 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:01:33 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:00:18 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:00:14 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-02 04:40:53 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-02 04:37:17 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.024 |  |
| 2026-04-02 04:36:59 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.024 |  |
| 2026-04-02 04:36:42 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.024 |  |
| 2026-04-02 04:36:26 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.024 |  |
| 2026-04-02 04:36:20 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 04:25:02 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 04:21:37 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-02 04:20:30 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 05:00:14 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-02 04:02:24 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 05:02:09 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 05:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 05:04:37 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-02 05:02:28 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 05:03:31 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-02 05:02:35 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:32 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:06 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:38 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:02:10 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:11:36 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:11:03 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:56 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:05:53 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 04:20:30 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:11:30 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:01:33 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:00:18 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:22 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:02:29 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:04:53 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 04:11:09 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:04:08 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 05:06:43 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-04-01 18:05:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-02 05:04:22 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-04-02 05:06:49 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.012 |  |
| 2026-04-02 04:03:43 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-04-02 05:03:42 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-04-02 05:02:57 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | -0.020 |  |
| 2026-04-02 05:01:50 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.024 |  |
| 2026-04-01 18:01:16 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.031 |  |
| 2026-04-02 05:01:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.066 |  |
| 2026-04-02 05:04:37 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.092 |  |
| 2026-04-02 05:05:12 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.187 |  |
| 2026-04-02 03:03:39 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.217 |  |
| 2026-04-02 05:03:45 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -4.421 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)