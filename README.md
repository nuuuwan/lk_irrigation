# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_08:07:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,377 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 08:07:09 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:05:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:05:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-03-29 08:05:42 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:05:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-03-29 08:05:03 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:04:56 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:04:33 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:04:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-03-29 08:03:43 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:03:16 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:03:11 | Hanwella (Kelani Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-03-29 08:03:04 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:02:58 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:52 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-29 08:02:50 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-29 08:02:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:39 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-03-29 08:02:26 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:20 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:13 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:02:12 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:01:52 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-03-29 08:01:35 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:01:35 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:01:29 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:01:20 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.052 |  |
| 2026-03-29 08:00:41 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:00:36 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:00:36 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-29 07:49:53 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:27:59 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:19:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:14:38 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.052 |  |
| 2026-03-29 07:14:25 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:14:23 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:14:17 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.047 |  |
| 2026-03-29 07:12:55 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 08:02:50 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-29 08:00:36 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-29 07:10:56 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-29 08:02:52 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-29 08:01:35 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:01:29 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:01:35 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:03:04 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:02:13 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 08:02:20 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:05:56 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:00:41 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:05:26 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:26 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:44 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:00:09 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:07:09 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:12 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:04:56 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:58 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:03:16 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:05:03 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:02:47 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:05:42 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:01:20 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:00:36 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:03:43 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:27:59 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-29 08:04:33 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-29 07:05:51 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-29 08:02:39 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-03-29 08:05:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-03-29 08:03:11 | Hanwella (Kelani Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-03-29 08:04:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-03-29 08:05:39 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.047 |  |
| 2026-03-29 08:01:52 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-03-29 08:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.052 |  |
| 2026-03-29 07:01:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-03-29 07:08:35 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)