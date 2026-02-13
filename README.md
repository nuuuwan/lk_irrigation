# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_20:17:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 20:17:17 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.016 |  |
| 2026-02-13 20:16:05 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.026 |  |
| 2026-02-13 20:15:51 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:14:53 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-02-13 20:11:56 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-02-13 20:11:31 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:08:13 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:07:43 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:07:11 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-02-13 20:06:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-13 20:05:59 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 20:05:37 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-13 20:05:33 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.060 |  |
| 2026-02-13 20:05:21 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-02-13 20:05:02 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:59 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:47 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:03 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:00 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-13 20:03:59 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-13 20:02:59 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-02-13 20:02:49 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:02:38 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-02-13 20:02:16 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-13 20:02:11 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:02:03 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:59 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:58 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:45 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:34 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-13 20:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:23 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-13 20:01:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-13 20:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.41 | 🟢 Normal | -0.093 |  |
| 2026-02-13 20:00:48 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:00:36 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 20:14:53 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-02-13 20:02:59 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-02-13 20:01:23 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-13 20:01:12 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-13 20:04:00 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-13 20:06:18 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-13 20:05:37 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-13 20:05:59 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 20:01:58 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:02:03 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:00:48 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:45 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:02:49 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:08:13 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:56 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:59 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:11:31 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:03:59 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:04:03 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:15:51 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:02:11 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:05:02 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:01:59 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:07:43 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 20:03:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-13 20:02:16 | Dunamale (Aththanagalu Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-02-13 20:01:34 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-13 20:11:56 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-02-13 20:17:17 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.016 |  |
| 2026-02-13 20:07:11 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-02-13 20:05:21 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-02-13 20:02:38 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-02-13 20:16:05 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.026 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-13 20:05:33 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.060 |  |
| 2026-02-13 20:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.41 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)