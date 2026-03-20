# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_09:05:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,347 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 09:05:02 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:04:43 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-20 09:04:11 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-03-20 09:04:02 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:57 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:52 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:43 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:32 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:29 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-20 09:03:19 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-20 09:03:19 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.026 |  |
| 2026-03-20 09:02:55 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-03-20 09:02:55 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 09:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.055 |  |
| 2026-03-20 09:02:51 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-20 09:02:30 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.111 |  |
| 2026-03-20 09:02:27 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 09:02:26 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:02:07 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2026-03-20 09:01:58 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:01:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:01:29 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-03-20 09:01:13 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-20 09:01:13 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.161 |  |
| 2026-03-20 09:01:06 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 09:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:00:46 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-20 09:00:43 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.034 |  |
| 2026-03-20 09:00:14 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:54:46 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:18:59 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.034 |  |
| 2026-03-20 08:17:25 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.026 |  |
| 2026-03-20 08:15:22 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:12:30 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 09:01:29 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-03-20 09:00:46 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-20 09:03:19 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-20 08:01:52 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-20 09:02:27 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 09:04:43 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-20 09:01:06 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-20 09:02:55 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 09:02:51 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-20 09:01:58 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:43 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:02:26 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:07:35 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:04:02 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:00:14 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:06:30 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:01:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:07:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:52 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:32 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:05:02 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:57 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-03-20 09:03:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 08:06:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-20 09:02:07 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2026-03-20 09:04:11 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-03-20 09:01:13 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-20 09:02:55 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-03-20 09:03:19 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.026 |  |
| 2026-03-20 08:08:14 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-03-20 09:00:43 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.034 |  |
| 2026-03-20 08:18:59 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.034 |  |
| 2026-03-20 09:03:29 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-03-20 09:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.055 |  |
| 2026-03-20 08:04:04 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.067 |  |
| 2026-03-20 08:04:48 | Rathnapura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.096 |  |
| 2026-03-20 09:02:30 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.111 |  |
| 2026-03-20 09:01:13 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)