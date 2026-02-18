# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_05:28:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 05:28:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.045 |  |
| 2026-02-18 05:15:59 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:10:43 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-02-18 05:10:36 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:08:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:06:15 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 05:05:58 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:05:32 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-18 05:05:25 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:05:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:05:00 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-18 05:04:55 | Rathnapura (Kalu Ganga) | 0.30 | 🟢 Normal | -396.000 |  |
| 2026-02-18 05:04:54 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:04:54 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -396.000 |  |
| 2026-02-18 05:04:29 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:04:17 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:04:14 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.114 |  |
| 2026-02-18 05:04:07 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.023 |  |
| 2026-02-18 05:03:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 05:03:21 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.016 |  |
| 2026-02-18 05:02:58 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.032 |  |
| 2026-02-18 05:02:38 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-18 05:02:36 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-18 05:02:01 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:01:56 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 05:01:53 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-18 05:01:39 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:01:36 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:01:31 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.304 |  |
| 2026-02-18 05:01:13 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.020 |  |
| 2026-02-18 05:01:10 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-18 05:00:50 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:00:50 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.025 |  |
| 2026-02-18 04:44:29 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.032 |  |
| 2026-02-18 04:40:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 05:05:32 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-02-18 05:05:00 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-17 18:03:50 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-18 05:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-18 04:28:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-18 05:01:56 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 05:03:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 05:06:15 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-18 05:00:50 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:00:50 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:01:39 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:05:58 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:02:36 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:10:36 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:04:17 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:08:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:02:01 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:15:59 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:05:25 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:49 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:05:04 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:27 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:04:54 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:04:29 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:09:28 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 05:02:38 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-18 05:01:10 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-18 05:01:53 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-18 05:03:21 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.016 |  |
| 2026-02-18 05:01:13 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.020 |  |
| 2026-02-18 05:10:43 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-02-18 05:04:07 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.023 |  |
| 2026-02-18 05:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.025 |  |
| 2026-02-18 05:02:58 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.032 |  |
| 2026-02-18 05:28:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.045 |  |
| 2026-02-18 05:04:14 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.114 |  |
| 2026-02-18 05:01:31 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.304 |  |
| 2026-02-18 05:04:55 | Rathnapura (Kalu Ganga) | 0.30 | 🟢 Normal | -396.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)