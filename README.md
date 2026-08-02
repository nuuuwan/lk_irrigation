# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_10:22:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 10:22:17 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.140 |  |
| 2026-08-02 10:15:38 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:15:08 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:10:44 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-08-02 10:10:28 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:08:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:08:07 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.038 |  |
| 2026-08-02 10:07:44 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:07:02 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-02 10:06:11 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-08-02 10:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:05:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-08-02 10:05:23 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:05:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.088 |  |
| 2026-08-02 10:05:00 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:04:51 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.029 |  |
| 2026-08-02 10:04:20 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-02 10:04:13 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-08-02 10:03:47 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-08-02 10:03:46 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:03:38 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:03:15 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:03:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:02:45 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.103 |  |
| 2026-08-02 10:02:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:02:40 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-02 10:02:34 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-02 10:02:30 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:02:15 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-02 10:02:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:02:03 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:01:35 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-02 10:01:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-08-02 10:01:23 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:01:20 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:00:58 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:00:20 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:00:18 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 10:06:11 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-08-02 10:01:35 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-02 10:02:34 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-02 10:02:15 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-02 10:02:40 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-02 10:04:20 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-02 10:07:02 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-02 10:00:18 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:02:43 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:02:03 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:01:20 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 09:04:19 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:08:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:03:46 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:15:38 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:00:20 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:03:15 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:05:23 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:03:11 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:07:44 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:01:23 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:02:30 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:15:08 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:00:58 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:10:28 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:02:14 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:05:00 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:03:38 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-08-02 10:03:47 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-08-02 09:01:47 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-08-02 10:10:44 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-08-02 10:01:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-08-02 10:04:51 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.029 |  |
| 2026-08-02 10:04:13 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-08-02 10:08:07 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.038 |  |
| 2026-08-02 10:05:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.088 |  |
| 2026-08-02 10:02:45 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.103 |  |
| 2026-08-02 10:22:17 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)