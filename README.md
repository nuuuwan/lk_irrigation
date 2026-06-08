# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_20:15:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,082 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 20:15:46 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:14:20 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.017 |  |
| 2026-06-08 20:13:45 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:11:32 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.037 |  |
| 2026-06-08 20:11:24 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -0.802 |  |
| 2026-06-08 20:10:01 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.019 |  |
| 2026-06-08 20:10:00 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:08:36 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-06-08 20:07:56 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:06:58 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.031 |  |
| 2026-06-08 20:06:07 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:05:43 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-08 20:05:31 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.025 |  |
| 2026-06-08 20:05:26 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-08 20:05:18 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.029 |  |
| 2026-06-08 20:04:54 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-08 20:04:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:04:10 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-08 20:04:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-06-08 20:03:56 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-08 20:03:52 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 20:03:42 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:03:40 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 20:03:11 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 20:02:55 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:02:46 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-06-08 20:02:21 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:02:19 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-08 20:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:02:14 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 20:02:00 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:01:30 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2026-06-08 20:01:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:59:58 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 20:05:26 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-06-08 20:03:56 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-06-08 20:05:43 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-08 20:04:10 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-08 19:28:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-08 20:02:19 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-08 20:03:11 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-08 20:03:40 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 20:03:52 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 20:02:14 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 20:03:42 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:10:00 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:02:21 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:02:00 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:07:56 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-08 19:59:58 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:01:19 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:06:07 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:04:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:15:46 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:13:45 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:02:55 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 20:04:54 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-08 20:14:20 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.017 |  |
| 2026-06-08 20:10:01 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.019 |  |
| 2026-06-08 20:08:36 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-06-08 20:02:46 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-06-08 20:05:31 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.025 |  |
| 2026-06-08 20:05:18 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | -0.029 |  |
| 2026-06-08 20:01:30 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2026-06-08 20:04:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-06-08 20:06:58 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.031 |  |
| 2026-06-08 20:11:32 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.037 |  |
| 2026-06-08 19:00:57 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.040 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-08 20:11:24 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -0.802 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)