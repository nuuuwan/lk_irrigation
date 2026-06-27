# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_01:13:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 01:13:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-28 01:10:39 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:09:03 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:08:13 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-28 01:05:45 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.199 |  |
| 2026-06-28 01:04:39 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.009 |  |
| 2026-06-28 01:04:27 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-06-28 01:04:07 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-06-28 01:04:05 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:04:02 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:03:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:03:23 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.112 |  |
| 2026-06-28 01:03:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-28 01:03:13 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.005 |  |
| 2026-06-28 01:02:35 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:31 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:30 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:18 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:14 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:13 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:09 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:08 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:08 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-28 01:02:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:01:37 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:01:33 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-28 01:00:50 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 00:06:43 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-28 01:08:13 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-28 01:13:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-27 18:03:41 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:00:50 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:31 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:30 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:08 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 00:05:45 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 00:03:40 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:35 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:10:39 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:09:03 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:13 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:03:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-28 00:02:54 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:14 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-28 00:02:08 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:01:37 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:18 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:04:02 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:04:05 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:02:09 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-28 01:03:13 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.005 |  |
| 2026-06-28 01:04:39 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.009 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 01:04:27 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-06-28 01:03:13 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-28 01:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-28 01:01:33 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-28 00:06:37 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-06-28 01:04:07 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-06-28 01:02:08 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-06-28 00:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.023 |  |
| 2026-06-28 01:03:23 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.112 |  |
| 2026-06-28 01:05:45 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)