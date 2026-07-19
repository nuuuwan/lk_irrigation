# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--19_11:36:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **210,405 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 11:36:27 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:23:20 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:17:34 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:16:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.033 |  |
| 2026-07-19 11:13:05 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-07-19 11:12:34 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:12:11 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:09:44 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:08:59 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.219 |  |
| 2026-07-19 11:08:21 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:08:03 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:07:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-19 11:06:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.018 |  |
| 2026-07-19 11:06:33 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 11:05:48 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:05:42 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-07-19 11:05:33 | Nagalagam Street (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-07-19 11:05:20 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:03:21 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:03:09 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:56 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-07-19 11:02:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:48 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:43 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:32 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:20 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:08 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:03 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:44 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:38 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:32 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:28 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:26 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-07-19 11:01:24 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-19 11:01:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-19 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:00:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:00:46 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:00:15 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:00:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-19 11:01:26 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-07-19 11:01:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-19 11:07:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-19 11:06:33 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-19 11:01:24 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-19 11:00:46 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:38 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:03 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:12:34 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:44 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:00:54 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:05:48 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:08:03 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:36:27 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:48 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:08 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:23:20 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:00:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:32 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:08:21 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:00:15 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:20 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:05:20 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:03:09 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:28 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:09:44 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:17:34 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:01:32 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:03:21 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:02:43 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-19 11:13:05 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-07-19 11:02:56 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-07-19 11:06:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.018 |  |
| 2026-07-19 11:05:42 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-07-19 11:05:33 | Nagalagam Street (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-07-19 11:16:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.033 |  |
| 2026-07-19 11:08:59 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)