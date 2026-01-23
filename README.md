# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_09:15:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 09:15:00 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:10:10 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-01-23 09:09:30 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.082 |  |
| 2026-01-23 09:08:01 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:07:59 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:07:15 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:06:51 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-01-23 09:06:32 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:05:33 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:05:30 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:05:22 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.150 |  |
| 2026-01-23 09:05:13 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:57 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.125 |  |
| 2026-01-23 09:04:45 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:21 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:19 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:04:15 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-23 09:04:11 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:09 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:04 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.046 |  |
| 2026-01-23 09:03:53 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:03:30 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:03:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 09:02:39 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.031 |  |
| 2026-01-23 09:02:36 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 09:02:33 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:02:31 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-23 09:02:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:02:25 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:02:22 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:02:14 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-23 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.051 |  |
| 2026-01-23 09:01:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:01:53 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-23 09:01:41 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:01:28 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-23 09:01:01 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:00:12 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 08:30:51 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 09:04:15 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-23 09:02:31 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-23 09:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-23 09:02:14 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-23 09:01:53 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-23 09:03:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 09:02:36 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 09:03:53 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:01:41 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:01:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:00:12 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:01:01 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:07:15 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:05:33 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:05:30 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:21 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:11 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:02:30 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:09 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:15:00 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:02:33 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:05:13 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:08:01 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:07:59 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:06:32 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:45 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:06:51 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-01-23 09:03:30 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:04:19 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:01:28 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:02:22 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-23 09:10:10 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-01-23 09:02:39 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.031 |  |
| 2026-01-23 09:04:04 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.046 |  |
| 2026-01-23 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.051 |  |
| 2026-01-23 09:09:30 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.082 |  |
| 2026-01-23 09:04:57 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.125 |  |
| 2026-01-23 09:05:22 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)