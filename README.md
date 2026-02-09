# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_06:19:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,109 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 06:19:11 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-02-09 06:14:12 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.008 |  |
| 2026-02-09 06:13:07 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-02-09 06:10:59 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:10:47 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-02-09 06:10:41 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:09:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:09:31 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-02-09 06:09:08 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 06:07:56 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 06:07:28 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:07:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.256 |  |
| 2026-02-09 06:05:15 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-09 06:05:13 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-09 06:05:04 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:04:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:03:51 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:03:24 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:03:21 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.208 |  |
| 2026-02-09 06:03:19 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-09 06:03:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-02-09 06:02:56 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-09 06:02:53 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:02:35 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-09 06:02:17 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 06:02:13 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-09 06:02:04 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-02-09 06:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:01:42 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:01:36 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:01:33 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:01:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 06:01:20 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -72.000 |  |
| 2026-02-09 06:01:19 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -72.000 |  |
| 2026-02-09 06:01:18 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -72.000 |  |
| 2026-02-09 06:01:16 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -72.000 |  |
| 2026-02-09 06:01:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:00:55 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-09 06:00:47 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-02-09 05:54:32 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:37:23 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 06:05:15 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-09 06:19:11 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-02-09 06:02:13 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-09 06:01:32 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 06:00:55 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-09 06:05:13 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-09 06:02:17 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 06:09:08 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 06:07:56 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 06:01:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:03:21 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:02:53 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:01:42 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:03:51 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:07:28 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:10:41 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:05:04 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:04:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:10:59 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:09:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:01:33 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:03:24 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 06:14:12 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.008 |  |
| 2026-02-09 06:13:07 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-02-09 06:10:47 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 06:02:56 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-09 06:02:35 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-09 06:02:04 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-02-09 05:01:30 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-02-09 06:09:31 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-02-09 06:03:19 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-09 06:00:47 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-02-09 06:03:09 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-02-09 06:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.208 |  |
| 2026-02-09 06:07:20 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.256 |  |
| 2026-02-09 06:01:20 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)