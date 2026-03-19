# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_01:51:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,063 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 01:51:18 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.004 |  |
| 2026-03-20 01:51:09 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-03-20 01:37:45 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 01:36:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:27:27 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 01:12:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:11:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-03-20 01:07:18 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:06:44 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:05:33 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:04:56 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.413 |  |
| 2026-03-20 01:04:44 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-03-20 01:04:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-03-20 01:04:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-03-20 01:04:04 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.100 |  |
| 2026-03-20 01:04:04 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:03:58 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 1.286 | 🔺 Rising |
| 2026-03-20 01:03:30 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 1.286 | 🔺 Rising |
| 2026-03-20 01:03:15 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-03-20 01:03:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:58 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 1.286 | 🔺 Rising |
| 2026-03-20 01:02:50 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:46 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:24 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:09 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 01:02:02 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:01:56 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-20 01:01:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-20 01:01:41 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:01:13 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-03-20 01:01:13 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.030 |  |
| 2026-03-20 01:01:07 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 01:03:58 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 1.286 | 🔺 Rising |
| 2026-03-20 01:01:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 01:01:56 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-20 01:02:09 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 01:37:45 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 01:27:27 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-20 00:13:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:04:04 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-19 23:07:05 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:03:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:05:33 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 23:01:59 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:06:44 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:36:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:50 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:24 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:07:18 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:12:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:46 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:01:41 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:02:02 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-20 01:51:18 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.004 |  |
| 2026-03-20 01:51:09 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2026-03-20 01:04:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-03-20 01:03:15 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-03-20 01:01:13 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-03-20 01:01:07 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.022 |  |
| 2026-03-20 01:11:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-03-20 01:04:44 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-03-20 01:01:13 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.030 |  |
| 2026-03-20 01:04:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-03-19 22:04:21 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-03-20 01:04:04 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.100 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-20 01:04:56 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.413 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)