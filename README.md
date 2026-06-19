# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_22:13:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 22:13:42 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:13:35 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:13:02 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:11:20 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.034 |  |
| 2026-06-19 22:10:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 22:10:39 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:09:22 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:08:39 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:08:14 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-06-19 22:07:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | -0.035 |  |
| 2026-06-19 22:07:31 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-19 22:06:58 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:06:45 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:06:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |
| 2026-06-19 22:06:31 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:06:17 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-19 22:06:00 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-06-19 22:05:45 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:04:37 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:04:26 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:04:12 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:03:59 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:03:30 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:02:50 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:02:23 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-19 22:02:09 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-06-19 22:02:01 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:01:50 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:01:27 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | -0.020 |  |
| 2026-06-19 22:01:27 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:01:18 | Nakkala (Kumbukkan Oya) | 0.06 | 🟢 Normal | -0.557 |  |
| 2026-06-19 22:01:07 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:00:18 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 22:06:17 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-19 22:10:55 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-19 22:06:45 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:00:18 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:01:27 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:01:18 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:13:02 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:01:07 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:01:50 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:06:58 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:04:37 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:09:22 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:04:26 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:03:59 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:10:39 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:04:12 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:06:31 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:08:39 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:13:35 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:03:30 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:13:42 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 22:07:31 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-19 22:08:14 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-06-19 20:04:15 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:05:45 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:02:01 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:02:50 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-19 22:01:27 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | -0.020 |  |
| 2026-06-19 22:02:23 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-19 22:02:09 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.020 |  |
| 2026-06-19 22:06:00 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-06-19 22:11:20 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.034 |  |
| 2026-06-19 22:07:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | -0.035 |  |
| 2026-06-19 22:06:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.091 |  |
| 2026-06-19 22:01:18 | Nakkala (Kumbukkan Oya) | 0.06 | 🟢 Normal | -0.557 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)