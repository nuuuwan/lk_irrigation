# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_19:13:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,863 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 19:13:46 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-19 19:10:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 19:09:32 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:07:09 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 19:06:17 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.048 |  |
| 2026-03-19 19:05:57 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.047 |  |
| 2026-03-19 19:05:53 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-19 19:05:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-03-19 19:05:37 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.024 |  |
| 2026-03-19 19:05:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-03-19 19:05:14 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 19:05:14 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-03-19 19:05:07 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:04:57 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:04:54 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 19:04:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:04:49 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:03:44 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 19:03:36 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-03-19 19:03:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-19 19:03:23 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.045 |  |
| 2026-03-19 19:03:00 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-03-19 19:02:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:02:31 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-03-19 19:02:30 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-19 19:02:27 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 19:02:11 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 19:01:55 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:01:40 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-19 19:01:35 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:01:29 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 19:01:20 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2026-03-19 19:01:09 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:00:45 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:00:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 19:02:30 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-03-19 19:13:46 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-19 19:05:53 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-19 19:02:27 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 19:03:26 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-19 19:02:11 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-19 19:05:14 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 19:04:54 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 19:01:29 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 19:03:44 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 19:07:09 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 19:10:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 19:01:09 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:09:32 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:01:55 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:00:45 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:00:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:02:40 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:04:57 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:04:52 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:05:07 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:04:49 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 19:05:14 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-03-19 19:01:40 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-19 19:02:31 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-03-19 19:03:00 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-03-19 19:05:37 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.024 |  |
| 2026-03-19 19:05:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-03-19 19:03:36 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-03-19 19:03:23 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.045 |  |
| 2026-03-19 19:05:57 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.047 |  |
| 2026-03-19 19:06:17 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.048 |  |
| 2026-03-19 19:01:20 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.050 |  |
| 2026-03-19 19:05:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.061 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-19 18:01:50 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)