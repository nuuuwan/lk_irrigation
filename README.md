# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_19:23:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,382 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 19:23:32 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.080 |  |
| 2026-04-02 19:15:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | -0.016 |  |
| 2026-04-02 19:14:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.074 |  |
| 2026-04-02 19:14:13 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:10:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:09:46 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-04-02 19:09:11 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-02 19:08:32 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:08:22 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:08:05 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:06:51 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-02 19:06:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:06:16 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:06:16 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-02 19:05:38 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:04:55 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-04-02 19:04:55 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:04:39 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-02 19:04:10 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:36 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-02 19:03:23 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:15 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 19:03:12 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:12 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:09 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:02:59 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:02:57 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-02 19:02:27 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-02 19:02:23 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-02 19:02:06 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:01:31 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-02 19:01:25 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:01:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:00:15 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:00:15 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 19:04:55 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-04-02 19:09:11 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-04-02 19:04:39 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-02 19:02:57 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-02 19:06:51 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-02 19:03:36 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-02 19:06:16 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-02 19:03:15 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 19:02:06 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:14:13 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:09 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:01:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:08:32 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:00:15 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:08:22 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:12 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:04:55 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:06:16 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:05:38 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:02:59 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:08:05 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:04:10 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:06:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:12 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:10:20 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:01:25 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:03:23 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 19:09:46 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-04-02 19:02:23 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-02 19:01:31 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-02 19:15:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | -0.016 |  |
| 2026-04-02 19:02:27 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-02 19:00:15 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-04-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-04-02 19:14:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.074 |  |
| 2026-04-02 19:23:32 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)