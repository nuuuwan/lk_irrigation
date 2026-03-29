# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_23:23:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,959 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 23:23:26 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:16:18 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:09:57 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-03-29 23:08:41 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-03-29 23:07:50 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:07:26 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-29 23:07:16 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-29 23:06:00 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:57 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:49 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-29 23:05:41 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-29 23:05:38 | Magura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:27 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:20 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:10 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.024 |  |
| 2026-03-29 23:04:40 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:04:32 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:03:52 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:03:38 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 1.008 | 🔺 Rising |
| 2026-03-29 23:02:49 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 23:02:27 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 23:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:02:15 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 23:02:12 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:02:00 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-03-29 23:01:58 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 23:01:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:01:35 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:01:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:01:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-03-29 23:00:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:00:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 23:03:38 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 1.008 | 🔺 Rising |
| 2026-03-29 23:05:47 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-29 23:07:26 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-29 23:01:58 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 23:07:16 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-29 23:02:27 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 23:02:49 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 23:02:15 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 23:04:32 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:20 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:00:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:16:18 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:01:43 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:02:12 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:01:35 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:03:02 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:38 | Magura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:03:52 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-29 22:15:32 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:23:26 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:57 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:00:50 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:49 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:05:27 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:07:50 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:06:00 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:01:31 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:04:40 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 23:09:57 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-03-29 23:05:41 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-29 22:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-29 23:01:00 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-03-29 23:05:10 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.024 |  |
| 2026-03-29 23:08:41 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-03-29 23:02:00 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.040 |  |
| 2026-03-29 18:00:53 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)