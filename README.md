# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_17:25:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 17:25:16 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:16:58 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-10 17:12:45 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.018 |  |
| 2026-06-10 17:08:43 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:08:02 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-10 17:07:41 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:07:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:06:45 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:06:30 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:06:03 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.011 |  |
| 2026-06-10 17:04:56 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:04:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:04:23 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:04:20 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:04:00 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:03:59 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:03:49 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:03:41 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:03:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.034 |  |
| 2026-06-10 17:03:33 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.030 |  |
| 2026-06-10 17:03:22 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.040 |  |
| 2026-06-10 17:03:18 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 17:03:11 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 17:02:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:02:29 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.059 |  |
| 2026-06-10 17:02:27 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 17:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.61 | 🟢 Normal | -0.020 |  |
| 2026-06-10 17:02:22 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:02:10 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-06-10 17:02:03 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-06-10 17:02:01 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:01:53 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-06-10 17:01:29 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.022 |  |
| 2026-06-10 17:01:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -1.895 |  |
| 2026-06-10 17:01:15 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:01:09 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:01:09 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 17:08:02 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-10 17:16:58 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-10 17:03:11 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 17:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 17:02:27 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 17:01:15 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:03:41 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:02:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:00:48 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:06:30 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:03:49 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:02:22 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:01:09 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:04:56 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:07:16 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:25:16 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:04:23 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:03:18 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:01:09 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:07:41 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-10 17:08:43 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:04:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:04:20 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:03:59 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:02:01 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:06:45 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:04:00 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-06-10 17:02:10 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-06-10 17:02:03 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-06-10 17:06:03 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.011 |  |
| 2026-06-10 17:12:45 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.018 |  |
| 2026-06-10 17:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.61 | 🟢 Normal | -0.020 |  |
| 2026-06-10 17:01:29 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.022 |  |
| 2026-06-10 17:03:33 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.030 |  |
| 2026-06-10 17:03:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.034 |  |
| 2026-06-10 17:03:22 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.040 |  |
| 2026-06-10 17:01:53 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-06-10 17:02:29 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.059 |  |
| 2026-06-10 17:01:15 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)