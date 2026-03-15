# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_13:12:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,033 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 13:12:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 13:10:06 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:08:07 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:07:44 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:06:58 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 13:06:22 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.028 |  |
| 2026-03-15 13:06:08 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 13:05:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-15 13:05:23 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:04:58 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:04:54 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:04:39 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:04:33 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:04:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-15 13:04:23 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.005 |  |
| 2026-03-15 13:04:11 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.137 |  |
| 2026-03-15 13:04:02 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.030 |  |
| 2026-03-15 13:03:55 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:03:54 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:03:41 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-03-15 13:03:23 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.059 |  |
| 2026-03-15 13:03:02 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 13:02:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:02:17 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-15 13:02:06 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:02:05 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:01:48 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:01:45 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-03-15 13:01:37 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:01:06 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:01:01 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-15 13:00:32 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:00:13 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.365 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 13:00:13 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2026-03-15 13:05:29 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-15 12:05:01 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-15 13:04:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-15 13:02:17 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-03-15 12:02:54 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-15 12:07:52 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-15 13:01:01 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-15 13:06:08 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 13:12:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 13:03:02 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 13:06:58 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 13:01:48 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:10:06 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-15 12:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:04:58 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:01:37 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:00:32 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:02:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:04:33 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:04:39 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:08:07 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:01:06 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 13:04:23 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.005 |  |
| 2026-03-15 13:03:54 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:07:44 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:02:05 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:05:23 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:04:54 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:03:55 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:02:06 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-15 13:03:41 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-03-15 12:02:23 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-03-15 13:06:22 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.028 |  |
| 2026-03-15 13:04:02 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.030 |  |
| 2026-03-15 13:01:45 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-03-15 13:03:23 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.059 |  |
| 2026-03-15 13:04:11 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)