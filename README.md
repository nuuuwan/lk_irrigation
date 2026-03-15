# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_17:07:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 17:07:11 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:06:46 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-03-15 17:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.076 |  |
| 2026-03-15 17:06:23 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:05:32 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:05:29 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-15 17:05:24 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-15 17:04:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-03-15 17:04:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:04:20 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:03:35 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:03:18 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.079 |  |
| 2026-03-15 17:03:11 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:03:08 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:03:07 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:03:01 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-03-15 17:02:58 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:02:40 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-03-15 17:02:38 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.058 |  |
| 2026-03-15 17:02:20 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:02:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:02:05 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:46 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:45 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:31 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:28 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-15 17:01:16 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-03-15 17:01:13 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:13 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-15 17:01:09 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 17:01:08 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 17:00:37 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:00:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 17:02:40 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-03-15 17:05:29 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-15 17:01:13 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-15 17:05:24 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-15 16:06:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 17:01:08 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 17:01:09 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 17:00:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 17:06:23 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:02:20 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:01:15 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:04:20 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:04:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:03:08 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:45 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:02:05 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 16:05:14 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:31 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:01:46 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:02:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:05:32 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:03:11 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:07:11 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 17:03:35 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:01:10 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:02:58 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:03:07 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:00:37 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-15 16:07:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:01:28 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-15 17:03:01 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-03-15 17:01:16 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-03-15 17:06:46 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-03-15 16:07:10 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.028 |  |
| 2026-03-15 17:04:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-03-15 17:02:38 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.058 |  |
| 2026-03-15 16:11:42 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-03-15 17:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.076 |  |
| 2026-03-15 17:03:18 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)