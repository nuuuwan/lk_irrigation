# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_18:37:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,777 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 18:37:54 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:24:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:18:10 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:17:49 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:09:51 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:07:43 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:06:18 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:06:07 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:05:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-03-29 18:05:12 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:04:52 | Thawalama (Gin Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-03-29 18:04:33 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:04:29 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:04:21 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.030 |  |
| 2026-03-29 18:04:19 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:04:11 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.176 |  |
| 2026-03-29 18:03:44 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 18:03:02 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:53 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:43 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-29 18:02:40 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:36 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:34 | Magura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:33 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-29 18:02:30 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-03-29 18:02:29 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.040 |  |
| 2026-03-29 18:02:27 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.457 |  |
| 2026-03-29 18:02:24 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:20 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-29 18:02:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:03 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-29 18:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.071 |  |
| 2026-03-29 18:00:58 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:00:53 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.229 |  |
| 2026-03-29 18:00:44 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 18:02:20 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-29 18:02:43 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-29 18:03:44 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-29 18:00:58 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:04:19 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:24:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:24 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:04:29 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:03:02 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:34 | Magura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:06:18 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:36 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:07:43 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:37:54 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:17:49 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:03 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:40 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:12 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:49 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:05:12 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:06:07 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:09:51 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:53 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:04:33 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:02:30 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-03-29 18:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-29 17:04:52 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-03-29 18:02:33 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-03-29 18:04:21 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.030 |  |
| 2026-03-29 18:05:31 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-03-29 18:04:52 | Thawalama (Gin Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-03-29 18:02:29 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.040 |  |
| 2026-03-29 18:00:44 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.047 |  |
| 2026-03-29 18:01:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.071 |  |
| 2026-03-29 18:04:11 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.176 |  |
| 2026-03-29 18:00:53 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.229 |  |
| 2026-03-29 18:02:27 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.457 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)