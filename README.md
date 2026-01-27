# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_05:32:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,734 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 05:32:03 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:14:56 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-27 05:13:42 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:13:31 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 05:12:18 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.029 |  |
| 2026-01-27 05:09:20 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 05:08:06 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:06:59 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 05:06:06 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-01-27 05:05:45 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-01-27 05:04:58 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:04:56 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:04:28 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-01-27 05:04:05 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:38 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:25 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:25 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.014 |  |
| 2026-01-27 05:02:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 05:02:45 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-27 05:02:34 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:02:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:02:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-01-27 05:01:52 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.105 |  |
| 2026-01-27 05:01:44 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:40 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:40 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:14 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.283 |  |
| 2026-01-27 05:01:07 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.142 |  |
| 2026-01-27 05:01:04 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:00:18 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:00:12 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-01-27 04:39:54 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 03:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-27 05:14:56 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-27 05:02:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 05:09:20 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 05:06:59 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 05:13:31 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-26 18:00:09 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:00:18 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:04 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:04:58 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:44 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:30 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:40 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:13:42 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:08:06 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:38 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:02:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:04:56 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:02:34 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:40 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:25 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:04:05 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:32:03 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:03:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:01:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-27 04:04:58 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 05:06:06 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-01-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-27 05:02:45 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-27 05:00:12 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-01-27 05:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.014 |  |
| 2026-01-27 05:04:28 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-01-27 05:02:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.020 |  |
| 2026-01-27 05:05:45 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-01-27 04:16:47 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.028 |  |
| 2026-01-27 05:12:18 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.029 |  |
| 2026-01-27 05:01:52 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.105 |  |
| 2026-01-27 05:01:07 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.142 |  |
| 2026-01-27 05:01:14 | Kithulgala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.283 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)