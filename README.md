# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_03:41:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 03:41:48 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:17:23 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.004 |  |
| 2026-02-27 03:13:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:12:45 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:12:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.015 |  |
| 2026-02-27 03:09:57 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:08:42 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-27 03:08:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:07:43 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:07:30 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:06:27 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-02-27 03:05:55 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:05:47 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-27 03:04:57 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-27 03:04:05 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.159 |  |
| 2026-02-27 03:03:45 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:03:41 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:03:40 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:03:27 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:03:22 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.204 |  |
| 2026-02-27 03:02:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.005 |  |
| 2026-02-27 03:02:29 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.300 |  |
| 2026-02-27 03:02:25 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:02:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:02:11 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:01:52 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:01:49 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.005 |  |
| 2026-02-27 03:01:39 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-27 03:01:28 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.051 |  |
| 2026-02-27 03:01:20 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:01:19 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 18:01:32 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-27 03:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-27 02:17:50 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-27 03:05:47 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-27 02:05:17 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-27 03:02:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.005 |  |
| 2026-02-27 03:01:49 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.005 |  |
| 2026-02-27 03:17:23 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.004 |  |
| 2026-02-27 03:03:41 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:01:20 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:02:25 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:41:48 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:05:55 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:03:27 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:13:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-27 02:01:04 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:07:43 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:03:45 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:08:34 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:01:52 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:09:57 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:04:57 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:02:11 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:03:40 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:01:19 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-26 18:02:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-27 01:03:18 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:07:30 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:02:18 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 03:08:42 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-27 03:01:39 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-27 03:12:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.015 |  |
| 2026-02-27 03:06:27 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.019 |  |
| 2026-02-27 03:01:28 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.051 |  |
| 2026-02-27 03:04:05 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.159 |  |
| 2026-02-27 02:00:18 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.162 |  |
| 2026-02-27 03:03:22 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.204 |  |
| 2026-02-27 03:02:29 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)