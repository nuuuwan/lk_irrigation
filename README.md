# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_04:09:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,685 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 04:09:13 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-03-15 04:08:38 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:07:07 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-15 04:06:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:05:26 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 04:05:11 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 04:04:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:04:36 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.018 |  |
| 2026-03-15 04:04:09 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-15 04:04:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:03:17 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.033 |  |
| 2026-03-15 04:03:02 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.052 |  |
| 2026-03-15 04:02:58 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.081 |  |
| 2026-03-15 04:02:57 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.114 |  |
| 2026-03-15 04:02:38 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:02:22 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:02:21 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-03-15 04:02:12 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 04:02:11 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:37 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:14 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:06 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-03-15 04:00:30 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.040 |  |
| 2026-03-15 04:00:28 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:00:27 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.022 |  |
| 2026-03-15 03:59:58 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:56:37 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:56:15 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:49:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 9.134 | 🔺 Rising |
| 2026-03-15 03:48:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 9.134 | 🔺 Rising |
| 2026-03-15 03:31:01 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.018 |  |
| 2026-03-15 03:21:52 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:21:51 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:21:49 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:19:50 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:17:41 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-15 03:17:20 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 03:49:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 9.134 | 🔺 Rising |
| 2026-03-15 04:07:07 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-15 04:02:12 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 04:05:11 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 01:16:37 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-15 04:05:26 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 04:04:45 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:02:38 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:02:11 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:37 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:21:52 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:01:35 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:04:08 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:00:28 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:03:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:02:22 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:06:09 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:08:38 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 04:01:14 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:14:50 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 04:04:09 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-15 04:09:13 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-03-15 04:01:06 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-03-15 04:04:36 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.018 |  |
| 2026-03-15 04:00:27 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.022 |  |
| 2026-03-15 04:02:21 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-03-15 04:03:17 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.033 |  |
| 2026-03-15 04:00:30 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.040 |  |
| 2026-03-15 03:04:11 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-03-15 04:03:02 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.052 |  |
| 2026-03-15 04:02:58 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.081 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |
| 2026-03-15 04:02:57 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.114 |  |
| 2026-03-15 03:05:24 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -54.000 |  |
| 2026-03-15 03:06:46 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)