# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_08:05:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,874 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 08:05:56 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:05:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:05:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:04:47 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:04:37 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:04:09 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.100 |  |
| 2026-03-03 08:03:43 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:03:40 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.051 |  |
| 2026-03-03 08:03:12 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.140 |  |
| 2026-03-03 08:03:07 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:02:47 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.050 |  |
| 2026-03-03 08:02:35 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:02:20 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:02:12 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:02:09 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.021 |  |
| 2026-03-03 08:02:03 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-03-03 08:01:49 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.040 |  |
| 2026-03-03 08:01:46 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.067 |  |
| 2026-03-03 08:01:45 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:01:10 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:01:09 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:00:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:00:32 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:00:24 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:00:15 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:27:17 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-03 07:24:30 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.140 |  |
| 2026-03-03 07:19:04 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:18:11 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:17:46 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:16:55 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:15:18 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-03-03 07:14:52 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.050 |  |
| 2026-03-03 07:13:28 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 07:27:17 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-03-03 08:01:45 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:00:15 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:00:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 06:03:16 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:02:20 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:19:04 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:02:12 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:03:07 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:04:37 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:04:47 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:05:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:18:11 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:07:56 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:03:43 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:00:32 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:05:56 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 07:05:25 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:01:09 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-03 06:21:00 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:02:35 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:00:24 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-03 08:03:40 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-03 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:01:10 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:05:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-03 08:01:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-03 07:02:34 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.011 |  |
| 2026-03-03 08:02:03 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-03-03 08:02:09 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.021 |  |
| 2026-03-03 07:03:48 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-03-03 07:15:18 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-03-03 08:01:49 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | -0.040 |  |
| 2026-03-03 08:02:47 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.050 |  |
| 2026-03-03 08:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.051 |  |
| 2026-03-03 08:01:46 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.067 |  |
| 2026-03-03 08:04:09 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.100 |  |
| 2026-03-03 07:05:25 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | -0.133 |  |
| 2026-03-03 08:03:12 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)