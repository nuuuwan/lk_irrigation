# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_06:18:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,506 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 06:18:27 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 1.330 | 🔺 Rising |
| 2026-03-27 06:13:39 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:09:16 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:06:14 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-03-27 06:06:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:58 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-03-27 06:05:48 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-27 06:05:36 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:24 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:04 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:01 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.005 |  |
| 2026-03-27 06:04:57 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:04:33 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-27 06:04:29 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:04:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 06:04:06 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:04:05 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:03:14 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:03:12 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:03:11 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:03:09 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 06:03:08 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:03:05 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-03-27 06:02:58 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:58 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-27 06:02:55 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-27 06:02:44 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:40 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-27 06:02:37 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:23 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:22 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:01:54 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:01:24 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.005 |  |
| 2026-03-27 06:01:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.041 |  |
| 2026-03-27 06:01:05 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:00:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-27 05:58:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.064 |  |
| 2026-03-27 05:33:20 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 1.330 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 06:18:27 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 1.330 | 🔺 Rising |
| 2026-03-27 06:06:14 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-03-27 06:04:33 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-27 06:02:55 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-27 06:02:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-27 06:03:09 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 05:04:23 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 06:04:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 06:01:24 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.005 |  |
| 2026-03-27 06:05:01 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.005 |  |
| 2026-03-27 06:01:54 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:23 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:00:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:37 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:01:05 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 18:01:41 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:13:39 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:04:06 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:04:29 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:36 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:06:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:04 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:03:08 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:22 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:58 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:40 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:24 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:04:57 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:09:16 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-27 05:09:32 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:02:44 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:05:48 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-27 06:02:58 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-27 06:05:58 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-03-27 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-27 06:03:05 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-03-27 06:01:09 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.041 |  |
| 2026-03-27 05:58:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)