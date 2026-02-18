# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_00:17:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,836 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 00:17:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:10:40 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:09:33 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 00:07:14 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-19 00:06:29 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-02-19 00:05:39 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 00:05:23 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:05:19 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:04:26 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-02-19 00:04:21 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:53 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:26 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-19 00:03:18 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:16 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:02 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 00:02:53 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:50 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.061 |  |
| 2026-02-19 00:02:46 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:44 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-19 00:02:37 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:37 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:17 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:14 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-19 00:02:11 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-19 00:01:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-19 00:01:47 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:01:24 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:00:55 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:00:43 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:00:32 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:00:08 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-18 23:59:59 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 23:06:21 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-02-19 00:04:26 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-02-19 00:01:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-02-19 00:02:11 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-02-19 00:07:14 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-19 00:02:44 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-19 00:03:02 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 00:05:39 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 00:09:33 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 00:00:08 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-19 00:02:37 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:00:55 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:01:24 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:17:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:46 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 23:41:10 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:04:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:10:40 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:53 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:37 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:04:21 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:01:47 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:05:23 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:00:32 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-18 23:59:59 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:18 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:34 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:53 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:00:43 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:02:17 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:05:19 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-18 23:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:06:29 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-02-19 00:03:26 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-19 00:02:14 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-18 18:01:50 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-19 00:02:50 | Manampitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)