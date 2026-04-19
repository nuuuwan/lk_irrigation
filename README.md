# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_04:10:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,840 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 04:10:44 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-20 04:10:42 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-20 04:08:32 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.357 |  |
| 2026-04-20 04:07:55 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:07:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-20 04:07:26 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-20 04:05:57 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:05:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:05:50 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.063 |  |
| 2026-04-20 04:05:30 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 04:05:10 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:04:35 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:04:23 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-20 04:03:44 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-20 04:02:58 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-04-20 04:02:58 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:02:36 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-20 04:02:11 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 04:02:11 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 04:02:06 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.202 |  |
| 2026-04-20 04:02:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:01:57 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:01:36 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-20 04:01:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:01:21 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-04-20 04:01:13 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:00:56 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:00:53 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 04:00:48 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-04-20 04:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.084 |  |
| 2026-04-20 03:37:09 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:31:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.084 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 04:10:44 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-20 03:03:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-04-20 04:03:44 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-04-20 04:07:26 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-20 04:02:36 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 04:05:30 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 04:02:11 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 04:07:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-20 04:02:11 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 04:00:53 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:02:51 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-20 04:01:57 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:05:57 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:04:35 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:00:56 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:18 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:07:55 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:02:06 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:05:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:01:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:02:58 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 00:02:42 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:05:10 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:01:13 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:12:48 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:04:23 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-20 04:01:36 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-04-20 04:00:48 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-04-20 03:02:54 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-04-20 04:01:21 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-04-20 04:02:58 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-04-20 04:05:50 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.063 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-20 04:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.084 |  |
| 2026-04-20 04:02:06 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.202 |  |
| 2026-04-20 04:08:32 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)