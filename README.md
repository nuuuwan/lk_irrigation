# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_06:30:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 06:30:03 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.067 |  |
| 2026-05-19 06:10:14 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-05-19 06:08:04 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-19 06:07:22 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:07:18 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-05-19 06:06:25 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:06:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.136 |  |
| 2026-05-19 06:06:07 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:05:14 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-05-19 06:04:42 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-19 06:04:35 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:04:34 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:04:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.105 |  |
| 2026-05-19 06:04:25 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-05-19 06:04:23 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-05-19 06:04:14 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:03:48 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:03:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:03:05 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | -0.106 |  |
| 2026-05-19 06:02:42 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-05-19 06:02:39 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:02:38 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-05-19 06:02:37 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-19 06:02:36 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:02:35 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:02:32 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.032 |  |
| 2026-05-19 06:02:30 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-05-19 06:02:21 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.063 |  |
| 2026-05-19 06:02:06 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-05-19 06:01:51 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:01:37 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-19 06:01:31 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-05-19 06:01:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:01:18 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | -0.025 |  |
| 2026-05-19 06:00:39 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 06:02:37 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-05-19 06:08:04 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-19 06:04:42 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-19 06:00:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-19 06:01:37 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-19 06:00:31 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:02:36 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:03:39 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:03:48 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:07:22 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:06:07 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:04:34 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:04:35 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:02:35 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:01:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 06:10:14 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-05-19 06:07:18 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-05-19 06:06:25 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:02:39 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:01:51 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:04:14 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:03:05 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.010 |  |
| 2026-05-19 06:02:38 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-05-19 06:02:42 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-05-19 06:01:31 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-05-19 06:04:25 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-05-19 06:04:23 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.021 |  |
| 2026-05-19 06:01:18 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | -0.025 |  |
| 2026-05-19 06:02:06 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-05-19 06:02:32 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.032 |  |
| 2026-05-19 06:05:14 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-05-19 06:00:39 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.043 |  |
| 2026-05-19 06:02:30 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-05-19 06:02:21 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.063 |  |
| 2026-05-19 06:30:03 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | -0.067 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-19 06:04:30 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.105 |  |
| 2026-05-19 06:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | -0.106 |  |
| 2026-05-19 06:06:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)