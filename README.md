# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_07:10:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 07:10:56 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-29 07:09:20 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.067 |  |
| 2026-03-29 07:08:35 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.063 |  |
| 2026-03-29 07:07:59 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:07:46 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-03-29 07:05:51 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-29 07:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-03-29 07:05:36 | Hanwella (Kelani Ganga) | 0.16 | 🟢 Normal | -0.028 |  |
| 2026-03-29 07:05:26 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:05:25 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-29 07:05:07 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 07:04:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-29 07:03:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:03:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:03:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:02:45 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:02:32 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:02:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.054 |  |
| 2026-03-29 07:01:59 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:55 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:53 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:48 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.034 |  |
| 2026-03-29 07:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-03-29 07:01:25 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-29 07:01:16 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.051 |  |
| 2026-03-29 07:01:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:50 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:44 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:09 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:31:46 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:19:42 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 07:07:46 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-03-29 07:01:25 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-29 07:10:56 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-29 06:04:21 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-29 07:04:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-29 06:11:23 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-29 07:05:07 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 07:01:53 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:29 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:59 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:05:26 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:44 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:09 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:46 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:02:45 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:02:32 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:55 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:00:28 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:25 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:03:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:50 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:03:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:07:59 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:05:47 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:01:18 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:03:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 06:04:52 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:01:12 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:05:25 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-29 07:05:51 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-29 06:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-03-29 07:05:36 | Hanwella (Kelani Ganga) | 0.16 | 🟢 Normal | -0.028 |  |
| 2026-03-29 07:01:48 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.034 |  |
| 2026-03-29 07:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-03-29 07:01:16 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.051 |  |
| 2026-03-29 07:02:30 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.054 |  |
| 2026-03-29 07:01:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-03-29 07:08:35 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.063 |  |
| 2026-03-29 07:09:20 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)