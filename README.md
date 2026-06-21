# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_10:19:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 10:19:20 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:18:17 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.008 |  |
| 2026-06-21 10:14:18 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:13:02 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:12:56 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:12:07 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:12:06 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:12:03 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 10:11:00 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 10:10:44 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-06-21 10:10:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-21 10:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-06-21 10:09:48 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:09:10 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:08:03 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:07:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:06:40 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 10:05:21 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-21 10:00:14 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-21 10:10:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-21 10:12:03 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 10:03:50 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 10:03:57 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 10:11:00 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 10:00:54 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:14:18 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:06:09 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:01:40 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:05:53 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:02:57 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:01:59 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:09:48 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:12:07 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:12:56 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:03:41 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:12:06 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:02:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:06:40 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:07:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:08:03 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:05:30 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:04:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:09:10 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:05:13 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:06:14 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:13:02 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:19:20 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:03:14 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:02:20 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 10:18:17 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.008 |  |
| 2026-06-21 10:01:22 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.011 |  |
| 2026-06-21 10:03:36 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.029 |  |
| 2026-06-21 10:03:56 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.039 |  |
| 2026-06-21 10:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-06-21 10:10:44 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)