# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_14:10:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,810 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 14:10:19 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-06 14:10:03 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:09:09 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:08:55 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:07:22 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:06:08 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-03-06 14:05:57 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:05:54 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:05:34 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:05:15 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-06 14:05:11 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:04:43 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.098 |  |
| 2026-03-06 14:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:04:10 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.041 |  |
| 2026-03-06 14:03:51 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:03:46 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:03:45 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 14:03:41 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-06 14:03:38 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 14:03:16 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:03:07 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:48 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:02:46 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:22 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:19 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:00 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:50 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:40 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:30 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:26 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:01:08 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-03-06 14:01:07 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:06 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:46 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 14:00:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:37 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:25 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:56:08 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 13:56:01 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 14:01:08 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-03-06 14:05:15 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-06 14:03:41 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-06 14:10:19 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-06 14:03:45 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 14:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 14:03:38 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 14:01:50 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:05:34 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:46 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:40 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:19 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:05:57 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:08:55 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:05:54 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:00 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:03:16 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:09:09 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:07 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:03:46 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:30 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:03:07 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:10:03 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:07:22 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:01:06 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:46 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:22 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:00:37 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-06 14:02:48 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:03:51 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:05:11 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:01:26 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-06 14:06:08 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-03-06 14:04:10 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.041 |  |
| 2026-03-06 14:04:43 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)