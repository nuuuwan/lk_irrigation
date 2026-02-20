# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_01:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 01:13:33 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 01:10:28 | Padiyathalawa (Maduru Oya) | 1.99 | 🟢 Normal | -0.034 |  |
| 2026-02-21 01:07:32 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 01:06:45 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:05:43 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 01:05:38 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:05:25 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 01:05:07 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:05:05 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-21 01:03:56 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-21 01:03:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.096 |  |
| 2026-02-21 01:03:43 | Manampitiya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.067 |  |
| 2026-02-21 01:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-21 01:03:36 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-02-21 01:03:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:59 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:37 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:29 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 01:02:27 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 01:02:26 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:21 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-21 01:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:11 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:55 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:09 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:40 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:39 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:09 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:08 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:59:34 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:34:50 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:19:08 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 00:10:31 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-02-21 00:06:14 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-02-21 01:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-21 01:02:14 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-21 01:03:56 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-21 01:05:25 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 01:05:05 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-21 01:02:27 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 01:02:29 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 01:07:32 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 01:05:43 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 01:13:33 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 01:02:26 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:39 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:11 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:40 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:55 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:37 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:08 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:05:38 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:06:45 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:21 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:09 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:03:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:09 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:09:06 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:05:07 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:02:59 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:02:34 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-21 00:19:08 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-02-21 01:03:36 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-02-21 01:10:28 | Padiyathalawa (Maduru Oya) | 1.99 | 🟢 Normal | -0.034 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-21 01:03:43 | Manampitiya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.067 |  |
| 2026-02-21 01:03:44 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)