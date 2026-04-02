# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_11:17:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,072 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 11:17:37 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-02 11:16:10 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-02 11:13:20 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-02 11:13:06 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:09:40 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:08:40 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.091 |  |
| 2026-04-02 11:07:41 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 11:07:14 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:07:10 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 11:06:36 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.143 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 11:02:44 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-04-02 11:06:36 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-04-02 11:13:20 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-02 11:03:40 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-02 11:07:41 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 11:02:27 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 11:01:54 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 11:03:01 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 11:07:10 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 11:04:39 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 10:00:50 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:04:50 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:01:30 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:13:06 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:03:34 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:05:00 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:03:03 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:04:49 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:01:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:03:29 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:09:40 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:07:14 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:04:41 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:00:50 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:04:32 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:02:16 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 11:01:45 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | -0.006 |  |
| 2026-04-02 11:16:10 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-04-02 11:02:58 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-02 11:02:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-02 11:03:29 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-04-02 11:17:37 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-04-02 11:03:29 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.031 |  |
| 2026-04-02 11:00:41 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.041 |  |
| 2026-04-02 11:08:40 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.091 |  |
| 2026-04-02 11:00:47 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.198 |  |
| 2026-04-02 11:00:49 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | -0.468 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)