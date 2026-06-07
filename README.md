# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_00:39:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,327 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 00:39:06 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 9.971 | 🔺 Rising |
| 2026-06-08 00:25:12 | Panadugama (Nilwala Ganga) | 0.95 | 🟢 Normal | 9.971 | 🔺 Rising |
| 2026-06-08 00:12:17 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-08 00:08:55 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.036 |  |
| 2026-06-08 00:07:55 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:07:46 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-08 00:07:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:06:48 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:06:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:06:29 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 00:05:44 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-08 00:05:28 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-06-08 00:04:47 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:04:33 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 00:04:30 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:04:26 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.099 |  |
| 2026-06-08 00:03:57 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 00:03:37 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.043 |  |
| 2026-06-08 00:03:17 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-06-08 00:02:45 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.032 |  |
| 2026-06-08 00:02:39 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-08 00:02:35 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:02:30 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:02:17 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:50 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:38 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:31 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:22 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:01:15 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:00:31 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 00:39:06 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 9.971 | 🔺 Rising |
| 2026-06-08 00:07:46 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-08 00:12:17 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-08 00:02:39 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-08 00:05:44 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 23:08:13 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-08 00:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 00:04:33 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 00:06:29 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 00:07:55 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:00:31 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:38 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:02:35 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:31 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:50 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:07:17 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:04:30 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:26:42 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:02:30 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:05:28 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:02:17 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:06:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:06:48 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:01:15 | Nawalapitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:04:47 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:01:22 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:03:57 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:02:45 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.032 |  |
| 2026-06-08 00:08:55 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.036 |  |
| 2026-06-08 00:03:17 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-06-08 00:03:37 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.043 |  |
| 2026-06-08 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-08 00:04:26 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.099 |  |
| 2026-06-07 23:05:51 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)