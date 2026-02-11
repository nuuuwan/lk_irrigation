# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_16:27:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,287 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 16:27:43 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:23:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-11 16:16:02 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:15:43 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-02-11 16:11:55 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:10:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.013 |  |
| 2026-02-11 16:10:11 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-02-11 16:09:06 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:08:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-11 16:06:56 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:06:51 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:06:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:06:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:05:47 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:05:15 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-11 16:05:04 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:05:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:04:46 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:04:41 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:04:17 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-11 16:03:57 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-11 16:03:50 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:03:49 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:03:33 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.211 |  |
| 2026-02-11 16:03:31 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:03:28 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-02-11 16:03:15 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 16:03:11 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:03:03 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:03:01 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 16:02:50 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 16:02:24 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:02:00 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:01:43 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-11 16:01:32 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:00:57 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:00:36 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 16:03:57 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-11 16:04:17 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-11 16:08:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-02-11 16:01:43 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-11 16:23:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-11 16:00:36 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-11 16:03:01 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 16:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 16:05:15 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-11 16:03:15 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 16:05:04 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:03:50 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:04:46 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:06:51 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:02:24 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:04:41 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:09:06 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:11:55 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:03:49 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 15:02:50 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:03:11 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:00:57 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:02:50 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:05:47 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:27:43 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:06:56 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:06:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:05:01 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:06:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:16:02 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:15:43 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-02-11 16:10:11 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-02-11 16:01:32 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:03:31 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:02:00 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:03:03 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-11 16:10:55 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.013 |  |
| 2026-02-11 16:03:28 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-02-11 16:03:33 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.211 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)