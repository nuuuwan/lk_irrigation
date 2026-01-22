# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--22_18:10:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **52,789 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 18:10:45 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:09:04 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-01-22 18:07:29 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:08 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:06 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:06:42 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.057 |  |
| 2026-01-22 18:06:40 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-22 18:05:57 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 18:05:41 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:04:41 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:04:28 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:04:03 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:03:55 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-22 18:03:36 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:03:36 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:03:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:03:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:52 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:41 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:28 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:25 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:23 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-01-22 18:02:20 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2026-01-22 18:01:44 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:34 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:33 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.022 |  |
| 2026-01-22 18:01:28 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:20 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:17 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.081 |  |
| 2026-01-22 18:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:53 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:38 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:37 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:35 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:12 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:00:06 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 17:01:30 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-22 18:03:55 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-22 18:06:40 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-22 18:05:57 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 18:00:35 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:53 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:28 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:29 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:08 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:37 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:28 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:04:41 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:20 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:03:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:10:45 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:20 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:25 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:03:36 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:06 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:00:38 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:04:28 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:41 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:01:34 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:52 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:09:04 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:03:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-22 18:07:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.009 |  |
| 2026-01-22 18:05:41 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:04:03 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:03:36 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:00:12 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-22 18:02:23 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-01-22 18:01:33 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.022 |  |
| 2026-01-22 18:00:06 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.050 |  |
| 2026-01-22 18:06:42 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.057 |  |
| 2026-01-22 18:01:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2026-01-22 18:01:17 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)