# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_16:07:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,387 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 16:07:16 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:06:15 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:06:05 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:05:37 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:05:21 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:05:10 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:05:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-01-25 16:04:04 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:04:03 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:03:52 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 16:03:43 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:03:40 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:03:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:02:59 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 16:02:53 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:49 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:41 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:26 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:21 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:18 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:00 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:01:39 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-25 16:01:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-25 16:01:29 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:01:28 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:01:15 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-25 16:01:10 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.120 |  |
| 2026-01-25 16:01:10 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-25 16:01:06 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:00:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 16:00:23 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:16:55 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-25 15:13:37 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 16:01:10 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-01-25 16:01:30 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-25 16:01:15 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-25 15:03:14 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-25 16:00:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 16:03:52 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 16:02:59 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 16:01:28 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:01:29 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:00:23 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:01:48 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:26 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:03:43 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:05:21 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:53 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:06:15 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:04:58 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:06:59 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:04:04 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:26 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:01:06 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:03:40 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:49 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:21 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:02:18 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:04:03 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:06:05 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-25 15:01:48 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 16:07:16 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:02:00 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:02:41 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:03:37 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:05:37 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:05:10 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-25 16:01:39 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-25 16:05:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-01-25 15:01:20 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.041 |  |
| 2026-01-25 16:01:10 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | -0.120 |  |
| 2026-01-25 15:07:05 | Baddegama (Gin Ganga) | 0.11 | 🟢 Normal | -1.884 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)