# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_04:44:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,873 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 04:44:46 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.015 |  |
| 2026-04-29 04:40:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.039 |  |
| 2026-04-29 04:13:51 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:09:57 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -1.800 |  |
| 2026-04-29 04:09:37 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -1.800 |  |
| 2026-04-29 04:09:15 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -1.800 |  |
| 2026-04-29 04:07:47 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-04-29 04:07:25 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-29 04:06:39 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:05:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-29 04:05:11 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:05:04 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-29 04:04:45 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:04:41 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-04-29 04:04:20 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.015 |  |
| 2026-04-29 04:04:11 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.024 |  |
| 2026-04-29 04:03:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.073 |  |
| 2026-04-29 04:03:43 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-04-29 04:03:24 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-04-29 04:03:12 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-04-29 04:03:06 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:02:50 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:02:49 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:02:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:02:15 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-29 04:02:07 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 04:01:59 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:01:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.003 |  |
| 2026-04-29 04:01:42 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:01:01 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-04-29 04:00:57 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-04-29 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.081 |  |
| 2026-04-29 04:00:29 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.083 |  |
| 2026-04-29 04:00:26 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-04-29 04:00:14 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 04:05:04 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-29 04:02:07 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-29 03:00:57 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 04:07:25 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-29 04:02:15 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 03:04:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:13:51 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:02:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:04:45 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:02:50 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:05:11 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:00:14 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:03:06 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:06:39 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:01:59 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-29 03:06:17 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 04:01:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.003 |  |
| 2026-04-29 04:07:47 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2026-04-29 00:03:00 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 04:00:26 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-04-29 03:00:17 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-29 04:05:49 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-29 04:04:41 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-04-29 04:44:46 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.015 |  |
| 2026-04-29 04:03:43 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-04-29 04:01:01 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | -0.020 |  |
| 2026-04-29 04:00:57 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-04-29 04:03:24 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-04-29 04:04:11 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.024 |  |
| 2026-04-29 04:03:12 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-04-29 04:40:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.039 |  |
| 2026-04-29 04:03:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.073 |  |
| 2026-04-29 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.081 |  |
| 2026-04-29 04:00:29 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.083 |  |
| 2026-04-29 02:08:44 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-04-29 04:09:57 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)