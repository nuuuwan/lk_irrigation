# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_08:46:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 08:46:35 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-03-08 08:33:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:23:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2026-03-08 08:10:36 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-08 08:09:48 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:09:41 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.032 |  |
| 2026-03-08 08:09:17 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.141 |  |
| 2026-03-08 08:08:28 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-08 08:08:26 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:08:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:07:44 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-08 08:07:20 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:07:05 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:07:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:06:58 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-08 08:06:44 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:05:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:04:40 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-03-08 08:04:37 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:04:35 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-08 08:04:34 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-08 08:04:11 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 08:03:51 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-03-08 08:03:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:03:14 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 08:03:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:59 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:55 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:52 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:33 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 08:02:19 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-03-08 08:02:16 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:01:50 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.300 |  |
| 2026-03-08 08:01:25 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-08 08:01:19 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-08 08:01:09 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:00:44 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 08:07:44 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-08 08:08:28 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-03-08 08:10:36 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-08 08:06:58 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-08 08:03:14 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 08:02:33 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 08:04:11 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 08:03:02 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:04:37 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:33:19 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:16 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:59 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:52 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:09:48 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:07:20 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:08:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:00:44 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:03:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:02:55 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:03:51 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:06:44 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:07:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:01:09 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:07:05 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:08:26 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:01:19 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:05:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-08 08:04:35 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-08 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-08 08:04:34 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-08 08:02:19 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-03-08 08:46:35 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-03-08 08:01:25 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-08 08:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-03-08 08:04:40 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.020 |  |
| 2026-03-08 08:09:41 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.032 |  |
| 2026-03-08 08:23:59 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.045 |  |
| 2026-03-08 08:09:17 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.141 |  |
| 2026-03-08 08:01:50 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)