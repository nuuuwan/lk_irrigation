# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_22:23:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,427 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 22:23:10 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:15:13 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.044 |  |
| 2026-03-03 22:14:13 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:11:17 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 22:07:54 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:07:46 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-03 22:07:34 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:06:30 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:05:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:04:47 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:04:20 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:04:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 22:04:14 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:04:09 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 22:03:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.120 |  |
| 2026-03-03 22:03:31 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:03:25 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:03:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-03 22:03:07 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:03:01 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:34 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:26 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:13 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-03-03 22:01:52 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:45 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-03-03 22:01:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:30 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:29 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:00:48 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 22:03:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-03 22:04:09 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 22:11:17 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 22:04:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 18:08:32 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 22:03:25 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:04:47 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:04:20 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:00:48 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:23:10 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:52 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:26 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:34 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:03:01 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:14:13 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:19:44 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:03:31 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:30 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:01:29 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:13 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:04:14 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:06:30 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:03:07 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:05:59 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:07:34 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:53 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:07:54 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:04:36 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-03 22:07:46 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-03 22:01:45 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-03-03 22:02:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-03-03 22:15:13 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.044 |  |
| 2026-03-03 22:03:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)