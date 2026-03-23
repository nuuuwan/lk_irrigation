# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_19:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,432 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 19:11:11 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 19:10:58 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-23 19:10:45 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:10:21 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:10:20 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.061 |  |
| 2026-03-23 19:07:46 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.119 |  |
| 2026-03-23 19:07:32 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-23 19:06:55 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.036 |  |
| 2026-03-23 19:06:53 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:06:48 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:06:08 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:05:55 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:05:45 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:05:43 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-23 19:05:14 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 19:05:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.116 |  |
| 2026-03-23 19:04:48 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:03:20 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-23 19:03:19 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-03-23 19:03:16 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:03:00 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:57 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-23 19:02:43 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.039 |  |
| 2026-03-23 19:02:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:32 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:15 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:08 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-03-23 19:01:35 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:01:31 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -24.000 |  |
| 2026-03-23 19:01:28 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -24.000 |  |
| 2026-03-23 19:00:58 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 19:00:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:26:03 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-23 18:26:02 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-23 18:26:00 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-23 18:25:59 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-23 18:25:40 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:23:41 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 19:03:19 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-03-23 19:10:58 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-23 19:05:43 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-23 19:00:58 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 19:07:32 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-23 19:05:14 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 19:11:11 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 19:05:55 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:00:37 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:32 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:10:45 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:03:00 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:04:48 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:05:45 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:10:21 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:03:16 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:06:53 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:22 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:15 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:43 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:06:48 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:06:08 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:01:35 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:08 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 19:02:57 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:04:53 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-23 19:02:00 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-03-23 19:03:20 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-23 19:06:55 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.036 |  |
| 2026-03-23 19:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.039 |  |
| 2026-03-23 19:10:20 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.061 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |
| 2026-03-23 19:05:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.116 |  |
| 2026-03-23 19:07:46 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.119 |  |
| 2026-03-23 19:01:31 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -24.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)