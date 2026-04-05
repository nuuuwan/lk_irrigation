# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_13:19:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 13:19:37 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:17:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.032 |  |
| 2026-04-05 13:16:48 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:16:32 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.069 |  |
| 2026-04-05 13:14:15 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:13:26 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:12:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-05 13:11:29 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:11:19 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-04-05 13:09:30 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-04-05 13:09:25 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-04-05 13:06:06 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-05 13:05:41 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:49 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:07 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:03 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.074 |  |
| 2026-04-05 13:03:51 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.013 |  |
| 2026-04-05 13:03:48 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:03:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:27 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-05 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-05 13:03:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:03:08 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.253 |  |
| 2026-04-05 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 13:02:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:37 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 13:02:26 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:22 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:07 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:50 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:38 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:36 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:36 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:01:31 | Thanthirimale (Malwathu Oya) | 2.88 | 🟢 Normal | -0.060 |  |
| 2026-04-05 13:01:13 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.148 |  |
| 2026-04-05 13:00:56 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 13:03:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-04-05 13:06:06 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-04-05 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-05 13:12:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-05 13:02:37 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 13:02:22 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:50 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:13:26 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:36 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:07 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:05:41 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:14:15 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:27 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:38 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:16:48 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:02:26 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 12:00:56 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:01:44 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:19:37 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:11:29 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:03:43 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:04:07 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-05 13:11:19 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-04-05 13:09:25 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-04-05 13:09:30 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.009 |  |
| 2026-04-05 12:03:31 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-04-05 13:03:17 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-05 13:03:51 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.013 |  |
| 2026-04-05 13:03:48 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:03:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:01:36 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-04-05 13:17:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.39 | 🟢 Normal | -0.032 |  |
| 2026-04-05 13:00:56 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.033 |  |
| 2026-04-05 13:01:31 | Thanthirimale (Malwathu Oya) | 2.88 | 🟢 Normal | -0.060 |  |
| 2026-04-05 13:16:32 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.069 |  |
| 2026-04-05 13:04:03 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.074 |  |
| 2026-04-05 13:01:13 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.148 |  |
| 2026-04-05 13:03:08 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.253 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)