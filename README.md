# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_02:18:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,986 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 02:18:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:15:28 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-06-21 02:09:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:08:35 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-06-21 02:07:53 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.027 |  |
| 2026-06-21 02:06:51 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:06:07 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.032 |  |
| 2026-06-21 02:04:43 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.085 |  |
| 2026-06-21 02:03:48 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-21 02:03:44 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:03:40 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 02:03:39 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:03:26 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-06-21 02:03:24 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:03:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:03:03 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 02:02:38 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.020 |  |
| 2026-06-21 02:02:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:02:20 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:02:02 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:02:00 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-06-21 02:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:45 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:44 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:42 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:25 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.299 |  |
| 2026-06-21 02:00:56 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.038 |  |
| 2026-06-21 01:57:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 01:02:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-21 02:03:48 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-21 02:03:03 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 02:03:40 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 01:05:32 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-20 18:12:10 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-21 01:12:03 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:00:43 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:57:55 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:02:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:04:43 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:09:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:02:06 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:44 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:42 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:18:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:03:24 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:06:51 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 01:01:24 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:01:45 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 02:15:28 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-06-21 02:02:20 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:03:39 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:03:44 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:02:02 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-06-21 02:08:35 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-06-20 18:00:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.011 |  |
| 2026-06-21 02:02:00 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-06-21 02:02:38 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.020 |  |
| 2026-06-21 02:03:26 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-06-21 02:07:53 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.027 |  |
| 2026-06-21 01:09:11 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.032 |  |
| 2026-06-21 02:06:07 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.032 |  |
| 2026-06-21 00:34:19 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.035 |  |
| 2026-06-21 02:00:56 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.038 |  |
| 2026-06-21 02:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.085 |  |
| 2026-06-21 02:01:25 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)