# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_03:30:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,359 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 03:30:10 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-04-15 03:15:42 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.008 |  |
| 2026-04-15 03:11:35 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-15 03:08:57 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 03:07:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-15 03:06:04 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:05:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.103 |  |
| 2026-04-15 03:05:02 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:04:55 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-04-15 03:04:33 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-15 03:04:19 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-15 03:04:05 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.087 |  |
| 2026-04-15 03:04:00 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:03:39 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:03:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:02:56 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-04-15 03:02:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-04-15 03:02:40 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:02:39 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:02:36 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.195 |  |
| 2026-04-15 03:02:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:01:56 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:01:41 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 03:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:01:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:01:16 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:01:14 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 03:00:43 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.011 |  |
| 2026-04-15 03:00:41 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 02:13:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 4.065 | 🔺 Rising |
| 2026-04-15 03:30:10 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-04-15 03:04:33 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-15 03:04:19 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-15 03:01:14 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 03:01:41 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 03:08:57 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 03:11:35 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-15 00:19:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:02:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:25:30 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:06:36 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:01:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:02:39 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:04:00 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:02:40 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:03:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:03:30 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:01:15 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:00:41 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:04:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 03:01:56 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 02:15:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-04-15 03:15:42 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.008 |  |
| 2026-04-15 03:07:23 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-04-15 03:06:04 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:05:02 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:03:39 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:01:19 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-04-15 03:00:43 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.011 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-15 03:02:56 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-04-15 03:04:55 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-15 03:02:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-15 03:04:05 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.087 |  |
| 2026-04-15 03:05:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.103 |  |
| 2026-04-15 03:02:36 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)