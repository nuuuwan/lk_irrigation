# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_02:20:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 02:20:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:20:13 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:19:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-19 02:14:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:12:23 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-06-19 02:08:24 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | -0.028 |  |
| 2026-06-19 02:05:37 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:05:12 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 02:05:05 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-19 02:04:57 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.270 |  |
| 2026-06-19 02:04:52 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:04:51 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-19 02:04:35 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:04:29 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 02:04:22 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:03:59 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:03:59 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.039 |  |
| 2026-06-19 02:03:58 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:03:45 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:03:44 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:03:11 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-19 02:03:05 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-06-19 02:02:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:02:27 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:02:27 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 02:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.014 |  |
| 2026-06-19 02:02:06 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:02:04 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 02:01:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:01:46 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:00:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:35:06 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 02:04:51 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-19 02:19:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.12 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-19 02:05:05 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-19 02:03:11 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-19 02:04:29 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 02:05:12 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-19 02:02:04 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 02:02:27 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 02:03:44 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:20:13 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:00:51 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:02:06 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:03:59 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:01:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:03:58 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:02:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:03:50 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:02:27 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:20:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:14:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:03:45 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:01:46 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:18:58 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.007 |  |
| 2026-06-19 02:04:35 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:05:37 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:04:22 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:12:23 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-06-19 02:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.014 |  |
| 2026-06-19 01:35:06 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-06-19 01:23:51 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.015 |  |
| 2026-06-19 02:08:24 | Dunamale (Aththanagalu Oya) | 2.77 | 🟢 Normal | -0.028 |  |
| 2026-06-19 02:03:05 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-06-19 02:03:59 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.039 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-19 01:08:37 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | -0.045 |  |
| 2026-06-19 02:04:57 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.270 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)