# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_06:04:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,987 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 06:04:37 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-02-10 06:04:34 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-10 06:04:25 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:04:24 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:03:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-10 06:03:45 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.067 |  |
| 2026-02-10 06:03:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:03:30 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:03:17 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:03:17 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.005 |  |
| 2026-02-10 06:02:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:02:51 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:02:45 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-02-10 06:02:15 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-02-10 06:02:08 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:02:03 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.002 |  |
| 2026-02-10 06:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 06:01:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-10 06:01:42 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:01:16 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-02-10 06:01:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-02-10 06:01:09 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:01:07 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:00:39 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-10 06:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 06:00:09 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-10 05:39:56 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-10 05:39:55 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-10 05:34:56 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-10 05:31:37 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:15:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-02-10 05:15:47 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:15:20 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-10 05:13:58 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.012 |  |
| 2026-02-10 05:11:01 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-10 05:08:58 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 04:01:12 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 5.684 | 🔺 Rising |
| 2026-02-10 06:02:45 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-02-10 06:04:34 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-02-10 05:07:02 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-02-10 06:01:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-10 05:11:01 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-10 06:03:53 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-10 05:05:30 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-02-10 06:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 05:02:44 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 06:01:57 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 06:01:09 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:03:30 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:02:51 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:01:42 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:04:24 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:06:42 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:00:47 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:01:07 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:03:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:01:06 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:03:17 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 05:15:47 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:02:51 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:02:08 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:04:25 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-10 06:02:03 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | -0.002 |  |
| 2026-02-10 06:03:17 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.005 |  |
| 2026-02-10 05:05:40 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.009 |  |
| 2026-02-10 06:00:39 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-10 06:00:09 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-02-10 06:01:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-02-10 06:02:15 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-02-10 05:15:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-02-10 06:04:37 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.032 |  |
| 2026-02-10 06:01:16 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-02-10 06:03:45 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)