# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_15:09:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,727 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 15:09:40 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-31 15:09:28 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:09:11 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 15:09:03 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 15:07:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-31 15:07:27 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | -0.033 |  |
| 2026-01-31 15:07:22 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:06:49 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:06:15 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-31 15:05:28 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:05:27 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:05:14 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:05:07 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:59 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:59 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:04:31 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-01-31 15:04:28 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:10 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:05 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 15:04:00 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.063 |  |
| 2026-01-31 15:04:00 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:03:18 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:03:15 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:02:55 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:02:48 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:02:31 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:02:15 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 15:02:04 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.136 |  |
| 2026-01-31 15:01:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-01-31 15:01:55 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:48 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:43 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-31 15:01:42 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:14 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:00:45 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 15:07:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-31 15:01:43 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-31 15:09:40 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-31 15:06:15 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-31 15:00:45 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 15:09:03 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 15:02:15 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 15:04:05 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 15:09:11 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 15:01:14 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:42 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:05:07 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:02:48 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:05:14 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:07:22 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:03:15 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:59 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:10 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:55 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:00 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:28 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:01:48 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 14:00:06 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:02:31 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:05:28 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:05:27 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:09:28 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-31 15:04:31 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-01-31 15:04:59 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-31 14:03:34 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:02:55 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:06:49 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:03:18 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.010 |  |
| 2026-01-31 15:01:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-01-31 15:07:27 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | -0.033 |  |
| 2026-01-31 15:04:00 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.063 |  |
| 2026-01-31 15:02:04 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)