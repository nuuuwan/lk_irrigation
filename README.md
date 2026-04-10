# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_05:32:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,980 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 05:32:50 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:32:48 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:32:47 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:20:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-10 05:20:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:19:09 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-04-10 05:18:07 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-10 05:15:22 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-04-10 05:11:34 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:10:49 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 05:08:16 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:07:27 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:07:07 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -36.000 |  |
| 2026-04-10 05:07:06 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -36.000 |  |
| 2026-04-10 05:07:04 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -36.000 |  |
| 2026-04-10 05:06:55 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.123 |  |
| 2026-04-10 05:06:27 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:05:28 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.011 |  |
| 2026-04-10 05:05:07 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-04-10 05:05:06 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-10 05:04:53 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-10 05:03:48 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 05:02:51 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-10 05:02:46 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-10 05:02:19 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.016 |  |
| 2026-04-10 05:02:15 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -1.636 |  |
| 2026-04-10 05:01:49 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.081 |  |
| 2026-04-10 05:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:29 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:22 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -1.636 |  |
| 2026-04-10 05:01:13 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.123 |  |
| 2026-04-10 05:01:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:00:25 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:00:24 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:00:24 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 05:05:07 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-04-10 05:04:53 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-10 03:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-10 05:05:06 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-10 05:18:07 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-10 05:20:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-10 05:10:49 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 05:03:48 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 05:00:25 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:29 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:02:15 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:03:26 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:32:50 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:11:34 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:20:20 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-10 04:08:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:08:16 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:22 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:07:27 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 05:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-10 03:09:30 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-10 01:52:00 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.005 |  |
| 2026-04-10 05:02:46 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-10 05:02:51 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-10 05:05:28 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.011 |  |
| 2026-04-10 05:19:09 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-04-10 05:02:19 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.016 |  |
| 2026-04-10 05:15:22 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2026-04-10 05:00:24 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.066 |  |
| 2026-04-10 05:01:49 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.081 |  |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-10 05:06:55 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.123 |  |
| 2026-04-10 05:01:13 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.123 |  |
| 2026-04-10 05:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -1.636 |  |
| 2026-04-10 05:07:07 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)