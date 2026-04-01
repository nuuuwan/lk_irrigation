# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_02:14:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,726 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 02:14:32 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:12:38 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-02 02:12:06 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:11:58 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:10:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-02 02:09:25 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-02 02:07:52 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:06:36 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:05:58 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-04-02 02:05:51 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:05:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:05:21 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:04:47 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:04:36 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-02 02:04:27 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-02 02:03:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:22 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:14 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-02 02:03:06 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:01 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.040 |  |
| 2026-04-02 02:02:51 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:11 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:10 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:01:32 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 02:01:29 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 01:59:45 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-02 01:55:47 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-02 01:50:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-02 01:32:08 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 01:01:48 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-04-02 02:09:25 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-02 02:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-02 02:10:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-02 01:59:45 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-02 02:04:27 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-02 00:01:31 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 02:01:32 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 02:04:36 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-02 02:05:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:14:32 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:51 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:04:47 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:05:21 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:11 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:02:10 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-02 00:07:59 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:01:29 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:12:06 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:05:51 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 01:02:27 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:06:36 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:22 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 01:04:22 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:11:58 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-02 01:04:52 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:03:06 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:07:52 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:05:58 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-04-01 18:05:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-02 02:12:38 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-04-02 01:00:59 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-01 18:01:16 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.031 |  |
| 2026-04-02 00:04:28 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.031 |  |
| 2026-04-02 02:03:01 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)