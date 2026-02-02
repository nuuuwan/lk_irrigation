# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--03_05:18:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-03 05:16:15 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.016 |  |
| 2026-02-03 05:11:52 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-02-03 05:09:30 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:07:22 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.127 |  |
| 2026-02-03 05:07:15 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.406 |  |
| 2026-02-03 05:06:48 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-02-03 05:04:55 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-02-03 05:04:47 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:04:45 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-03 05:04:38 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:04:36 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 05:03:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-03 05:03:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-03 05:03:31 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:03:31 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:03:12 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:03:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-02-03 05:02:44 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-03 05:02:41 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-03 05:02:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 05:02:25 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-03 05:02:23 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-03 05:02:22 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.115 |  |
| 2026-02-03 05:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-02-03 05:01:55 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:01:03 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:16 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.187 |  |
| 2026-02-03 05:00:13 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-03 04:57:57 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.127 |  |
| 2026-02-03 04:43:37 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.406 |  |
| 2026-02-03 04:41:00 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.187 |  |
| 2026-02-03 04:25:59 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.093 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:06:48 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-03 04:25:59 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-03 05:04:36 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-03 05:03:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-03 05:04:45 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-03 03:56:29 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 05:02:25 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-03 05:00:13 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-03 05:02:44 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-03 04:02:19 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-03 05:02:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-03 05:01:55 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:03:31 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:04:38 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:03:12 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:09:30 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:04:47 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:03:31 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:01:03 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:11:52 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-02-03 05:03:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-02-03 05:02:23 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-02-03 05:02:41 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-03 05:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-02-03 05:04:55 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-02-03 05:16:15 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.016 |  |
| 2026-02-03 04:03:30 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 05:03:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 05:02:22 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.115 |  |
| 2026-02-03 05:07:22 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.127 |  |
| 2026-02-03 05:00:16 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.187 |  |
| 2026-02-03 05:07:15 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.406 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)