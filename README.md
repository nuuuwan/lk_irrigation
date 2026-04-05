# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_03:11:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,356 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 03:11:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:11:20 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-06 03:11:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.017 |  |
| 2026-04-06 03:08:19 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.049 |  |
| 2026-04-06 03:08:03 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:07:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:05:56 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-06 03:05:49 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-04-06 03:05:45 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-04-06 03:05:15 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-04-06 03:05:04 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-04-06 03:04:56 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-06 03:04:49 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-04-06 03:04:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:04:02 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:57 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:51 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:49 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:49 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:32 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:50 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:45 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:30 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:28 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:11 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:03 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:01:40 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 03:01:29 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:01:16 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.005 |  |
| 2026-04-06 03:01:04 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:00:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:43:45 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.049 |  |
| 2026-04-06 02:43:44 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.049 |  |
| 2026-04-06 02:43:11 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:40:58 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.012 |  |
| 2026-04-06 02:34:54 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:25:57 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:25:24 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 03:05:56 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-06 02:04:47 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-06 01:06:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-06 02:07:58 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-06 03:11:20 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-06 03:01:40 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 03:02:45 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:01:04 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:00:58 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:07:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:03 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:01:29 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:11:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:08:03 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:57 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:49 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:11 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.000 |  |
| 2026-04-06 00:01:54 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:50 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:30 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:51 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:02:28 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:03:32 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 02:25:57 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:04:25 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 03:05:15 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.005 |  |
| 2026-04-06 03:01:16 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.005 |  |
| 2026-04-06 03:05:49 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.009 |  |
| 2026-04-06 03:04:56 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-06 02:40:58 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.012 |  |
| 2026-04-06 03:04:49 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-04-06 03:05:04 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-04-06 03:11:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.017 |  |
| 2026-04-06 03:05:45 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-04-06 03:08:19 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.049 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-06 02:00:49 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)