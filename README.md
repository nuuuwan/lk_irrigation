# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_23:20:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,563 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 23:20:35 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:11:04 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 23:08:57 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 23:08:36 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-02-20 23:08:20 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-02-20 23:07:44 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-02-20 23:07:16 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:06:01 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:05:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:05:04 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:04:45 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 23:04:36 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:03:40 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-02-20 23:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-20 23:02:48 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:33 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-20 23:02:29 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:29 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:05 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:00 | Padiyathalawa (Maduru Oya) | 1.91 | 🟢 Normal | -0.029 |  |
| 2026-02-20 23:01:57 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:01:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:01:23 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-20 23:01:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-20 23:01:09 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:00:59 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:00:45 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:00:42 | Manampitiya (Mahaweli Ganga) | 3.08 | 🟡 Alert | -0.010 |  |
| 2026-02-20 23:00:36 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:00:10 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 23:00:42 | Manampitiya (Mahaweli Ganga) | 3.08 | 🟡 Alert | -0.010 |  |
| 2026-02-20 23:08:20 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-02-20 23:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-20 23:01:10 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-20 23:04:45 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 22:04:37 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 23:11:04 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 22:03:50 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 23:08:57 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 22:20:49 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:00:45 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:20:35 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:05 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:07:16 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:00:36 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:06:01 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:01:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:01:57 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:00:59 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:04:36 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:05:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:05:04 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 22:23:09 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:48 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:29 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:01:09 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:02:29 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-20 23:08:36 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-02-20 23:07:44 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-02-20 23:01:23 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-02-20 23:02:33 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-20 23:00:10 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-02-20 23:03:40 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-02-20 23:02:00 | Padiyathalawa (Maduru Oya) | 1.91 | 🟢 Normal | -0.029 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-20 22:06:23 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.059 |  |
| 2026-02-20 22:09:04 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)