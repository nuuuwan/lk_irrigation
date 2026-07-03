# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--03_23:22:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 23:22:59 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-03 23:20:31 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.077 |  |
| 2026-07-03 23:20:05 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:19:50 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:14:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:11:22 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 23:11:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:10:08 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-03 23:08:59 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:08:45 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:07:02 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.028 |  |
| 2026-07-03 23:06:26 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:06:17 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-03 23:05:32 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-03 23:05:17 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:05:17 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-03 23:05:11 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 23:04:28 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:03:47 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-03 23:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-07-03 23:03:23 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:02:50 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-07-03 23:02:50 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:02:47 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:02:37 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-07-03 23:02:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:02:15 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 23:02:10 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:01:45 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.022 |  |
| 2026-07-03 23:01:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:01:38 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:01:36 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:01:23 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.092 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-03 23:02:37 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-07-03 23:02:50 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-07-03 23:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-07-03 23:05:32 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-03 23:10:08 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-03 22:01:32 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-03 23:02:15 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 23:05:11 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-03 23:11:22 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-03 23:22:59 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-03 23:02:47 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:01:38 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:01:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-03 22:02:10 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:04:28 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:01:36 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:02:50 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:20:05 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:08:59 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:14:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:05:17 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:03:23 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-03 22:02:30 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:19:50 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:11:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:02:10 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:06:26 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:47:16 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-03 23:02:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-03 18:09:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.005 |  |
| 2026-07-03 23:05:17 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-07-03 23:03:47 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-07-03 23:06:17 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-07-03 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-07-03 23:01:45 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.022 |  |
| 2026-07-03 22:03:24 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.024 |  |
| 2026-07-03 23:07:02 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.028 |  |
| 2026-07-03 23:20:31 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.077 |  |
| 2026-07-03 23:01:23 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)