# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_11:59:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,495 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 11:59:50 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-01 11:26:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.015 |  |
| 2026-02-01 11:17:37 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:17:00 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:15:40 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-01 11:09:39 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:09:04 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-01 11:08:57 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 11:08:39 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 11:08:24 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 11:06:34 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:06:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:06:26 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:05:45 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-01 11:05:41 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:04:53 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-01 11:04:35 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 11:04:28 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.065 |  |
| 2026-02-01 11:04:26 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:04:03 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.029 |  |
| 2026-02-01 11:03:30 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-02-01 11:03:22 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-01 11:03:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 11:03:06 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-02-01 11:03:06 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:03:01 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 11:01:55 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-02-01 11:01:53 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-02-01 11:03:16 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 11:01:45 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-01 11:04:53 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-01 11:01:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-01 11:01:57 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-01 11:08:24 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 11:59:50 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-01 11:08:57 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 11:09:04 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-01 11:03:01 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 11:08:39 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 11:02:55 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 11:04:35 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 11:01:18 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:01:04 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:17:37 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:03:06 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:06:26 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:04:26 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:06:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:09:39 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:06:34 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:05:41 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 11:02:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-01 11:05:45 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-01 11:02:43 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-01 11:01:11 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-01 11:00:41 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-02-01 11:02:55 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-02-01 11:26:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.015 |  |
| 2026-02-01 11:03:30 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-02-01 11:03:22 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-01 11:03:06 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-02-01 11:02:21 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.021 |  |
| 2026-02-01 11:04:03 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.029 |  |
| 2026-02-01 11:04:28 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)