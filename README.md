# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_07:54:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,311 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 07:54:50 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 05:07:06 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-02 05:06:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 2.070 | 🔺 Rising |
| 2026-01-02 05:01:27 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-01-02 05:12:58 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-01-02 05:01:33 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-02 05:14:39 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-02 05:01:19 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-02 05:18:06 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-02 05:22:02 | Horowpothana (Yan Oya) | 3.87 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-02 05:03:33 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.005 |  |
| 2026-01-02 05:05:55 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:06:54 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:02:35 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:11:35 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:05:21 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 07:54:50 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:12:37 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:01:38 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:08:54 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:01:02 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.010 |  |
| 2026-01-02 05:00:48 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-01-02 04:47:54 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.013 |  |
| 2026-01-02 05:12:35 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.018 |  |
| 2026-01-02 04:03:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-02 05:11:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-02 05:03:44 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.041 |  |
| 2026-01-02 05:06:28 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.046 |  |
| 2026-01-02 05:08:29 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.088 |  |
| 2026-01-02 05:09:55 | Siyambalanduwa (Heda Oya) | 1.86 | 🟢 Normal | -0.098 |  |
| 2026-01-02 05:00:14 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.100 |  |
| 2026-01-02 05:02:56 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | -0.103 |  |
| 2026-01-02 05:02:24 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.142 |  |
| 2026-01-02 05:05:44 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | -0.186 |  |
| 2026-01-02 04:03:57 | Padiyathalawa (Maduru Oya) | 3.63 | 🟢 Normal | -0.380 |  |
| 2026-01-02 05:25:10 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -1.286 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)