# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_04:12:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,134 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 04:12:16 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-27 04:12:02 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:12:00 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:11:59 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:11:58 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:11:57 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:11:55 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:06:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-02-27 04:05:57 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 04:05:46 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:05:45 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:05:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:05:00 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.023 |  |
| 2026-02-27 04:04:55 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:04:36 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -36.000 |  |
| 2026-02-27 04:04:34 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -36.000 |  |
| 2026-02-27 04:04:33 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -36.000 |  |
| 2026-02-27 04:04:25 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:03:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-02-27 04:03:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 04:03:36 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:03:21 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.878 |  |
| 2026-02-27 04:03:10 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-02-27 04:03:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:40 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.878 |  |
| 2026-02-27 04:02:37 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:36 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:35 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-02-27 04:02:34 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.005 |  |
| 2026-02-27 04:02:30 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:29 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | -0.535 |  |
| 2026-02-27 04:02:25 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.185 |  |
| 2026-02-27 04:02:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:19 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:19 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.878 |  |
| 2026-02-27 04:02:06 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-02-27 04:01:48 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:01:14 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:00:57 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-27 04:00:36 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | -0.168 |  |
| 2026-02-27 04:00:13 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-27 03:41:48 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 04:00:13 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-27 03:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-27 04:05:57 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 04:03:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-27 04:12:16 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-27 03:01:49 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.005 |  |
| 2026-02-27 03:17:23 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.004 |  |
| 2026-02-27 04:02:21 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:36 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:19 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:03:36 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:12:02 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:05:46 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:01:14 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:03:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:04:57 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:37 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:05:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:04:55 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:01:19 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:04:25 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:02:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 04:02:34 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.005 |  |
| 2026-02-27 04:00:57 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-27 04:02:06 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-02-27 04:03:50 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-02-27 04:03:10 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-02-27 04:05:00 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.023 |  |
| 2026-02-27 04:02:35 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-02-27 04:06:32 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-02-27 04:00:36 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | -0.168 |  |
| 2026-02-27 04:02:25 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.185 |  |
| 2026-02-27 04:02:29 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | -0.535 |  |
| 2026-02-27 04:03:21 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.878 |  |
| 2026-02-27 04:04:36 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)