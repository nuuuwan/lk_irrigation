# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_00:04:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,312 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 00:04:07 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-03 00:03:57 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-03 00:03:55 | Nawalapitiya (Mahaweli Ganga) | 5.58 | 🟠 Minor Flood | 1.538 | 🔺 Rising |
| 2026-08-03 00:03:27 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-03 00:03:24 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:03:18 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-03 00:03:11 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-08-03 00:03:02 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:55 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:51 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-03 00:02:21 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:10 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-03 00:02:06 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-08-03 00:02:02 | Kithulgala (Kelani Ganga) | 4.58 | 🟠 Minor Flood | 1.959 | 🔺 Rising |
| 2026-08-03 00:01:50 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:01:18 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:01:14 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:01:07 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-08-03 00:00:42 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:00:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:41:32 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-08-02 23:16:51 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.101 |  |
| 2026-08-02 23:15:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.017 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 00:02:02 | Kithulgala (Kelani Ganga) | 4.58 | 🟠 Minor Flood | 1.959 | 🔺 Rising |
| 2026-08-03 00:03:55 | Nawalapitiya (Mahaweli Ganga) | 5.58 | 🟠 Minor Flood | 1.538 | 🔺 Rising |
| 2026-08-02 23:41:32 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-08-02 23:06:42 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-08-02 23:04:39 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-08-03 00:02:06 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-08-02 23:08:59 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-02 23:06:41 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-08-03 00:03:57 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-03 00:02:51 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-03 00:03:18 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-03 00:02:10 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-03 00:04:07 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-03 00:03:27 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-02 23:15:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-02 23:06:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-02 23:04:49 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 00:01:50 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:01:14 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:00:42 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:01:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:00:33 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:03:49 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:21 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:06:41 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:03:24 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:02:55 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:03:32 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:03:02 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:00:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-02 18:00:59 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:01:18 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-02 23:12:43 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 00:03:11 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-08-03 00:01:07 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-08-02 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-02 23:02:16 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-08-02 23:13:02 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.046 |  |
| 2026-08-02 23:16:51 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)