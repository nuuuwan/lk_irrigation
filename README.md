# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_19:23:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 19:23:09 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:22:50 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:20:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.015 |  |
| 2026-01-11 19:13:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-11 19:12:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-11 19:08:56 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:08:15 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-11 19:07:27 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-11 19:06:35 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 19:06:31 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-01-11 19:06:01 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-11 19:05:25 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 19:04:37 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:04:37 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.061 |  |
| 2026-01-11 19:04:14 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-01-11 19:04:12 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.030 |  |
| 2026-01-11 19:04:06 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:04:05 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 19:03:14 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:03:10 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 19:03:06 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:54 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:53 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:44 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:28 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:24 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-01-11 19:01:59 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.049 |  |
| 2026-01-11 19:01:38 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:01:23 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.015 |  |
| 2026-01-11 19:01:11 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:01:11 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:01:06 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-11 19:01:04 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.076 |  |
| 2026-01-11 19:00:43 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -1.221 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 19:08:15 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-11 19:07:27 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-11 19:06:01 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-11 19:13:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-11 19:12:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-11 19:03:10 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 19:03:32 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 19:06:35 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 19:05:25 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:01:11 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:01:38 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:23:09 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:03:14 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:03:06 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:53 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:54 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:01:11 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:04:05 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:00:34 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:24 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:08:56 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:28 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:02:44 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:04:06 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:04:37 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 19:06:31 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-01-11 19:01:23 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.015 |  |
| 2026-01-11 19:20:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.015 |  |
| 2026-01-11 19:04:14 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-01-11 19:01:06 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-01-11 19:02:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.029 |  |
| 2026-01-11 19:04:12 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.030 |  |
| 2026-01-11 19:01:59 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.049 |  |
| 2026-01-11 19:04:37 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.061 |  |
| 2026-01-11 19:01:04 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.076 |  |
| 2026-01-11 19:00:43 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -1.221 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)