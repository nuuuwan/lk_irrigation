# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_00:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,642 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 00:03:16 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-04-02 00:03:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 00:03:09 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:37 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:31 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:23 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:00 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-02 00:01:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-04-02 00:01:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:47 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:31 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 00:01:23 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:21 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:10 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:56:54 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:55:54 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:32:40 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:18:54 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:18:10 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-01 23:14:28 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:11:58 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 00:01:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-04-01 23:01:06 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-01 23:07:34 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-02 00:02:00 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-01 23:07:12 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-01 23:02:18 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-01 23:03:09 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 00:01:31 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 00:03:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 23:55:54 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:03:09 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-01 21:02:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:10 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:18:54 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:02:10 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:14:28 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:01:17 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:03:45 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:23 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:47 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:02:28 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:23 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:01:21 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:37 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:31 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:02:21 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:03:26 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 22:10:40 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:05:54 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:03:29 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 23:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:05:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-01 23:01:55 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-04-02 00:03:16 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-04-01 18:01:16 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.031 |  |
| 2026-04-01 23:05:26 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-04-01 21:27:44 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)