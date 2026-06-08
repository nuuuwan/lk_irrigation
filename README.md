# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_19:21:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 19:21:28 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.015 |  |
| 2026-06-08 19:17:06 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.017 |  |
| 2026-06-08 19:09:48 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.036 |  |
| 2026-06-08 19:08:33 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-08 19:08:11 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.021 |  |
| 2026-06-08 19:07:40 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.029 |  |
| 2026-06-08 19:06:38 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.067 |  |
| 2026-06-08 19:06:05 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:05:56 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:05:46 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-08 19:05:44 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-08 19:05:42 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-08 19:05:36 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:05:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:05:16 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 19:04:33 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:04:32 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:04:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:04:09 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:03:46 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-08 19:03:43 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:03:40 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.022 |  |
| 2026-06-08 19:03:28 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-08 19:03:24 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 19:03:09 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:43 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:22 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-08 19:02:19 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:11 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-06-08 19:01:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:00:57 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.040 |  |
| 2026-06-08 19:00:46 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:44:37 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.125 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 19:08:33 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-06-08 19:05:42 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-08 19:05:44 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-08 19:03:46 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-08 19:05:46 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-08 19:03:24 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 19:03:28 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-08 19:05:16 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 19:05:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:01:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:03:43 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:03:09 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:28 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:06:05 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:43 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:04:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:05:36 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:00:46 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:04:09 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:04:32 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:04:33 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:05:56 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:19 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:02:22 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-08 18:06:08 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.012 |  |
| 2026-06-08 19:21:28 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.015 |  |
| 2026-06-08 19:17:06 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.017 |  |
| 2026-06-08 19:02:11 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-06-08 19:08:11 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | -0.021 |  |
| 2026-06-08 19:03:40 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.022 |  |
| 2026-06-08 19:07:40 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.029 |  |
| 2026-06-08 19:09:48 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | -0.036 |  |
| 2026-06-08 19:00:57 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.040 |  |
| 2026-06-08 18:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | -0.040 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-08 19:06:38 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)