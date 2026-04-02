# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_20:07:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 20:07:54 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 20:07:01 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-02 20:06:22 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.140 |  |
| 2026-04-02 20:06:17 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-02 20:06:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.107 |  |
| 2026-04-02 20:05:51 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:05:13 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:38 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-02 20:04:31 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-02 20:04:31 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 20:04:24 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:16 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:08 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:00 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:03:53 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 20:03:36 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 20:03:34 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:03:11 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-04-02 20:03:07 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:02:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:02:54 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:02:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-04-02 20:02:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 20:02:18 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:02:15 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-02 20:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | -0.026 |  |
| 2026-04-02 20:01:10 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 19:23:32 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.140 |  |
| 2026-04-02 19:15:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | -0.026 |  |
| 2026-04-02 19:14:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.107 |  |
| 2026-04-02 19:14:13 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 19:04:55 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-04-02 19:02:57 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-02 20:02:15 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-02 20:07:01 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-02 20:04:31 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-02 20:06:17 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-02 20:03:36 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 20:03:53 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 19:03:15 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 20:04:33 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-02 20:02:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 20:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 20:04:31 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 20:07:54 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 20:03:07 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:38 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:09 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:08:32 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:16 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:01:10 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:08:22 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:00 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:05:13 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:03:34 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:08 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:02:54 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:02:57 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:05:51 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:02:18 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:04:24 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 20:03:11 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-04-02 20:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | -0.026 |  |
| 2026-04-02 19:00:15 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-04-02 20:02:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-04-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-04-02 20:06:06 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.107 |  |
| 2026-04-02 20:06:22 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)