# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_01:27:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 01:27:23 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.007 |  |
| 2026-04-03 01:23:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-04-03 01:22:51 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-04-03 01:19:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-03 01:16:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-04-03 01:13:16 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-03 01:10:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-03 01:10:19 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.018 |  |
| 2026-04-03 01:10:07 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-03 01:06:26 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:06:24 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-03 01:06:00 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-03 01:05:37 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:05:32 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-03 01:05:05 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:04:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:03:24 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.311 |  |
| 2026-04-03 01:03:18 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:02:44 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:02:40 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-03 01:02:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:02:31 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:02:08 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.031 |  |
| 2026-04-03 01:01:41 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:01:31 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:01:24 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:01:06 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 01:16:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-04-03 01:10:07 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-03 01:06:00 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-03 01:19:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-03 01:05:32 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-03 01:01:24 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:01:41 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:04:09 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:05:37 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 01:13:16 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-03 01:06:26 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:02:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 00:04:16 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 00:02:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:01:06 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:05:05 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-02 23:06:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-03 00:01:20 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 23:01:58 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:02:44 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:02:31 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:01:31 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:03:18 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 01:27:23 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.007 |  |
| 2026-04-03 01:23:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-04-03 01:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-03 01:02:40 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-03 01:06:24 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-04-02 23:04:35 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-04-03 01:10:19 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.018 |  |
| 2026-04-03 01:10:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-04-03 00:02:54 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-04-03 01:22:51 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-04-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-04-03 01:02:08 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.031 |  |
| 2026-04-03 01:00:10 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.139 |  |
| 2026-04-03 01:03:24 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.311 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)