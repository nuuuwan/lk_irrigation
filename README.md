# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_01:39:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,362 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 01:39:47 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.076 |  |
| 2026-06-08 01:31:17 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-08 01:19:07 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | -252.000 |  |
| 2026-06-08 01:19:06 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | -252.000 |  |
| 2026-06-08 01:15:25 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:14:05 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:13:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:07:56 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-08 01:07:56 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.071 |  |
| 2026-06-08 01:06:44 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:06:01 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:05:44 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:05:26 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 01:05:17 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:05:11 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:04:51 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 01:04:46 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:04:23 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-06-08 01:03:27 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-06-08 01:03:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:03:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:03:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.070 |  |
| 2026-06-08 01:02:59 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:02:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:02:49 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:02:10 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-08 01:02:03 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:01:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:37 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:27 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-06-08 01:01:22 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:09 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:01:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 01:02:10 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-08 01:07:56 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-08 01:05:26 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 00:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 01:04:51 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 01:31:17 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-08 01:05:44 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:27 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:03:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:02:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:55 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:05:17 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:02:59 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:04:46 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:37 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:03:27 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:06:01 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:01:22 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:06:44 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:13:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-08 00:06:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:15:25 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:02:03 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:02:49 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:01:09 | Ellagawa (Kalu Ganga) | 7.77 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:04:47 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:05:11 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-08 01:04:23 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-06-08 01:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-06-08 01:03:27 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-06-08 01:03:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.070 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-08 01:07:56 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.071 |  |
| 2026-06-08 01:39:47 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.076 |  |
| 2026-06-08 01:19:07 | Magura (Kalu Ganga) | 2.97 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)